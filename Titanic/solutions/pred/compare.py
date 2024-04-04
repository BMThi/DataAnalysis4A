accuracy = pd.DataFrame([[kmeans_accuracy_famd,svm_accuracy_famd,logistic_accuracy_famd],
              [kmeans_accuracy_mca,svm_accuracy_mca,logistic_accuracy_mca]],
            index = ['FAMD','MCA'],
            columns = ['$k$-means','SVM','logistic']
)

display(accuracy.style.format('{:.2%}').highlight_max(color='lightblue'))