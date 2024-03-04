class vehicle:
    def __init__(self,name,carNo):
        self.name=name
        self.carNo=carNo
    def display(self):
        print(f'''Name is:{self.name},
Number is:{self.carNo}''')
class Bike(vehicle):
    def __init__(self, name, carNo,color):
        self.color=color
        super().__init__(name, carNo)
    def display(self):
        super().display()
        print(f'Color is {self.color}')
bike=Bike("BIKE",202,"red\n")
bullet=Bike("BULLET",300,"Silvery White\n")
bullet.display()

bike.display()