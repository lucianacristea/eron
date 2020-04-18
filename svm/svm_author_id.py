

""" 
    This is the code to accompany the Lesson 2 (SVM) mini-project.
    Use a SVM to identify emails from the Enron corpus by their authors:    
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

from sklearn.svm import SVC
features_train, features_test, labels_train, labels_test = preprocess()
clf = SVC(kernel='rbf', C=10000.0)
t0 = time()
### features_train = features_train[:int(len(features_train)/100)]
### labels_train = labels_train[:int(len(labels_train)/100)]
clf.fit(features_train, labels_train)
print ("Time to train:", round(time()-t0, 3), "s")

t0 = time()
pred=clf.predict(features_test)
print("Element 9:", pred[10])
print("Element 10:", pred[10])
print("Element 26:", pred[26])
print("Element 50:", pred(features_test[50])
print ("Time to make prediction:", round(time()-t0, 3), "s")

### calculate and return the accuracy on the test data
from sklearn.metrics import accuracy_score
accuracy = accuracy_score(pred, labels_test)
print("Accuracy of SVM predictor is: {}".format(accuracy))
##################################################################

### draw the decision boundary with the text points overlaid
prettyPicture(clf, features_test, labels_test)
output_image("test.png", "png", open("test.png", "rb").read())

#########################################################
