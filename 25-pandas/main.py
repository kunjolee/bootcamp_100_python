# Data frame is the table from a sheet
# Series is a column from a sheet

import pandas
data = pandas.read_csv("./weather_data.csv")
temp = data['temp']

# Dataframe to dictionary
data_dic = data.to_dict()
print(data_dic)

# Series to list
temp_list = temp.to_list()
temp_average = temp.mean()
print(temp_average)

# Series max of a column
temp_max = temp.max()
print(temp_max)

print('\n')

# Get data in columns

print(data['condition'])
print(data.condition)

print('\n')

# Get data in rows --

# Max temperature
print(data [ data.temp == data.temp.max() ])
# get monday data

monday = data[ data.day == "Monday" ]
monday_temp = int(monday.temp)
monday_temp_f = monday_temp * 9/5 + 32

print("Monday temperature in fahrenheit ",monday_temp_f)
print('\n')


# Create a data frame from scratch

students = {
    "students": ["amy", "james", "angela"],
    "scores": [76,56,65]
}

data_students = pandas.DataFrame(students)

data_students.to_csv("new_data.csv")
