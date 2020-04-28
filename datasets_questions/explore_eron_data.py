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
tp=0
poitp=""
for key, value in enron_data.items():
    if value["poi"]==1:
        k+=1
    if key=="PRENTICE JAMES":
        print("Total value of the stock belonging to {} is {}".format(key, value["total_stock_value"]))
    if key=="COLWELL WESLEY":
        print("Number of email messages from {} to POI is {}".format(key, value["from_this_person_to_poi"]))
    if key=="SKILLING JEFFREY K":
        print("Value of stock options exercised by {} is {}".format(key, value["exercised_stock_options"]))
        if tp<value["total_payments"]:
            tp=value["total_payments"]
            poitp=key
    if key=="FASTOW ANDREW":
        if tp<value["total_payments"]:
            tp=value["total_payments"]
            poitp=key
    if key=="LAY KENNETH":
        if tp<value["total_payments"]:
            tp=value["total_payments"]
            poitp=key
 
print("In the data set there are {} POI (persons of interest).".format(k))
print("Most money has been taken by {} and the value was {}".format(poitp, tp))

k=0
### enron_poi = pickle.load(open("../final_project/poi_names.txt", "rb"))
enron_poi=open("../final_project/poi_names.txt", "r")
for ln in enron_poi:
  if ln.startswith('(y)') or ln.startswith('(n)'):
    k+=1
 
print("In the txt data set there are {} POI (persons of interest).".format(k))
