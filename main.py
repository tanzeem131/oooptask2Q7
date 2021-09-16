class student:
    def __init__(self, name, age, roll_no):
        self.name = name
        self.age = age
        self.roll_no = roll_no

    def displayDetails(self):
        print("name:", self.name, "age:", self.age, "roll_no:", self.roll_no)

st_1 = student('Rahul', 21, 33)
st_2 = student('Rohit', 22, 40)
A = st_1.age
B = st_2.age

st_1.displayDetails()
st_2.displayDetails()

print(A==B)