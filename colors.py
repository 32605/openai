colors = []  # create an empty list of colors

while len(colors) < 5:  # while the length of the list is less than 5
    color = input("Enter a color: ")  # ask the user to enter a color
    colors.append(color)  # append the color to the list

for color in colors:  # for each color in the list
    print(color)  # print the color
