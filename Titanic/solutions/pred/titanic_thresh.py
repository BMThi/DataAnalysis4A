titanic_thresh = titanic_clip.copy()

titanic_thresh['age'] = pd.qcut(titanic_thresh['age'], 4, duplicates='drop')
titanic_thresh['fare'] = pd.cut(titanic_thresh['fare'], [0,8,15,30,100,200,600])

# titanic_mca['age'] = pd.qcut(titanic_mca['age'], 6, duplicates='drop')
# titanic_mca['fare'] = pd.cut(titanic_mca['fare'], [0,8,15,30,60,100,200,600]) #, duplicates='drop'

titanic_thresh = titanic_thresh.astype('category')