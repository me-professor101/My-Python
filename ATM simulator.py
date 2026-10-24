while True:
  balance= 100000
  pin=1234
  user_pin= int(input("Enter your pin")) # pyton variable name me space nhi hoga space ke liye under score se set kiya
  if user_pin ==1234:
    print("======ATM======")
    print("1, Check balance")
    print("2,withdrawl money enter")
    print("3 depositable amount")
    print("4 Exit")

    choice= int(input("enter valid no.")) # input string deta hai hame integer ko recpgnise krwana hai 

    if choice== 1:
     print("balance",balance)

    elif choice==2:
     withdrawl=int(input("enter your withdrawl money")) # yhaa print ka use nhi kiye kyuki vo keval hame message flass krata but withdrawl krwana hai amount ko var me save krna hai

    if withdrawl > balance:
      print("invalid ammount")
    else:
      balance= balance- withdrawl
      print("withdrwl succesfull")
      print("remaining balance", balance)

  elif choice==3:
     print("enter depositable amount")

  else :
    print( "exist")
