#!/usr/bin/python

""" 
    This is the code to accompany the Naive Bayes mini-project. 
    Use a Naive Bayes Classifier to identify emails by their authors
    
    authors and labels:
    Sara has label 0
    Chris has label 1
"""
    
import sys
from time import time
sys.path.append("../tools/")
from email_preprocess import preprocess
###from class_vis import prettyPicture, output_image


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()

##################################################################
### create and predict according to Naive Bayes algorithm###
from sklearn.naive_bayes import GaussianNB
clf=GaussianNB()
t0 = time()
clf.fit(features_train, labels_train)
print ("Time to train:", round(time()-t0, 3), "s")

###new plot
import numpy as np
import matplotlib.pyplot as plt

# Plot the decision boundary. For that, we will assign a color to each
# point in the mesh [x_min, x_max]x[y_min, y_max].
x_min, x_max = features_train[:, 0].min() - 1, features_train[:, 0].max() + 1
y_min, y_max = features_train[:, 1].min() - 1, features_train[:, 1].max() + 1
xx, yy = np.meshgrid(np.arange(x_min, x_max, h), np.arange(y_min, y_max, h))
Z = clf.predict(np.c_[xx.ravel(), yy.ravel()])

# Put the result into a color plot
Z = Z.reshape(xx.shape)
plt.pcolormesh(xx, yy, Z, cmap=plt.cm.Paired)

# Plot also the training points
plt.scatter(X[:, 0], X[:, 1], c=Y, cmap=plt.cm.Paired, edgecolors='k')
plt.title('3-Class classification using Naive Bayes algorithm')
plt.axis('tight')
plt.show()

###########


### draw the decision boundary with the text points overlaid
###prettyPicture(clf, features_test, labels_test)
###output_image("test.png", "png", open("test.png", "rb").read())

t0 = time()
pred=clf.predict(features_test)
print ("Time to make prediction:", round(time()-t0, 3), "s")

### calculate and return the accuracy on the test data
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)
print("Accuracy of Naive Bayes predictor is: {}".format(accuracy))
##################################################################
