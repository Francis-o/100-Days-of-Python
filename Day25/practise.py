import csv
import pandas

# with open("weather_data.csv") as file_data:
#     weather_data = csv.reader(file_data)
#     temperatures = []
#     for row in weather_data:
#         if row[1] != "temp":
#             temperatures.append(int(row[1]))

# print(temperatures)
# data = pandas.read_csv("weather_data.csv")

# # print row data where temperature is at the maximum
# monday = data[data.day == "Monday"]
# temp_celc = monday.temp[0]
# temp_fah = (temp_celc * 9/5) + 32
# print(temp_fah)

data = pandas.read_csv("2018_Central_Park_Squirrel_Census_-_Squirrel_Data.csv")

squirel_color = data["Primary Fur Color"]

red_squirels = squirel_color[squirel_color == "Cinnamon"]
gray_squirels = squirel_color[squirel_color == "Gray"]
black_squirels = squirel_color[squirel_color == "Black"]

squirel_count = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [len(gray_squirels), len(red_squirels), len(black_squirels)]
}

data  = pandas.DataFrame(squirel_count)
data.to_csv("squirel_count.csv")