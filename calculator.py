import math
print("-----------------------------------")
print("|------------CALCULATOR-----------|")
print("-----------------------------------")
def main():
    while True:
        print("Which operation you want to perform?? ")
        print("1. Addition")
        print("2. Subtraction")
        print("3. Multiplication")
        print("4. Division")
        print("5. Trigonometric Functions")
        print("6. Exit")

        choice = input("Enter your choice: ")

        if choice == '6':
            print("Exiting...")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                result = num1 + num2
                print("Result:", result)
            elif choice == '2':
                result = num1 - num2
                print("Result:", result)
            elif choice == '3':
                result = num1 * num2
                print("Result:", result)
            elif choice == '4':
                if num2 == 0:
                    print("Error! Division by zero.")
                else:
                    result = num1 / num2
                    print("Result:", result)
        elif choice == '5':
            angle = float(input("Enter angle in degrees: "))
            radian = math.radians(angle)

            print("1. Sine")
            print("2. Cosine")
            print("3. Tangent")
            print("4. Inverse Sine")
            print("5. Inverse Cosine")
            print("6. Inverse Tangent")

            trig_choice = input("Enter your choice: ")

            if trig_choice == '1':
                result = math.sin(radian)
                print("Result:", result)
            elif trig_choice == '2':
                result = math.cos(radian)
                print("Result:", result)
            elif trig_choice == '3':
                result = math.tan(radian)
                print("Result:", result)
            elif trig_choice == '4':
                result = math.degrees(math.asin(angle))
                print("Result:", result)
            elif trig_choice == '5':
                result = math.degrees(math.acos(angle))
                print("Result:", result)
            elif trig_choice == '6':
                result = math.degrees(math.atan(angle))
                print("Result:", result)
            else:
                print("Invalid choice.")
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
