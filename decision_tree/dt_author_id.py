
""" 
    This is the code to accompany the Lesson 3 (decision tree) mini-project.
    Use a Decision Tree to identify emails from the Enron corpus by author:    
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

print("No. of features in the train data is:{}".format(len(features_train[0])

from sklearn.tree import DecisionTreeClassifier

clf = DecisionTreeClassifier(min_samples_split=40)
t0 = time()
### features_train = features_train[:int(len(features_train)/100)]
### labels_train = labels_train[:int(len(labels_train)/100)]
clf.fit(features_train, labels_train)
print("Time to train:", round(time()-t0, 3), "s")

t0 = time()
pred=clf.predict(features_test)
print("Time to make prediction:", round(time()-t0, 3), "s")

### calculate and return the accuracy on the test data
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(labels_test, pred)
print("Accuracy of Decision Tree predictor is: {}".format(accuracy))
##################################################################

### draw the decision boundary with the text points overlaid
### we only take the first two features.
new_features_train=features_train[:, :2]
new_features_test=features_test[:, :2]
new_clf= DecisionTreeClassifier(min_samples_split=40)
new_clf.fit(new_features_train, labels_train)
import matplotlib.pyplot as plt
plt=prettyPicture(new_clf, new_features_test, labels_test)
plt.show()
###output_image("test.png", "png", open("test.png", "rb").read())

#########################################################
#########################################################
