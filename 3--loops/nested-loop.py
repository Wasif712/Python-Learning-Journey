# python m first element include hota hai or last exlude hota hai.

# pehly waly loop k first element sy second loop k sary element print hongy.
for i in range(3):     # 0, 1, 2  = 3 
    for j in range(2): # 0, 1     = 2
        print(i, j)    # 3 x 2    = 6 

# yaha par bhi pehly waly array k first element sy second wala pora array print hoga then first array k second element sy second array pora print oga or aisy he sary hongy print
students = ["Wasif", "Ali", "Ahmed"]   # total = 3
subjects = ["Math", "Python", "Data Science"]  # total = 3       means 3 x 3 = 9 print hongy
for student in students:   # phelly array k first element ko select karo
    for subject in subjects:  # then second array k sary element us k sath print kardo
        print(student, "-", subject)

dataset = [[80, 75, 90],    # thela 1
           [65, 70, 85],    # thela 2
           [90, 95, 88] ]   # thela 3
for student in dataset:   # pehla thela uthao [80, 75, 90]
    for mark in student:  # us thely me se ek ek number nikalo
        if mark < 0 or mark > 100:  # har number ko compare karo
            print("Invalid mark:", mark)

for student in dataset:     # pehla thela uthao
    total = 0               # har thely k leyeh total 0 hai
    for mark in student:    # us thely m sy aik aik number nikalo eg : [80, 75, 90]
        total += mark       # har number ko add karty raho jis thelo ko lia hai us k eg : 80 + 75 + 90
    print("Total:", total)  # ab us thely k numbers k total ko print kardo eg : 245
    average = total / len(student)  #  ab us thely k average find kary gy
    print("Average:", average,"%")   # ab us thely k average ko print kardo eg : 81.66%