correctPassword = "AdminPote@1605"
passwordList = [
    "hello@123",
    "AdminPote@123",
    "Admin123",
    "JayHoo@1605",
    "AdminPote1605"
]

for PassWord in passwordList:
    if PassWord == correctPassword:
        print("Access Granted..!!")
        print("Correct Password: ", PassWord)
    else:
        print("Try Other Passwords..!!")