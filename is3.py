n=int(input("enter a number: "))
x=0
y=0
for i in range(1,n+1):
    x+=i**2
    y+=i
sumofsquares=x
squareofsum=y**2
print("difference = ",squareofsum-sumofsquares)