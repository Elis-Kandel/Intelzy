class Car:
    def __init__(self,name,model,color):
        self.name=name
        self.model=model
        self.color=color
    def display(self):
        print(self.name)
class Bike(Car):
    def __init__(self, name, model, color,engineNo):
        self.engineNo=engineNo
        super().__init__(name, model, color)
    def display(self):
        print(self.engineNo)
        super().display()
class Modification(Bike):
    def __init__(self,name,model,color,engineNo,modification):
        self.modification=modification
        super().__init__(name,model,color,engineNo)   
    def display(self):
        print(self.modification)
        super().display()   
car1=Car("BMW",'X5','RED')
bike=Bike("Rabin ko bullet",'laudu','setoseto','2')
bike.display()
