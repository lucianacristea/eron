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
from class_vis import prettyPicture, output_image


### features_train and features_test are the features for the training
### and testing datasets, respectively
### labels_train and labels_test are the corresponding item labels
features_train, features_test, labels_train, labels_test = preprocess()
clf = GaussianNB()
t0 = time()
clf.fit(features_train, labels_train)
print ("Time to train:", round(time()-t0, 3), "s")

t0 = time()
pred=clf.predict(features_test)
print ("Time to make prediction:", round(time()-t0, 3), "s")

### calculate and return the accuracy on the test data
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)
print("Accuracy of Naive Bayes predictor is: {}".format(accuracy))
##################################################################

### draw the decision boundary with the text points overlaid
prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())

