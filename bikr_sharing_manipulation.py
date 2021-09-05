import pandas as pd 
import numpy as np 

bike_old_train=pd.read_csv(r'/Users/sushilsunilkumardeshmukh/university_summer_2021/project/bike_sharing_project/bike-sharing-demand/train.csv')
bike_old_test=pd.read_csv(r'/Users/sushilsunilkumardeshmukh/university_summer_2021/project/bike_sharing_project/bike-sharing-demand/test.csv')


# print(bike_old_train['workingday'])
# print(bike_old_test['workingday'])

#print(bike_old_test.dtypes)

for i in range(len(bike_old_test)):
    if bike_old_test['workingday'][i]==0:
        bike_old_test['workingday'].replace(0,'no',inplace=True)
    else:
        bike_old_test['workingday'].replace(1,'yes',inplace=True)

#print(bike_old_test['workingday'])


for i in range(len(bike_old_test)):
    if bike_old_test['holiday'][i]==0:
        bike_old_test['holiday'].replace(0,'no',inplace=True)
    else:
        bike_old_test['holiday'].replace(1,'yes',inplace=True)

#print(bike_old_test['holiday'])


for i in range(len(bike_old_test)):
    if bike_old_test['weather'][i]==1:
        bike_old_test['weather'].replace(1,'clear',inplace=True)
    elif bike_old_test['weather'][i]==2:
        bike_old_test['weather'].replace(2,'mist',inplace=True)
    elif bike_old_test['weather'][i]==3:
        bike_old_test['weather'].replace(3,'light snow',inplace=True)
    elif bike_old_test['weather'][i]==4:
        bike_old_test['weather'].replace(4,'heavy snow',inplace=True)

#print(bike_old_test['weather'])






for i in range(len(bike_old_train)):
    if bike_old_train['workingday'][i]==0:
        bike_old_train['workingday'].replace(0,'no',inplace=True)
    else:
        bike_old_train['workingday'].replace(1,'yes',inplace=True)

#print(bike_old_train['workingday'])


for i in range(len(bike_old_train)):
    if bike_old_train['holiday'][i]==0:
        bike_old_train['holiday'].replace(0,'no',inplace=True)
    else:
        bike_old_train['holiday'].replace(1,'yes',inplace=True)

#print(bike_old_train['holiday'])

for i in range(len(bike_old_train)):
    if bike_old_train['weather'][i]==1:
        bike_old_train['weather'].replace(1,'clear',inplace=True)
    elif bike_old_train['weather'][i]==2:
        bike_old_train['weather'].replace(2,'mist',inplace=True)
    elif bike_old_train['weather'][i]==3:
        bike_old_train['weather'].replace(3,'light snow',inplace=True)
    elif bike_old_train['weather'][i]==4:
        bike_old_train['weather'].replace(4,'heavy snow',inplace=True)

#print(bike_old_train['weather'])



print(bike_old_test,bike_old_train)



bike_old_train.to_excel(r'/Users/sushilsunilkumardeshmukh/university_summer_2021/project/bike_sharing_project/bike-sharing-demand/train_1.xlsx')
bike_old_test.to_excel(r'/Users/sushilsunilkumardeshmukh/university_summer_2021/project/bike_sharing_project/bike-sharing-demand/test_1.xlsx')




