marks = [85, 93, 73, 67, 41]  # yeh ek list hai jo 5 marks ko store karta hai same data type ke.
print(marks[0])  # python m index 0 sy start hoti hai. Positive index 0,1,2,3,4 hoti hai. 
print(marks[-1])  # -1 index last element ko show karta hai. Negative index -1,-2,-3,-4,-5 hoti hai. 
marks[-1] = 100  # yeh last element ko update karta hai.
print(marks[-1])  # yeh last element ko update kiya gaya hai.

print(marks)  # yeh list ko print karta hai.

marks.append(200)  # yeh list me new element ko add karta hai end me.
marks.insert(2, 150)  # yeh list me new element ko add karta hai specific index me.list.insert(index, value)
marks.remove(67)  # yeh list me se specific element ko remove karta hai.
marks.pop()  # yeh list me se last element ko remove karta hai.
marks.pop(1)  # yeh list me se specific index ka element ko remove karta hai.
print(len(marks))  # yeh list ko print karta hai.

# for i in marks:  # yeh loop pory list ko iterate karta hai aur har element ko print karta hai.
#     print(i)


student = ["Wasif", 19, 3.05, True]  # python list me different data types ko store kar sakte hai.
# for i in student:
#     print(i)


number = [80, 75, 90, 65, 88, 72]
print(max(number))  # yeh list me se maximum value ko print karta hai.
print(min(number))  # yeh list me se minimum value ko print karta hai.
print(sum(number))  # yeh list me se sum of all elements ko print karta hai.
print(sum(number)/len(number), "%")  # yeh list me se average of all elements ko print karta hai.

# List slicing:
# list[start:stop]
print(number[1:4])  # yeh list me se specific range of elements ko print karta hai. index 1 sy 4 tak print karega but 4 ko include nahi karega.
print(number[:3])  # yeh list me se specific range of elements ko print karta hai. starting index 0 sy 3 tak print karega but 3 ko include nahi karega.
print(number[2:])  # yeh list me se specific range of elements ko print karta hai. index 2 sy end tak print karega.
print(number[::2])  # yeh list me even indexed elements ko print karta hai.
print(number[::-1])  # yeh list me right to left print karta hai. index 4 sy 0 tak print karega.
print(number[-3:-1])  # yeh list me se specific range of elements ko print karta hai. index -3 sy -1 tak print karega but -1 ko include nahi karega.
print(number[-1:-3])  # yeh list me se specific range of elements ko print karta hai. index -1 sy -3 tak print karega but -3 ko include nahi karega.
print(number[-3:])  # yeh list me se specific range of elements ko print karta hai. index -3 sy end tak print karega.
print(number[:-3])  # yeh list me se specific range of elements ko print karta hai. index 0 sy -3 tak print karega but -3 ko include nahi karega.
print("------------------------------------------------")
# Slicing with Step
# [start : stop : step]

counting = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
print(counting[0:8:2])  # yeh list me se specific range of elements ko print karta hai. index 0 sy 8 tak print karega but 8 ko include nahi karega. step 2 ka matlab hai ki har dusre element ko print karega.
print(counting[1:9:3])  # yeh list me se specific range of elements ko print karta hai. index 1 sy 9 tak print karega but 9 ko include nahi karega. step 3 ka matlab hai ki har teesre element ko print karega.
print(counting[::4])  # yeh list me se specific range of elements ko print karta hai. starting index 0 sy end tak print karega. step 4 ka matlab hai ki har chauthe element ko print karega.
print(counting[::-3])  # yeh list me se specific range of elements ko print karta hai. starting index end tak print karega. step -3 ka matlab hai ki har teesre element ko print karega right to left.
print(counting[-1:-9:-2])  # yeh list me se specific range of elements ko print karta hai. starting index -1 sy -9 tak print karega but -9 ko include nahi karega. step -2 ka matlab hai ki har dusre element ko print karega right to left.
print(counting[-2:-10:-3])  # yeh list me se specific range of elements ko print karta hai. starting index -2 sy -10 tak print karega but -10 ko include nahi karega. step -3 ka matlab hai ki har teesre element ko print karega right to left.
print(counting[-3::-4])  # yeh list me se specific range of elements ko print karta hai. starting index -3 sy start karega aur end tak print karega. step -4 ka matlab hai ki har chauthe element ko print karega right to left.
print(counting[-4:-10:-5])  # yeh list me se specific range of elements ko print karta hai. starting index -4 sy -10 tak print karega but -10 ko include nahi karega. step -5 ka matlab hai ki har paanchve element ko print karega right to left.

# List + Conditional Statements:
num = [80, 45, 90, 30, 65]
for mark in num:
    if mark >= 50:
        print(mark, "Pass")
    else:
        print(mark, "Fail")