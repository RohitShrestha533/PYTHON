# class Point():
#     def __init__(self,input1,input2):
#         #place the value in x and y
#         self.x = input1 
#         self.y = input2
# #object
# p=Point(1,10)
# print(p.x)
# print(p.y)

class Flight():
    def __init__(self,capacity):
        self.capacity = capacity
        self.passenger = []

    def add_passenger(self,name):
        if not self.available_seat():
            return False
        self.passenger.append(name)  
        return True

    def available_seat(self):
        return self.capacity - len(self.passenger)      
        
obj = Flight(3);     

people=["ram","hari","sita","rita"]
for p in people:
    success = obj.add_passenger(p)
    if success:
        print(f"Added {p} to flight successfully")
    else:
        print(f"No avaialable seats for {p}")