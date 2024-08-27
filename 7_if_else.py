"""Simple code explaining if, elif, else """


user = input("Enter your name: ").capitalize()

if user == "Himanshu":
    print(f"Welcome back {user} Sir.")

elif user == "Kshitija":
    print(f"Welcome back {user} Mam.")
else:
    print(f"Alert!!... Security Breach by user:{user}")