'''
1. input user's name then print it out
2. input user's age then print it out
'''
adult_age = 21

#ask_name = "What is your name"
client_name = "What is your name"
#name = input(ask_name + " ? ")
name = input(client_name + " ? ")
print(f"Hi {name}!")

ask_age = "How old are you"
age = input(f"{ask_age} {name}? ")
if int(age) > adult_age:
    print("Happy year " + age + "!")
else:
    print("Good year " + age + "!")
