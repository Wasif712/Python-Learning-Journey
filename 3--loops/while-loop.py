# While Loop

# initialization
# while condition:
    # code to be executed
    # update the condition

x = 1
while x <=5:
    print(x)
    x +=1

y=1
while y <= 10:
    print(y)
    y+=1
    if y == 8:
        break

for i in range(5):
    if i == 2:
       continue
    print(i)