"""
===============================================================================
                        PYTHON CODING PRACTICE PROBLEMS
===============================================================================
Author: Ayushka Bhattacharya
Description: A collection of basic Python programming problems for practice
Date: September 2025
===============================================================================
"""

import os
import sys

# ═══════════════════════════════════════════════════════════════════════════
#                           FUNCTION DEFINITIONS
# ═══════════════════════════════════════════════════════════════════════════

def evenorodd():
    """Check if a number is even or odd"""
    num = int(input("Enter a number to check even or odd: "))
    rem = num % 2
    if rem == 0:
        print(f"The {num} is Even")
    else:
        print(f"The {num} is Odd")

def multiplication_table():
    """Generate multiplication table for a given number"""
    try:
        n = int(input("Enter the number for which you want the table:\n"))
        tilln = int(input("Enter the number till which you want the table to be iterated: "))

        if n == 0 or n < 0 or tilln == 0 or tilln < 0:
            print("Invalid Input try again!!")
        else:
            for i in range(1, tilln+1):
                #print("%d * %d = %d" % (n, i, n*i))
                print(f"{n} * {i} = {n * i}")
    except ValueError:
        print("Invalid Input try again!!")

def sum_of_naturals():
    """Calculate sum of first n natural numbers"""
    a = int(input("Enter the number till which u want the sum: "))
    sum = 0
    i = 1
    while i <= a:
        sum = sum + i
        i = i + 1
    print(f"The sum of first {a} natural numbers is {sum}")

def sum_of_squares():
    """Calculate sum of squares of first n natural numbers"""
    n = int(input("Enter the number till which you want the sum of squares:"))
    output = sum([i**2 for i in range(1, n + 1)])
    #output = [i ** 2 for i in range(1, n + 1)] #just get the list of squares
    print(f"The Sum of Squares of all the number till {n} is {output}")

def swap_two_numbers():
    """Swap two numbers using temporary variable"""
    a = int(input("Enter first number:\n"))
    b = int(input("Enter second number:\n"))
    print(f"Before swapping: N1 : {a} N2 : {b}")
    # a = a+b     #without using third variable
    # b = a-b
    # a = a-b
    #a,b = b,a   #without using third variable
    temp = a  #using third variable
    a = b
    b = temp

    print(f"After swapping: N1 : {a} N2 : {b}")


def closest_number():
    """Find number closest to given number and divisible by another number"""
    # Given two integers n and m (m != 0). Find the number closest to n and divisible by m. If there is more than one such number, then output the one having maximum absolute value.
    m = int(input("Enter the number for which you want divisible number: "))
    n = int(input("Enter the target number: "))
    if m == 0:
        print("Invalid Input")
    else:
        lower = (m // n) * n
        higher = lower + n

        lower_dist = abs(m - lower)
        higher_dist = abs(m - higher)

        if lower_dist < higher_dist:
            print(f"The number closest to {m} and divisible by {n} is {lower}")
        elif lower_dist > higher_dist:
            print(f"The number closest to {m} and divisible by {n} is {higher}")
        else:
            print(f"The number closest to {m} and divisible by {n} is {higher}")

def dice_problem():
    """Find the opposite number on a dice"""
    #A number is given guess the opposite number in the dice
    n = int(input("Enter the number on the dice: "))
    if n < 1 or n > 6:
        print("Invalid Input")
    else:
        opposite = 7 - n
        print(f"The opposite number of {n} on the dice is {opposite}")

def nth_term_ap():
    """Calculate nth term of an Arithmetic Progression"""
    a = int(input("Enter the first term of the AP series:"))
    b = int(input("Enter the second term of the AP series:"))
    n = int(input("Enter the desired term position of the AP series:"))
    result = a + (n-1)*(b-a)
    print(f"The {n}th number is {result}")

# ═══════════════════════════════════════════════════════════════════════════
#                           CONFIGURATION & MENU
# ═══════════════════════════════════════════════════════════════════════════

# Problem menu dictionary
Problems = {
    1: "Check Even or Odd",
    2: "Multiplication Table",
    3: "Sum of Naturals",
    4: "Sum of Squares of Naturals",
    5: "Swap Two Numbers",
    6: "Closest Number",
    7: "Dice Problem",
    8: "Nth Term of AP"
}

# Function mapping dictionary
problem_functions = {
    1: evenorodd,
    2: multiplication_table,
    3: sum_of_naturals,
    4: sum_of_squares,
    5: swap_two_numbers,
    6: closest_number,
    7: dice_problem,
    8: nth_term_ap
}

# ═══════════════════════════════════════════════════════════════════════════
#                               MAIN PROGRAM
# ════════════════════════���══════════════════════════════════════════════════

def display_header():
    """Display program header with styling"""
    print("=" * 80)
    print("🐍 PRACTICING EASY CODES IN PYTHON 🐍".center(80))
    print("=" * 80)
    print()

def display_menu():
    """Display the menu options in a formatted way"""
    print("📋 Available Problems to Solve:")
    print("─" * 40)
    for key, value in Problems.items():
        print(f"   {key}. {value}")
    print("─" * 40)

def main():
    """Main program execution"""
    # Clear screen (works on both Windows and Unix)
    os.system('cls' if os.name == 'nt' else 'clear')

    # Display header
    display_header()

    # Display menu
    display_menu()

    # Get user input and execute
    try:
        choice = int(input("\n🔢 Enter your choice (1-8): "))

        if choice < 1 or choice > 8:
            print("❌ Invalid choice! Please enter a number between 1 and 8.")
            return

        print(f"\n✅ You selected: {Problems[choice]}")
        print("─" * 50)

        # Execute the corresponding function
        if choice in problem_functions:
            problem_functions[choice]()
        else:
            print("⚠️  Functionality for this option is not yet implemented.")

        print("\n" + "─" * 50)
        print("✨ Program completed successfully!")

    except ValueError:
        print("❌ Invalid input! Please enter a numeric value between 1 and 8.")
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted by user. Goodbye!")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# ═══════════════════════════════════════════════════════════════════════════
#                            PROGRAM ENTRY POINT
# ═══════════════════════════════════════════════════════════════════════════

if __name__ == "__main__":
    main()
