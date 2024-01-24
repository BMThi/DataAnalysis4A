param = {
    'n_components' : [15, 20, 25],
    'alpha_W' : [0.001, 0.01, 0.1],
    'l1_ratio' : [0], 
    'max_iter' : [500, int(1e3), int(1e4)]
}
n_search = 3**3

# Keep track of RMSE and parameters
grid_search = pd.DataFrame(columns = ['n_components', 'alpha_W', 'l1_ratio', 'max_iter', 'RMSE'])

# nb of folds in ShuffleSplit CV
n_folds = 5   
cv = ShuffleSplit(n_splits=5, test_size=0.33, random_state=0) # 5-fold scheme

i = 0
# Performing the Grid search
for n_components in param['n_components']:
    for alpha_W in param['alpha_W']:
        for l1_ratio in param['l1_ratio']:
            for max_iter in param['max_iter']:

                err = 0
                n_iter = 0
                i += 1
                print('---')
                print('Search %i / %i' % (i, n_search))
                for _, (train_index, test_index) in enumerate(cv.split(X_train)):
    
                    # Split into training and test set
                    X_train_cv, X_test_cv = X_train[train_index], X_train[test_index]
                    y_train_cv, y_test_cv = y_train[train_index], y_train[test_index]
            
                    # Construct the R matrices
                    R_train = make_R(X_train_cv, y_train_cv, R_shape)
                    R_test = make_R(X_test_cv, y_test_cv, R_shape)

                    # Current parameters for NMF decomposition
                    parametersNMF = {
                        'n_components' : n_components,
                        'init' : 'nndsvda', 
                        'alpha_W' : alpha_W,
                        'l1_ratio' : l1_ratio,
                        'max_iter' : max_iter
                    }
                    nmf = NMF(**parametersNMF)
                
                    # Train the NMF model
                    t0 = time.time()
                    nmf.fit(R_train)  
                    W = nmf.transform(R_train)
                    H = nmf.components_
                    n_iter += nmf.n_iter_ 

                    # Make predictions & clip values
                    R_pred = W.dot(H)
                    R_pred[R_pred > 5] = 5.
                    R_pred[R_pred < 1] = 1.

                    # Computing the error on the validation set 
                    err += get_rmse(R_pred, R_test)
        
                #print "RMSE Error : ", err / n_folds
                grid_search.loc[i] = [n_components, alpha_W, l1_ratio, max_iter, err/n_folds]
                print("n_components: %i, alpha_W: %f, l1_ratio: %f, max_iter: %i, RMSE: %f" % (n_components, alpha_W, l1_ratio, max_iter, err/n_folds))
                print("Mean number of iterations: %i" % (n_iter/n_folds))
    
                
best_params = grid_search.sort_values('RMSE')[:1]
print('\n*** best params ***')
print(best_params)