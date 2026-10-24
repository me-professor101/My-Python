while True:
#snake water gun game
 import random  # taki computer koi random module use krr sake mens random no. isse random module fn kehta hai
 '''


 1 for snake 
 -1 for water
 0 for gun
 '''
 computer= random.choice([-1, 0, 1])  # taki computer ek random choice krr sake
 youstr = input("Enter your choice: ")
 youdict= {"snake":1,"water":-1,"gun":0} #dictunory operator ka use hamne ek dict bnai kyy kisse dena hai
 
 you = youdict[youstr] #dictonary me youstr dalo jo user ne input kiya hai usko you me asign krr do 
 
 youreverse= {1:"snake",-1:"water",0:"gun"} #reverse dictunory operator ka use kiya hai taki computer ka choice print krr sake kyuki random user me computr no lega uss no. ko ulta s w ya g me convert krr de jabki dict me s g w ko no. me convert kiya tabhi to vompare hoga 
 
 print(f"you choose {youstr} and computer choose {youreverse[computer]}") #f string ka use kiya hai taki user aur computer ka choice print krr sake

 #by now we have two no variable you and computer
 if(computer==you):#ladder if else ka use kiya hai
   print("draw")
 else:
    if(computer==1 and you==-1):
       print("computer wins")
    elif(computer==1 and you ==0):
        print("you wins")
    elif(computer==-1 and you==0):
        print("computer wins")
    elif(computer==-1 and you==1):
        print("you wins")    
    elif(computer==0 and you==1):
        print("computer wins")
    elif(computer==0 and you==-1):
        print ("you wins")    
    else:
        print("you have a wrong choice")        




        '''doubt Agr computer ne randomly no. Liya to use you reverse snake water ya gun me se kuch bna dega but hamne choice snake ki di to usse you dict bhi to no. Bna dega to compare kaise hoga ek no.
        Professor bhai! 🔥 Ab tumne ekdum sahi doubt pakda hai. Tumhara question hai ki comparison ke time ek taraf number hoga aur doosri taraf `snake`, `water` ya `gun` — toh compare kaise hoga?

Lekin tumhare code mein aisa nahi ho raha. Chalo step-by-step samajhte hain.

### 1\. Tumhari dono dictionaries ka kaam

```python
youdict = {"snake": 1, "water": -1, "gun": 0}

youreverse = {1: "snake", -1: "water", 0: "gun"}
```

* `youdict` user ki choice ko number mein badalta hai.

* `youreverse` computer ke number ko naam mein badalta hai.

### 2\. Maan lo tumne `snake` choose kiya

Tumhare code mein ye lines chalengi:

```python
youstr = input("Enter your choice: ")
you = youdict[youstr]
```

Ab values hongi:

| Variable | Value   |
| -------- | ------- |
| youstr   | "snake" |
| you      | 1       |

Computer randomly `-1` choose karta hai:

```python
computer = random.choice([-1, 0, 1])
```

Ab `computer = -1` hai.

### 3\. Ab comparison kaise hoga?

Tumhari print statement mein:

```python
print(f"You choose {youstr} and computer choose {youreverse[computer]}")
```

Ismein `youreverse[computer]` sirf naam print karne ke liye hai. Comparison ke liye nahi!

Actual comparison hota hai:

```python
if computer == you:
```

Yaani:

```python
if -1 == 1:
```

Ye `False` hoga, kyunki dono numbers alag hain.

### Poora flow yaad rakho

Tum input dete ho: `"snake"`

`youdict["snake"]` → 1

Computer randomly -1 leta hai

`computer == you` → `-1 == 1` → False

Alag se `youreverse[-1]` computer ki choice ko `"water"` banata hai, taaki output mein naam dikha sake.

Sabse important baat, bhai: `you` aur `computer` dono numbers hain. `youstr` aur `youreverse[computer]` sirf naam hain, jinhe print karne ke liye use kiya ja raha hai.

Isi wajah se tumhara `if-elif` logic numbers compare kar sakta hai. 💻'''