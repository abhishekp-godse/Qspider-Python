def welcome(name):
    print(f"Welcome to KBC, {name}!")

def question_bank():
    price=0

    #question 1
    q1="1)largest river in the world?\na)neil river\tb)amazon river\t\nc)ganga river\td)yamuna river"
    ans1 = "amazon river"
    price=ask_question(q1,ans1,price)
    if price==-1:
        return print("you failed\n") 
    else:
        print(f"you have won {price}")


    #question 2
    q2="2)largest economic city in the india?\na)delhi\tb)mumbai\t\nc)kolkata\td)chennai"
    ans2 = "mumbai"
    price=ask_question(q2,ans2,price)
    if price==-1:
        return print("you failed\n") 
    else:
        print(f"you have won {price}")

    #question 3
    q3="3)highest gdp  state in the india?\na)rajasthan\tb)maharashtra\t\nc)Gujrat\td)kerala"
    ans3 = "maharashtra"
    price=ask_question(q3,ans3,price)
    if price==-1:
        return print("you failed\n") 
    else:
        print(f"you have won {price}")

    #question 4
    q4="4)Richest person in the india?\na)gautam adani\tb)mukesh ambani\t\nc)sundar pichai\td)Amit shah"
    ans4 = "mukesh ambani"
    price=ask_question(q4,ans4,price)
    if price==-1:
        return print("you failed\n") 
    else:
        print(f"you have won {price}")

    #question 5
    q5="5)who invented zero?\na)arya bhat\tb)ramanujan\tc)albert einstein\td)isaac newton"
    ans5 = "arya bhat"
    price=ask_question(q5,ans5,price)
    if price==-1:
        return print("you failed\n") 
    else:
        print(f"you have won {price}")

    #question 6
    q6="6)who is the founder pf Qspider?\na)saarang sir\tb)sandeep sir\tc)mayuresh sir\td)sachin sir"
    ans6 = "sandeep sir"
    price=ask_question(q6,ans6,price)
    if price==-1:
        return print("you failed\n") 
    else:
        print(f"you have won {price}")

    #question 7
    q7="7)inflation rate in india?\na)6.00\tb)5.59\tc)5.72\td)7.12"
    ans7 = "5.72"
    price=ask_question(q7,ans7,price)
    if price==-1:
        return print("you failed\n") 
    else:
        print(f"you have won {price}")

        print("\nCONGRAGULATIONS\nyou have won the KBC\n")
        return print("\n\tSATH CARORE\n")

def ask_question(ques,answer,current_price):
    print(f"Question: {ques}")
    user_ans=input("enter your answer ")
    print(user_ans)
    if user_ans == answer:
        current_price  +=1000000
        return current_price
    else:
        return -1
    
name = input("Enter your name\n")
welcome(name)
choice = input("Are you ready to play? (y/n)\n")
if choice=="n":
    print("thank you for playing\n")
elif choice=="y":
    print("thank you for joining the game \n LETS STARTS!!!")
    question_bank()