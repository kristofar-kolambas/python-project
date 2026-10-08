studentName = "Pradipsinh"
password = 123

for i in range(3):
    name=str(input("enter name:"))
    pw=int(input("enter password:"))

    if(name==studentName and pw == password):
        print("Welcome..!")
        break
    else:
        print("invalid username or password..")

else:
    print("Your Limit Is Over..")