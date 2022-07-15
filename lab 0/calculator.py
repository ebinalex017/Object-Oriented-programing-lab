class calc():
    def __init__(self,a,b):
        self.a = a
        self.b = b
        
    def add(self):
        return self.a + self.b
    def sub(self):
        if self.a > b:
            return self.a + self.b
        else:
            return self.b + self.a    
    def mul(self):
        return self.a * self.b
    def div(self):
        return self.a / self.b
    def rem(self):
        return self.a % self.b

while True:
    ext = input("Do you want to exit? ")
    if ext == 'yes':
        break
    elif ext == 'no':
        pass
    a = int(input("Enter first number"))
    b = int(input("Enter Second number"))
    obj=calc(a,b)
    def menu():
        x = ('1. Add \n2. Sub \n3. Multiply \n4. Divide\n5.Reminder') 
        print(x)
    menu()
    choice = int(input('Please select one of the following : '))
    if choice == 1:
        print("Result: ",obj.add())
    elif choice == 2:
        print("Result: ",obj.sub())
    elif choice == 3:
        print("Result: ",obj.mul())    
    elif choice == 4:
        print("Result: ",obj.div())
    elif choice == 5:
        print("Result: ",obj.rem())
    else:
        print("invalid input")
print()