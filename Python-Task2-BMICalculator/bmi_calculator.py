
print("BMI CALCULATOR")

while True:
    try:
        weight = float(input("\nEnter your weight in kg: "))
        height = float(input("Enter your height in meters: "))

        if weight <= 0:
            print("Weight must be greater than zero.")

        elif height < 0.5 or height > 2.7:
            print("Please enter a valid height between 0.5 and 2.7 meters.")

        else:
            bmi = weight / (height ** 2)

            print("\nYour BMI is:", round(bmi, 2))

            if bmi < 18.5:
                print("Category: Underweight")
            elif bmi < 25:
                print("Category: Normal weight")
            elif bmi < 30:
                print("Category: Overweight")
            else:
                print("Category: Obese")

    except ValueError:
        print("Invalid input. Please enter numbers only.")

    again = input("\nDo you want to calculate again? (yes/no): ")

    if again.strip().lower() != "yes":
        print("Thank you for using the BMI Calculator!")
        break
