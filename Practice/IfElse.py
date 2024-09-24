marks=int(input("Enter the marks of student: "))

if(marks>=90):
    grade="A"
elif(marks>=80 and marks<90):
    grade="B"
elif(marks>=70 and marks<80):
    grade="C"
else:
    grade="D"
print("grade of the student:",grade)

# output
# Enter the marks of student: 78
# grade of the student: C
---------------------------
# age=int(input())
# if(age>=18):
#     print("Can vote")
# else:
#     print("Cannot vote")
