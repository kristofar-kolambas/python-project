for i in range(3):
    Subject = str(input("Enter Subject Name:"))
    Mark = int(input("Enter Mark:"))

    if Mark >= 90:
        print("Grade:A")
    elif Mark >=70:
        print("Grade:B")
    elif Mark >=60:
        print("Grade:C")
    elif Mark >=50:
        print("Grade:D")
    else:
        print("Grade:E")
        