import pickle
import numpy
numpy.random.seed(42)


### The words (features) and authors (labels), already largely processed.
### These files should have been created from the previous (Lesson 10)
### mini-project.
words_file = "../text_learning/your_word_data.pkl" 
authors_file = "../text_learning/your_email_authors.pkl"
word_data = pickle.load( open(words_file, "rb"))
authors = pickle.load( open(authors_file, "rb") )


### test_size is the percentage of events assigned to the test set (the
### remainder go into training)
### feature matrices changed to dense representations for compatibility with
### classifier functions in versions 0.15.2 and earlier
from sklearn.model_selection import train_test_split
features_train, features_test, labels_train, labels_test = train_test_split(word_data, authors, test_size=0.1, random_state=42)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(sublinear_tf=True, max_df=0.5,
                             stop_words='english')
features_train = vectorizer.fit_transform(features_train)
features_test  = vectorizer.transform(features_test).toarray()

print("Training points : {}".format(len(features_train.toarray())))

### a classic way to overfit is to use a small number
### of data points and a large number of features;
### train on only 150 events to put ourselves in this regime
###features_train = features_train[:150].toarray()
features_train = features_train[:150]
labels_train   = labels_train[:150]

### your code goes here
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
classifier=DecisionTreeClassifier()
classifier=classifier.fit(features_train,labels_train)

# get importance
importance = classifier.feature_importances_
# summarize feature importance

feature_names = vectorizer.get_feature_names()

for i,v in enumerate(importance):
  if v>0.2:
    print("Feature: {}, Score: {}, Number: {}".format(feature_names[i],v,i))
    
top_features = [(number, feature, feature_names[number]) for number, feature in 
                zip(range(len(importance)), importance) if feature > 0.2]
print(top_features)

predictions=classifier.predict(features_test)

print("Accuracy: {}".format(accuracy_score(labels_test, predictions)))
