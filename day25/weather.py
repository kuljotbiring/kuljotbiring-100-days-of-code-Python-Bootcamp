import csv


# bad method of turning each line in csv file as a list element
# with open("weather_data.csv") as file:
#     data = file.readlines()
#
#     print(data)

# use the csv library which creates an object
with open("weather_data.csv") as data_file:
    data = csv.reader(data_file)
    # create empty list to store temperatures
    temperatures = []
    # now loop through the csv object
    for row in data:
        if row[1] != "temp":
            temperatures.append(int(row[1]))

print(temperatures)
