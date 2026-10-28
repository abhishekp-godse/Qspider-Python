def welcome(name):
    print(f"Welcome, {name}!")

name = input("Enter your name\n")
welcome(name)
choice = input("Are you ready to play? (yes/no)\n")
if choice=="n":
    print("thank you for playing\n")
elif choice=="y":
    print("thank you for joining the game \n LETS STARTS!!!")