import pickle
import sys
import matplotlib.pyplot
sys.path.append("../tools/")
from feature_format import featureFormat, targetFeatureSplit


### read in data dictionary, convert to numpy array
data_dict = pickle.load( open("../final_project/final_project_dataset.pkl", "rb") )
features = ["salary", "bonus"]
data = featureFormat(data_dict, features)


### your code below
max_salary=0
max_bonus=0
for point in data:
    salary = point[0]/1000
    bonus = point[1]/1000
    if salary>max_salary and salary!=26704.229:
        max_salary=salary
    if bonus>max_bonus and bonus!= 97343.619:
        max_bonus=bonus
    matplotlib.pyplot.scatter( salary, bonus )
    
print("max salary: {}".format(max_salary))
print("max bonus: {}".format(max_bonus))
    
matplotlib.pyplot.xlim(0, max_salary+5000)
matplotlib.pyplot.ylim(0, max_bonus+2500)
    
matplotlib.pyplot.xlabel("salary")
matplotlib.pyplot.ylabel("bonus")
matplotlib.pyplot.show()
