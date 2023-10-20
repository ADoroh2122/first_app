import pandas as pd
from pathlib import Path

# Set our folder directory
folder_dir = f'{Path(__file__).parents[0]}\\data'

d1=pd.read_csv(r'C:\Users\adoro\OneDrive\Documents\GitHub\first_app\src\data\student-mat.csv', sep=";", header= None)
d1

d1.columns = d1.iloc[0]
d1.columns
d1 = d1.drop(index=0)
d1

d1.columns = d1.columns.str.lower().str.strip().str.replace(' ', '_')
d1.columns

d1['id'] = range(1, len(d1) +1) 


d2=pd.read_csv(r"C:\Users\adoro\OneDrive\Documents\GitHub\first_app\src\data\student-por.csv", sep=";", header= None)
d2

d2.columns = d2.iloc[0]
d2.columns
d2= d2.drop(index=0)
d2

d2.columns = d2.columns.str.lower().str.strip().str.replace(' ', '_')
d2.columns

d2['id'] = range(1, len(d2) +1) 

#d2.info()

d1['age'] = d1['age'].astype(int)
d2['age'] = d2['age'].astype(int)

d1['medu'] = d1['medu'].astype(int)
d2['medu'] = d2['medu'].astype(int)

d1['fedu'] = d1['fedu'].astype(int)
d2['fedu'] = d2['fedu'].astype(int)

d1['traveltime'] = d1['traveltime'].astype(int)
d2['traveltime'] = d2['traveltime'].astype(int)

d1['studytime'] = d1['studytime'].astype(int)
d2['studytime'] = d2['studytime'].astype(int)

d1['failures'] = d1['failures'].astype(int)
d2['failures'] = d2['failures'].astype(int)

d1['schoolsup'] = d1['schoolsup'].astype(bool)
d2['schoolsup'] = d2['schoolsup'].astype(bool)

d1['famsup'] = d1['famsup'].astype(bool)
d2['famsup'] = d2['famsup'].astype(bool)

d1['paid'] = d1['paid'].astype(bool)
d2['paid'] = d2['paid'].astype(bool)

d1['activities'] = d1['activities'].astype(bool)
d2['activities'] = d2['activities'].astype(bool)

d1['nursery'] = d1['nursery'].astype(bool)
d2['nursery'] = d2['nursery'].astype(bool)

d1['higher'] = d1['higher'].astype(bool)
d2['higher'] = d2['higher'].astype(bool)

d1['internet'] = d1['internet'].astype(bool)
d2['internet'] = d2['internet'].astype(bool)

d1['romantic'] = d1['romantic'].astype(bool)
d2['romantic'] = d2['romantic'].astype(bool)

d1['famrel'] = d1['famrel'].astype(int)
d2['famrel'] = d2['famrel'].astype(int)

d1['freetime'] = d1['freetime'].astype(int)
d2['freetime'] = d2['freetime'].astype(int)

d1['goout'] = d1['goout'].astype(int)
d2['goout'] = d2['goout'].astype(int)

d1['dalc'] = d1['dalc'].astype(int)
d2['dalc'] = d2['dalc'].astype(int)

d1['walc'] = d1['walc'].astype(int)
d2['walc'] = d2['walc'].astype(int)

d1['health'] = d1['health'].astype(int)
d2['health'] = d2['health'].astype(int)

d1['absences'] = d1['absences'].astype(int)
d2['absences'] = d2['absences'].astype(int)

d1['g1'] = d1['g1'].astype(int)
d2['g1'] = d2['g1'].astype(int)

d1['g2'] = d1['g2'].astype(int)
d2['g2'] = d2['g2'].astype(int)

d1['g3'] = d1['g3'].astype(int)
d2['g3'] = d2['g3'].astype(int)

con_str = 'mongodb+srv://andrew:<password>@lancers.ureqiwj.mongodb.net/?retryWrites=true&w=majority'

import pymongo

client = pymongo.MongoClient(con_str)

# Create databases
db = client.db

# Create a collection from the database
student = db.student
classmate = db.classmate

db.student.drop()
db.classmate.drop()

student.insert_many(d1.to_dict(orient='records'))

classmate.insert_many(d2.to_dict(orient='records'))

print('It has been uploaded')

