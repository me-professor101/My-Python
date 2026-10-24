marks=[]
f1 = int(input("Enter the first mark: "))
marks.append(f1)
f2 = int(input("Enter the second mark: ")) 
marks.append(f2)
f3 = int(input("Enter the third mark: "))
marks.append(f3)
f4 = int(input("Enter the fourth mark: "))
marks.append(f4)
f5 = int(input("Enter the fifth mark: "))
marks.append(f5)
f6 = int(input("Enter the sixth mark: "))
marks.append(f6)

#sort function is used to sort the list in ascending order but ye yha kaam nhi karega bcz input stringformat me hai int lgakeintegerbna
marks.sort()
print(marks)