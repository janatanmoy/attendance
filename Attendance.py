attend_class=int(input("Enter Your Attend Class: "))
if attend_class<0:
    print("Your Attend Class Cannot be less than zero")
    exit()
total_class=int(input("Enter Your Total Class: "))
if total_class<0:
    print("Your Total Class Cannot be zero./nPlease Provide a Valid Details")
elif total_class<attend_class:
    print("The number of classes you attend is more than your total number of classes./nPlease Provide a Valid Details")
elif total_class==0:
    print("Your Total Class Cannot be Zero./nPlease Provide a Valid Details")
else:
    percentage_of_attandance=(attend_class/total_class)*100
    if percentage_of_attandance<75:
        print(f"You Are Not Eligible For Exam.Your Attandance is:{percentage_of_attandance:.2f}%")
    else:
        print(f"You Are Eligible For Exam.Your Attandance is:{percentage_of_attandance:.2f}%")