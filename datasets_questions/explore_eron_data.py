""" 
    Starter code for exploring the Enron dataset (emails + finances);
    loads up the dataset (pickled dict of dicts).
    The dataset has the form:
    enron_data["LASTNAME FIRSTNAME MIDDLEINITIAL"] = { features_dict }
    {features_dict} is a dictionary of features associated with that person.
    You should explore features_dict as part of the mini-project,
    but here's an example to get you started:
    enron_data["SKILLING JEFFREY K"]["bonus"] = 5600000
    
"""

import pickle

enron_data = pickle.load(open("../final_project/final_project_dataset.pkl", "rb"))
print("People (data points) in dataset: {}".format(len(enron_data)))
for key, value in enron_data.items():
    print("No. of attributes for one person (data point) in dataset: {}".format(len(list(filter(bool, value)))))
    print(key, value)
    break
k=0   
for key, value in enron_data.items():
    if key[value]["poi"]==1:
        k=+1
 
print("In the data set there are {} POI (persons of interest).".format(k))
