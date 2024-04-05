## Factor Analysis of Mixed Data - Titanic tutorial
### Titanic Survival Prediction

In this tutorial, we will use the [titanic dataset](https://www.kaggle.com/competitions/titanic/data), from Kaggle competition "_Titanic - Machine Learning from Disaster_".

Our aim here is to mobilise several dimension reduction algorithms covered in the lesson (PCA, MCA) and attempt to predict passengers' chances of survival.
As prediction algorithms are not at the heart of this course (unlike Machine Learning!), we will not optimise this part: we could implement much more efficient algorithms than the naive ones proposed here.

For this tutorial, we will be using the [`prince`](https://maxhalford.github.io/prince/) package, based on the same syntax as scikit-learn.