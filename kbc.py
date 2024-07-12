def greet(name):
    print("Welcome to KBC",name)


def instruction():
    print("********* Rules to  Follow(Instructions)*************")
    print("""1.choose one from given optiom only
        2.There will be 7 Questions 
        3.To Stay in game provide give correct answer
        4.if want to quit the game pls enter zero\n\n""")


def questions():
    amount=0
    Questions=[["capital of UP","Shilong","Banaras","Lucknow","Gaya",3],
              ["who won 2024 T20 workd cup?","India","Afgnaistan","Autralia","South Africa",1],
              ["capital of Bihar","Shilong","Banaras","Lucknow","Patna",4],
              ["capital of Odisha","Shilong","Banaras","Bhubneswar","Gaya",3],
              ["capital of Goa","Pondicherry","Banaras","Lucknow","Gaya",1],
              ["capital of Jharkhand","Shilong","Banaras","Lucknow","Ranchi",4],
              ["capital of Andhra Pradesh","Shilong","Banaras","Amarvati","Gaya",3],
              ]
    level=[1000,2000,5000,10000,25000,50000,100000]

    
    for i in range(0,len(Questions)):
        Question=Questions[i]
        print(f"Question for Rs:${level[i]} is -->> {Question[0]}::\n")
        print(f"1.{Question[1]}               2.{Question[2]}")
        print(f"3.{Question[3]}               4.{Question[4]}")

        answer=int(input("\nEnter the correct option :: "))
        if(answer==Question[-1]):
            amount=level[i]
            print("\nCorrect answer")
        elif(answer==0):
            print("You successfully quit the game")
            break
            
        else:
            print("Sorry it's incorrect ..... You Lose")
            break
            
    print(f"You have successfuly win amount of Rs:: ${amount}")







print("****************Welcome to KBC ****************")
name=input("Enter your name:: ")
greet(name)
instruction()

print("--->>",name,"Are u ready !!!!!!!!!!!\n")
print("So,let's Start")


questions()
