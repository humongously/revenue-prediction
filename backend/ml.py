import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics 


df = pd.read_csv (r'dataset.csv');

# first five row 
# print (df.head())

# row and colm

#print(df.shape)          
'''
(145830, 10)
'''

# more info 
# print(df.info())
'''
Data columns (total 10 columns):
 #   Column        Non-Null Count   Dtype  
---  ------        --------------   -----  
 0   Date          145830 non-null  object 
 1   Bill Number   145830 non-null  object 
 2   Item Desc     145830 non-null  object 
 3   Time          145830 non-null  object 
 4   Quantity      145830 non-null  int64  
 5   Rate          145830 non-null  float64
 6   Tax           145830 non-null  float64
 7   Discount      145830 non-null  float64
 8   Total         145830 non-null  float64
 9   Category      145830 non-null  object 
dtypes: float64(4), int64(1), object(5)
memory usage: 11.1+ MB

'''

# categorical features 
#  Date  Bill Number  Item Desc   Time Category


# missing values 
# print(df.isnull().sum() );

'''
Date            0
Bill Number     0
Item Desc       0
Time            0
Quantity        0
Rate            0
Tax             0
Discount        0
Total           0
Category        0
dtype: int64
'''
#--------  finding statistics 
# print(df.describe())

'''
           Quantity           Rate            Tax       Discount          Total
count  145830.000000  145830.000000  145830.000000  145830.000000  145830.000000
mean        1.121299     161.782259      48.929061       0.095079     224.959852
std         0.477237     102.244631      40.272851       3.720735     164.960776
min         1.000000       0.010000       0.000000       0.000000       0.010000
25%         1.000000      95.000000      22.560000       0.000000     117.560000
50%         1.000000     125.000000      32.060000       0.000000     167.060000
75%         1.000000     225.000000      72.000000       0.000000     315.000000
max        30.000000    2100.000000    2731.250000     825.000000   14231.250000
'''
#  25% of values are less than 1  

#--- Numerical features 
# distribution plot of rates 

# sns.set()
# plt.figure(figsize=(6,6))
# plt.title("Rate distribution plot ")
# sns.distplot(df['Rate'],bins=15)
# plt.show()

# # count plot of rates
# plt.title("Total distribution plot ")
# # sns.countplot(x='Discount' , data=df,bins=15)
# sns.distplot(df['Total'],bins=15)
# plt.show() 


#-- Categorical distributions

#Category
# sns.set()
# plt.title("countplot of Category in dataset")
# sns.countplot(x='Category' , data=df)
# plt.show()

# #Date
# sns.set()
# sns.countplot(x='Date' , data=df)
# plt.show()




#there is may x axis values are similiar in categorical like same date or same category
# so first we count the values in category colm
# print(df['Category'].value_counts())

'''
FOOD                57023
BEVERAGE            43573
TOBACCO             36496
LIQUOR               6200
MISC                 1187
WINES                 809
MERCHANDISE           487
LIQUOR & TPBACCO       54
LIQUOR                  1
Name: Category, dtype: int64
'''

# if some colm values same like wines or wine like that so we just replace function 
# and replace the wine or wines into 1 fix name df.replace()

#--------------------- Label encoding 
# here we convert categorical data into numerical values
encoder = LabelEncoder()

#now it will transform the categorical data into fix numerical values 
df['Category'] = encoder.fit_transform(df['Category']);

#now check top 5 values
#print(df.head())           #it will convert BEVERAGE ,wines ... into 0 ,1 like these values

# dat is also categorical
df['Date'] = encoder.fit_transform(df['Date']);

# bill number 
# df['BillNumber'] = encoder.fit_transform(df['BillNumber']);
# print(df['Bill Number'])


# items  
df['ItemDesc'] = encoder.fit_transform(df['ItemDesc']);

# time  Time
df['Time'] = encoder.fit_transform(df['Time']);

# now we check
# print(df.head())

'''
  Date    ItemDesc   Time  Quantity   Rate    Tax  Discount   Total  Category
0     4        352  12416         1   50.0  11.88       0.0   61.88         0
1     4        362  12416         1  100.0  23.75       0.0  123.75         0
2     4        344  12589         1   40.0   9.50       0.0   49.50         0
3     4        352  12759         1   50.0  11.88       0.0   61.88         0
4     4        364  12794         1   45.0  10.69       0.0   55.69         0
'''

#--------------------------------  heatmap -------------------------------
# Heatmaps describe relationships between variables in form of colors instead of numbers
#get top 70000 rows 
# dd = df.iloc[:70000]


'''
# Plot the heatmap
dd=df.head(25)
# plt.figure(figsize=(10,10))
# heat_map = sns.heatmap( dd, linewidth = 1 , annot = True)
# plt.title( "HeatMap of top data" )
# plt.show()

---------------------------------------

fig, ax = plt.subplots(figsize=(10,6))
sns.heatmap(dd.corr(), center=0, annot=True)
ax.set_title("Heatmap of dataset") 
plt.show()

'''
#------------------------ split ------------------------------------------
# target is our total revenue  colm

#storing all colm in list
colms = []
for col in df.columns:
    colms.append(col)
    # print(col)

#target is Total revenue
#now we drop it and store it into x 

# x will have all features expect target colm
# if we dropping colm so axis =1 , for row axis =0
x =df.drop(columns='Total',axis=1)
y = df['Total']
# print(x)

#---now we split training and testing data 
# 20% as test 
x_train,x_test,y_train,y_test  = train_test_split(x,y,test_size=0.3 , random_state=2)

# now we check how many are in train and test
# print(x.shape  ,  x_train.shape , x_test.shape)
#  (145830, 9) (116664, 9) (29166, 9)

#-- now we train the model
regressor = XGBRegressor()

# now we train our model
#by x_train and y_train
# it will find pattern between x_train to corresponding price value in y_train
regressor.fit(x_train , y_train)

#------------ training
# now we use our model for prediction 
# lets predict the value of x_train
#predict of training data 
# it will give predicted value 
# and y_train is original value of x_train
train_predict = regressor.predict(x_train)

# print(train_predict)
'''
[117.58065  61.88913 717.4878  ... 329.96094 142.16927  43.2752 ]
'''

# now we use R squared value for checking the distance between original value and predicted value
# we use func r2_score(orginal_value , predicted_value)
# original value is y_train  corressponding to x_train and train_predict is predicted value of x_train
# range of r2_score 0 to 1
r2_value_train =metrics.r2_score(y_train,train_predict)
print("R square value of training:" ,r2_value_train)

'''
R square value : 0.9999903462710198
'''
#------- now for testing 
test_predict = regressor.predict(x_test)
# so y_test is origional value of x_test   and test_predict is predicted value of x_test

# now we again check the r2 sqaure
r2_value_test =metrics.r2_score(y_test,test_predict)
print("R square value of testing :" ,r2_value_test)















