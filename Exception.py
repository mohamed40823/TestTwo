try:
    num1 = int(input("Enter a number: "))
    num2 = int(input("Enter another number: "))
    result = num1 / num2
    print(f"The result is: {result}")
except ZeroDivisionError:
    print("Error: You can't divide by zero!")
except ValueError:
    print("Error: Please enter a valid number.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
finally:
    print("This block always runs, no matter what.")
