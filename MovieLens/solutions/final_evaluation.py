parametersNMF_opt = {
    'n_components' : 15,
    'init' : 'nndsvda', 
    'alpha_W' : 0.001,
    'l1_ratio' : 0,
    'max_iter' : int(1e4)
}

nmf = NMF(**parametersNMF_opt)
     
# Train
nmf.fit(R_train)  
W = nmf.transform(R_train)
H = nmf.components_

# Make predictionscPickle
R_pred = W.dot(H)
R_pred[R_pred > 5] = 5.
R_pred[R_pred < 1] = 1.

# Compute error on the test set 
print('RMSE test:', get_rmse(R_pred, R_test))