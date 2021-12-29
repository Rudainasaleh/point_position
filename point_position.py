
# Description: in this program we need first to insert an input for the user to enter the 3 point coordinates
# The input will ask the user to enter x0, y0, x1, y1, x2, y2
# Then im going to add an if and elif statement that if:
# first: (x1 –y0)  ́(y2 –y0) –(x2 –x0) ́(y1 –y0) > 0 then p2 is on the left side of the line
# second: (x1–y0)  ́(y2 –y0) –(x2 –x0) ́(y1 –y0) < 0 then p2 is on the right side of the line
# Finally: otherwise p2 is on the same line
# And finally from the if statement the program is going to print the right statement with the pints


# write an input for the user to enter x0, y0, x1, y1, x2, y2
x_0 = float(input("Enter the x-coordinate for point p0:"))
y_0 = float(input("Enter the y-coordinate for point p0:"))
x_1 = float(input("Enter the x-coordinate for point p1:"))
y_1 = float(input("Enter the y-coordinate for point p1:"))
x_2 = float(input("Enter the x-coordinate for point p2:"))
y_2 = float(input("Enter the y-coordinate for point p2:"))


# write an if statement to determines where p2 is relative to the line
# print the relationship between p2 and the line
if (x_1 - y_0) * (y_2 - y_0) - (x_2 - x_0) * (y_1 - y_0) > 0:
    print("p2 at coordinates (", x_2, ",", y_2, ") is on the left side of the line")
    print("from point (", x_0, ",", y_0, ") to point (", x_1, ",", y_1, ")")
elif (x_1 - y_0) * (y_2 - y_0) - (x_2 - x_0) * (y_1 - y_0) < 0:
    print("p2 at coordinates (", x_2, ",", y_2, ") is on the right side of the line")
    print("from point (", x_0, ",", y_0, ") to point (", x_1, ",", y_1, ")")
else:
    print("p2 at coordinates (", x_2, ",", y_2, ") is on the line")
    print("from point (", x_0, ",", y_0, ") to point (", x_1, ",", y_1, ")")





