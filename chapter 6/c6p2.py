marks1 = int(input("inter marks subject 1 :"))
marks2 = int(input("inter marks subject 2 : "))
marks3 = int(input("inter marks subject 3 : "))

#checking for total percent

total_percentage= (100*( marks1 + marks2 + marks3))/300

if(total_percentage >= 40) and marks1>33 and marks2>33 and marks3>33:
    print("passed", total_percentage) 

else: 
    print("fail hogyi babuni", total_percentage)
