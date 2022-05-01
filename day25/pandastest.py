import pandas

# save object - a excel sheet is a data frame and a column would be a data series
data = pandas.read_csv("weather_data.csv")
print("Now printing the csv data")
print(data)

# if we want to print the data that's in a column - choose temp
print("Now printing the temp column values")
print(data["temp"])

# convert the csv to a dictionary
data_dict = data.to_dict()
print("Now printing the csv file as a dictionary")
print(data_dict)

# turn data series to a list
temp_list = data["temp"].to_list()

print("Now printing the series column of temps in a list")
print(temp_list)

# determine the average of the temperatures
ave_temp = sum(temp_list) / len(temp_list)

print(f"The ave of the temperatures is: {ave_temp}")

# alternatively can use a pandas function to determine
average = data["temp"].mean()
print(f"The ave of the temperatures is: {average}")

# use the pandas functions to get the highest temperature
high_temp = data["temp"].max()
print(f"The highest temperature noted is: {high_temp}")

# filter columns using conditionals to get rows

# get data in a row - used Monday as value to choose from
print(data[data.day == "Monday"])

# get the data in the row that had the highest temperature
print(data[data.temp == data.temp.max()])

# now from the row we can get more specific data such as condition on a specific day
monday = data[data.day == "Monday"]
print(monday.condition)

# convert the temperature in celsius to fahrenheit for Monday
monday_temp = int(monday.temp)

monday_temp_F = monday_temp * 9/5 + 32

print(monday_temp_F)

# create a data frame from scratch
# we have the dictionary below
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [16, 56, 65]
}

# use pandas library and data frame class and pass it the dictionary
data_frame = pandas.DataFrame(data_dict)
print(data_frame)

# convert the data frame made to a csv file - argument is file name and path
data_frame.to_csv("new_data.csv")
