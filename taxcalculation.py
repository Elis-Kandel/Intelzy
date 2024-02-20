'''
Write a program to accept the cost price of a bike and display the road
tax to be paid according to the following criteria
'''

bike_price=int(input("Enter price of bike"))

if bike_price>100000:
    tax=bike_price*0.15
elif bike_price>50000 or bike_price<=100000:
    tax=bike_price*0.1
elif bike_price<=50000:
    tax=bike_price*0.5
else:
    tax=0
print(f"tax is {tax}")