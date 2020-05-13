""" 
    Skeleton code for k-means clustering mini-project.
"""




import pickle
import numpy
import matplotlib.pyplot as plt
import sys
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit




def Draw(pred, features, poi, mark_poi=False, name="image.png", f1_name="feature 1", f2_name="feature 2"):
    """ some plotting code designed to help you visualize your clusters """

    ### plot each cluster with a different color--add more colors for
    ### drawing more than five clusters
    colors = ["b", "c", "k", "m", "g"]
    for ii, pp in enumerate(pred):
        plt.scatter(features[ii][0], features[ii][1], color = colors[pred[ii]])

    ### if you like, place red stars over points that are POIs (just for funsies)
    if mark_poi:
        for ii, pp in enumerate(pred):
            if poi[ii]:
                plt.scatter(features[ii][0], features[ii][1], color="r", marker="*")
    plt.xlabel(f1_name)
    plt.ylabel(f2_name)
    plt.savefig(name)
    plt.show()



### load in the dict of dicts containing all the data on each person in the dataset
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )
### there's an outlier--remove it! 
data_dict.pop("TOTAL", 0)


### the input features we want to use 
### can be any key in the person-level dictionary (salary, director_fees, etc.) 
feature_1 = "salary"
feature_2 = "exercised_stock_options"
feature_3 = "total_payments"
poi  = "poi"

from sklearn.cluster import KMeans

"""
###cluster with 2 features
features_list2 = [poi, feature_1, feature_2]
data2 = featureFormat(data_dict, features_list2 )
poi, finance_features2 = targetFeatureSplit( data2 )


### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
for f1, f2 in finance_features2:
    plt.scatter( f1, f2 )
plt.show()


kmeans2 = KMeans(n_clusters=2).fit(finance_features2)
pred2=kmeans2.predict(finance_features2)
"""

###cluster with 3 features
features_list = [poi, feature_1, feature_2, feature_3]
data = featureFormat(data_dict, features_list )
poi, finance_features = targetFeatureSplit( data )

### in the "clustering with 3 features" part of the mini-project,
### you'll want to change this line to 
### for f1, f2, _ in finance_features:
### (as it's currently written, the line below assumes 2 features)
max_exercised_stock_options=0
min_exercised_stock_options=0
max_salary=0
min_salary=0
for f1, f2, _ in finance_features:
    if f1>max_salary:
        max_salary=f1
        
    if f2>max_exercised_stock_options:
        max_exercised_stock_options=f2
    
    if min_salary==0:
        min_salary=f1
    else:
        if f1<min_salary and f1!=0:
            min_salary=f1
    
    if min_exercised_stock_options==0:
        min_exercised_stock_options=f2
    else:
        if f2<min_exercised_stock_options and f2!=0:
            min_exercised_stock_options=f2
    plt.scatter( f1, f2 )
plt.show()

print("min salary: {}".format(min_salary))
print("max salary: {}".format(max_salary))

print("min exercised_stock_options: {}".format(min_exercised_stock_options))
print("max exercised_stock_options: {}".format(max_exercised_stock_options))

### cluster here; create predictions of the cluster labels
### for the data and store them to a list called pred
kmeans = KMeans(n_clusters=3).fit(finance_features)
pred=kmeans.predict(finance_features)


### rename the "name" parameter when you change the number of features
### so that the figure gets saved to a different file
try:
     ###Draw(pred2, finance_features2, poi, mark_poi=False, name="clusters.pdf", f1_name=feature_1, f2_name=feature_2)
     Draw(pred, finance_features, poi, mark_poi=False, name="clusters3.pdf", f1_name=feature_1, f2_name=feature_2)
except NameError:
    print("no predictions object named pred found, no clusters to plot")
    
 
