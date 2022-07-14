x = []

for i in range(10):
    i = int(input("Enter numbers to list: "))
    x.append(i)

   
i = int(input("from "))
j = int(input("to "))
s=0
while i<j:
    temp = x[i]
    s = s + temp
    i= i+1
    
print(s)