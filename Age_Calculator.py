byear=int(input("Enter Your Birth Year: "))
year=int(input("Enter the Current Year: "))
age=year-byear

if age>0 and age<=12:
    print(f"You are {age} years old,which means you're a child")
elif age>=13 and age<=19:
    print(f"You are {age} years old,you are in your Teens!!!")
elif age>=20 and age<=59:
    print(f"You are {age} years old, You are An Adult now buddy!")
elif age>60:
    print(f"You are {age} years old, Though a Senior Citizen still young at heart!!")
else:
    print("Invaid Year entered")