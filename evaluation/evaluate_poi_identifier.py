
"""
    Starter code for the evaluation mini-project.
    Start by copying your trained/tested POI identifier from
    that which you built in the validation mini-project.
    This is the second step toward building your POI identifier!
    Start by loading/formatting the data...
"""

import pickle
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit

data_dict = pickle.load(open("../final_project/final_project_dataset.pkl", "rb") )

### add more features to features_list!
features_list = ["poi", "salary"]

data = featureFormat(data_dict, features_list, sort_keys = '../tools/python2_lesson14_keys.pkl')
labels, features = targetFeatureSplit(data)

### your code goes here 
from sklearn.model_selection import train_test_split
###features_train, features_test, labels_train, labels_test = train_test_split(features, labels)
features_train, features_test, labels_train, labels_test = train_test_split(features, labels, test_size = 0.3, random_state = 42)

from sklearn.tree import DecisionTreeClassifier
clf = DecisionTreeClassifier()

clf = clf.fit(features_train, labels_train)
###clf = clf.fit(features, labels)
pred=clf.predict(features_test)
###pred=clf.predict(features)
import numpy as np
from sklearn.metrics import confusion_matrix, precision_score, recall_score, classification_report, accuracy_score
print ("Number of POI's: ", np.count_nonzero(pred))
print ("People in Test Set: ", len(pred)) 
print (confusion_matrix(labels_test, pred))
print ("Precision is {}". format(precision_score(labels_test, pred)))
print ("Recall is {}". format(recall_score(labels_test, pred)))
print (classification_report(labels_test, pred))

accuracy = accuracy_score(labels_test, pred)
print("Accuracy of Decision Tree predictor is: {}".format(accuracy))
##################################################################
