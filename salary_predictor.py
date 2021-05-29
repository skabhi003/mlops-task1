
import joblib
model = joblib.load('salary.pk1')

while True:
    exp = float(input("Enter Years of Experience : "))
    result = model.predict([[exp]])
    salary = round(*result, 2)
    print("Estimated Salary : ₹ {0} \n".format(salary))
    choice = input("Do you want to continue [y/N]: ")
    if (choice == "N" or choice == "n"):
        break
    elif(choice == "Y" or choice == "y"):
        print()
    else:
        break




