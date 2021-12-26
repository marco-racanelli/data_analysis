#import necessary libraries
import pandas as pd
import numpy as np
import names
import barnum

#generate random first names
first_names = []
for i in range(1500):
  first_names.append(names.get_first_name())

#generate random last names
last_names = []
for j in range(1500):
  last_names.append(names.get_last_name())

#generate random age values
age = []
for y in range(1500):
  age.append(np.random.randint(17,79))

#generate random phone numbers
phone = []
for r in range(1500):
  phone.append(barnum.create_phone())

#generate random password values
pwd = []
for z in range(1500):
  pwd.append(barnum.create_pw())

#generate random phone numbers
phone_2 = []
for t in range(1500):
    phone_2.append(barnum.create_phone())

#generate random job titles
jobs = []
for g in range(1500):
    jobs.append(barnum.create_job_title())

#generate random company names
companies = []
for c in range(1500):
    companies.append(barnum.create_company_name())

#creates a dataframe with the generated values
list_of_tuples = list(zip(first_names, last_names, age, phone, pwd, phone_2,jobs, companies))
df = pd.DataFrame(list_of_tuples,columns = ['first_name', 'last_name','age', 'phone',
                                            'password', 'phone_2','role', 'company'])
