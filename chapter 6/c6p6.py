marks= int(input("enter your marks: "))

if(marks<=100 and marks>=90):
    grade= "Ex"




elif(marks<90 and marks>=80):
    grade = "B"
elif(marks<80 and marks>=70):
    grade = "C"

elif(marks<70 and marks>=60):
      grade = "D"

elif(marks<60 and marks>=50):
        grade = "E"

else:
        grade = "F"

print("your grade is:", grade) # yha maine glti ki thi ki grade 50 ke nice define hi nhi kiya tha so programm me geade name error
# aya tha tb else function lga kr use kiya grade define kiya ye bhi dekh lo kaise last me ek print se kaam chal gya 
