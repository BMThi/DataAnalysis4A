# Class 7 is far too low to be considered relevant. 
# -> We will treat it as outliers, and merge it with the Class 5. 
# Thus the ground truth consists effectively of 6 classes.

clusters_expert[clusters_expert==7] = 5

for i in range(10):
    print(i, ':', np.sum(clusters_expert==i) )