# this program goes through 2018 csv data on squirrels in Central Park, NY
# and outputs a new csv file with the totals of the colors (gray, red, black)

import pandas

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

# get  hold of each of the rows that contain the color we want
gray_rows = data[data["Primary Fur Color"] == "Gray"]
red_rows = data[data["Primary Fur Color"] == "Cinnamon"]
black_rows = data[data["Primary Fur Color"] == "Black"]

# store the length of the saved colors
gray_count = len(gray_rows)
red_count = len(red_rows)
black_count = len(black_rows)

# create a dictionary with the squirrel data we saved into variables
squirrel_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray_count, red_count, black_count]
}
# call the data frame and pass it the dictionary
data_frame = pandas.DataFrame(squirrel_dict)

# convert data frame to csv type file
data_frame.to_csv("squirrel_count.csv")
