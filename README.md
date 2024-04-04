## <a href="https://www.insa-toulouse.fr/"><img src="https://www.insa-toulouse.fr/wp-content/uploads/2022/10/Logo_INSAvilletoulouse-RVB.jpg" width=90px; alt="INSA Toulouse"/></a> &nbsp;<small>|</small>&nbsp; [*Applied Mathematics*](http://www.math.insa-toulouse.fr/fr/index.html),&nbsp; [`Data Science`](http://www.math.insa-toulouse.fr/fr/enseignement.html) 


# Data Analysis

This course is dedicated to learning the _multidimensional exploratory methods_ essential for data preparation, such as principal component analysis, linear discriminant analysis, correspondence analysis, multidimensional postioning, non-negative factorization, etc., as well as unsupervised classification (clustering) using k-means, CAH, DBSCAN, Gaussian mixtures.

> [Course moodle page](https://moodle.insa-toulouse.fr/course/view.php?id=1340)

<br>


The tutorials of this course are in the form of Jupyter notebooks.
- Make sure you have an **R kernel** installed on Jupyter. Otherwise: [Native R kernel for Jupyter](https://github.com/IRkernel/IRkernel) on GitHub.
-  I highly recommend using [JupyterLab](https://jupyter.org/install), whose interface offers far more possibilities (including opening several notebooks simultaneously on several tabs) than conventional notebooks.

<br>


## [Class Project](Velib)

**Data** - [Velib dataset](Velib/data/)

**Launch notebook** - [Lauch notebook in Python](Velib/TP_velib_Python.ipynb)

**Launch notebook** - [Lauch notebook in R](Velib/TP_velib_R.ipynb) 

<br>


## PART I: Basic dimension reduction methods

**TP - Digits** - [Visualization and denoising of handwritten digits](Digits/). <br>
_Goal:_ Refresh Principal Component Analysis (PCA) and the associated [Python](https://www.python.org/) formulas. Apply this technique to a simple dataset made up of handwritten digits.

**TP - Human Resources (HR)** - [HR Data Analysis and Attrition Prediction](HumanResources/). <br>
_Goal:_ Implement a classification using a logistic regression model on the one hand, and an LDA decomposition on the other, on HR data.

<br>


## PART II: Clustering methods

**TP - Wine** - [Study of different physico-chemical measurements on wine](Wine/). <br>
_Goal:_ To apply the different concepts studied during the course on clustering on _quantitative_ data, using [R](https://www.r-project.org/) language.

**TP - Mars** - [Large multi-spectral image segmentation: Representing the geological diversity of the surface of Mars](Mars/). <br>
_Goal:_ To apply the different concepts studied during the course on clustering on _quantitative_ data, using [Python](https://www.python.org/) language. More precisely, apply clustering to pixels of a multi-spectral image representing the surface of Mars.

<br>


##  PART III: Advanced factorial methods

**TP - Housetasks & Hobbies** - [Exploration of basic sociological data](Housetasks&Hobbies/) <br>
_Goal:_ To use in practice Correspondence Analysis (**CA**) and Multiple Correspondence Analysis (**MCA**), using [R](https://www.r-project.org/) language.

**TP - Titanic** - [Titanic Survival Prediction](Titanic/) <br>
_Goal:_ To mobilise several dimension reduction algorithms covered in the lesson (**PCA**, **MCA**, **MFA**) and attempt to predict passengers' chances of survival, using [Python](https://www.python.org/) language.

**TP - Movie Lens** - [What movie should I watch this evening?](MovieLens/) <br>
_Goal:_ To use in practice Non-Negative Matrix Factorization (**NMF**), using [Python](https://www.python.org/) language. More precisely, to build a movie recommendation system.
