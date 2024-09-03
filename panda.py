#Pandas is a Python library used for working with data sets.
#It has functions for analyzing, cleaning, exploring, and manipulating data.
import pandas as pd
# fisrt 
dataset = {
  'cars': ["BMW", "Volvo", "Ford"],
  'passings': [3, 7, 2]
}

file=pd.DataFrame(dataset)
print(file)

#using location row 
print(file.loc[0])
data = {
  "Duration":{
    "0":60,
    "1":60,
    "2":60,
    "3":45,
    "4":45,
    "5":60
  },
  "Pulse":{
    "0":110,
    "1":117,
    "2":103,
    "3":109,
    "4":117,
    "5":102
  },
  "Maxpulse":{
    "0":130,
    "1":145,
    "2":135,
    "3":175,
    "4":148,
    "5":127
  },
  "Calories":{
    "0":409,
    "1":479,
    "2":340,
    "3":282,
    "4":406,
    "5":300
  }
}

df = pd.DataFrame(data)

print(df) 
# dispaly series 
a=[12,33,44,"mariyam","ayesha"]
print(pd.Series(a))
std={1401:"mariyam",1402:"ayesha",1403:"hammad",1404:"uzma"}
print(pd.Series(std))
f=pd.Series(std)



# series also provide according to choice  index
a=[12,33,44,"mariyam","ayesha"]
print(pd.Series(a,index=[10,11,12,13,14]))

# using csv file
#A simple way to store big data sets is to use CSV files (comma separated files).
f=pd.read_csv('C:\\Users\\Swan Computers\\Documents\\data.csv')
print(f.to_string())#use to_string() to print the entire DataFrame.
# without to string ()its print first 5 and last 5 rows 
print(pd.options.display.max_rows)


#  json 
#Big data sets are often stored, or extracted as JSON.
#JSON is plain text, but has the format of an object, 


#pandas analysis data 
f=pd.read_csv('C:\\Users\\Swan Computers\\Documents\\data.csv')
print(f.head(10))# first 10 rows 
print(f.head())# first 5 rows
print(f.tail())#last 5 rows
print(f.info())# information



# cleaning data 



#Remove Rows
f=pd.read_csv('C:\\Users\\Swan Computers\\Documents\\data.csv')
new_df = f.dropna()
print(new_df.to_string())# remove empty cells  and will not change the original dataframes 
# if you want ro change orignal frames
f.dropna(inplace = True)
#  it will remove all rows containing NULL values
print(f.to_string())



#Replace Empty Values
#The fillna() method allows us to replace empty cells with a value:



