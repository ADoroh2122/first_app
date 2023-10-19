import requests
import pandas as pd

class Base:

    def __init__(self):
        self.get_data()
        self.get_data2()

    def get_data(self):
        '''Scrapes data from the csv and creates a Dataframe from it'''
        self.d1 = pd.read_csv(r'C:\Users\adoro\OneDrive\Documents\GitHub\first_app\student+performance\student\student-mat.csv')
        return self.d1
    
    def get_data2(self):
        self.d2 = pd.read_csv(r'C:\Users\adoro\OneDrive\Documents\GitHub\first_app\student+performance\student\student-por.csv')
        return self.d2
     

if __name__ == '__main__':
    c = Base()
    print(c.d1)
    print(c.d2)