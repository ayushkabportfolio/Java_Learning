"""
===============================================================================
                        PYTHON CODING PRACTICE PROBLEMS - DAY 2
===============================================================================
Author: Ayushka Bhattacharya
Description: A collection of Python programming problems for practice - Day 2
Date: September 2025
===============================================================================
"""

import os
import sys

# ═══════════════════════════════════════════════════════════════════════════
#                           FUNCTION DEFINITIONS
# ═══════════════════════════════════════════════════════════════════════════

def swap_first_last_element():
    """Swap first and last element of a list"""
    lst = input("Enter space-seperated digits for the list:").split()

    print(f"List: {lst}")
    lst[0], lst[-1] = lst[-1], lst[0]
    print(f"List after altering: {lst}")
def swap_two_numbers():
    """Swap 2 numbers"""
    a = int(input("Enter number 1: "))
    b = int(input("Enter number 2: "))
    print(f"Before Swapping number 1: {a} number 2: {b} ")
    a,  b = b,  a
    print(f"Before Swapping number 1: {a} number 2: {b} ")



def sum_array_elements():
    """sum_array_elements"""
    arr = list(map(int,input("Enter array space separated by comma: ").split(',')))
    # With Loop
    sum1 = 0
    for i  in arr:
        sum1 = sum1 + i
    print(f"The array : {arr}")
    print(f"Sum of all elements of the array : {sum1}")
    result = sum(arr)
    print(f"Sum of all elements of the array with built-in function : {result}")

def cumulative_sum_list():
    """Print the list by keep on adding the elements"""
    arr = list(map(int,input("Enter numbers with space").split()))
    cum = []
    for i in range (len(arr)):
        if i == 0:
            cum.append(arr[0])
        else:
            cum.append(cum[i-1]+arr[i])
    print(f"The cummulative value for the array {arr}  : {cum}")

#
def length_list_strings():
    """Length of the list and strings"""
    list1 = list(map(int,input("Enter list of values with space: ").split()))
    print(f"Length of the list is : {len(list1)}")
    string1 = input("Enter a string: ")
    print(f"Length of the string is : {len(string1)}")



def star_pattern():
    """Star pattern"""
    a = int(input("The row till which u want the * "))
    for i in range (1, a+1):
        print(' ' * (a-i) + '* ' * i)






def reverse_list():
    """Print the list in reverse order"""
    list1 = list(map(int,input("Enter a List with space: ").split()))
    rev = list1[::-1]
    print(f"The List entered: {list1}")
    print(f"The List reversed with variable: {rev}")
    print(f"The List reversed without variable: {list1[::-1]}")

def reverse_string():
    """Reverse the string"""
    strr = input("Enter a string")
    rev = strr[::-1]
    print(f"The string entered: {strr}")
    print(f"The string reversed with variable: {rev}")
    print(f"The string reversed without variable: {strr[::-1]}")
#
def second_largest_number():
    """Second largest number"""
    number_list = list(map(int,input("Enter numbers one by one with space: ").split()))
    number_list.sort(reverse= True)
    print(f"Sorted list: {number_list}")
    print(f"Second Largest Number is: {number_list[1]}")
def remove_duplicates():
    """Remove duplicates from the list"""
    number_list = list(map(int,input("Enter numbers one by one with space: ").split()))
    unique_num = list(set(number_list))
    print(f"List of numbers added: {number_list}")
    print("Incase duplicate number is there that is removed successfully!!")
    print(f"The Final List: {unique_num}")

def check_empty_list():
    """Check if the list is empty"""
    number_list = list(map(int, input("Enter numbers one by one with space: ").split()))
    if not number_list:
        print("Empty List Detected!!")
    else:
        print(f"Displaying the list: {number_list} ")

def reverse_words_in_string():
    """Find words in string with vowel and Reverse the words in string """

    lis = input("Write the desired String:")
    vowel_words = lis.split()
    vowels = 'aeiouAEIOU'
    filtered_words = [word for word in vowel_words if any (char in vowels for char in word)]
    print("The words in the string which has vowels are: ", ' '.join(filtered_words))
    words = lis.split()
    reversed_words = [each[::-1] for each in words]
    print("The reversed words in the string is as follows:  ", ' '.join(reversed_words))



# ═══════════════════════════════════════════════════════════════════════════
#                           CONFIGURATION & MENU
# ═══════════════════════════════════════════════════════════════════════════

# Problem menu dictionary
Problems = {
    1: "Swap first and last element of a list",
    2: "Swap 2 numbers",
    3: "Sum of all elements in the array",
    4: "Print the list by keep on adding the elements",
    5: "Length of the list and strings",
    6: "Star pattern",
    7: "Print the list in reverse order",
    8: "Reverse the string",
    9: "Second largest number",
    10: "Remove duplicates from the list",
    11: "Check if the list is empty",
    12: "Reverse the words in string"
}

# Function mapping dictionary
problem_functions = {
    1: swap_first_last_element,
    2: swap_two_numbers,
    3: sum_array_elements,
    4: cumulative_sum_list,
    5: length_list_strings,
    6: star_pattern,
    7: reverse_list,
    8: reverse_string,
    9: second_largest_number,
    10: remove_duplicates,
    11: check_empty_list,
    12: reverse_words_in_string
}

# ═══════════════════════════════════════════════════════════════════════════
#                               MAIN PROGRAM
# ═══════════════════════════════════════════════════════════════════════════

def display_header():
    """Display program header with styling"""
    print("=" * 80)
    print("🐍 PRACTICING EASY CODES IN PYTHON - DAY 2 🐍".center(80))
    print("=" * 80)
    print()

def display_menu():
    """Display the menu options in a formatted way"""
    print("📋 Available Problems to Solve:")
    print("─" * 50)
    for key, value in Problems.items():
        print(f"   {key:2d}. {value}")
    print("─" * 50)

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
        choice = int(input("\n🔢 Enter your choice (1-12): "))

        if choice < 1 or choice > 12:
            print("❌ Invalid choice! Please enter a number between 1 and 12.")
            return

        print(f"\n✅ You selected: {Problems[choice]}")
        print("─" * 60)

        # Execute the corresponding function
        if choice in problem_functions:
            problem_functions[choice]()
        else:
            print("⚠️  Functionality for this option is not yet implemented.")

        print("\n" + "─" * 60)
        print("✨ Program completed successfully!")

    except ValueError:
        print("❌ Invalid input! Please enter a numeric value between 1 and 12.")
    except KeyboardInterrupt:
        print("\n\n👋 Program interrupted by user. Goodbye!")
    except Exception as e:
        print(f"❌ An unexpected error occurred: {e}")

# ═══════════════════════════════════════════════════════════════════════════
#                            PROGRAM ENTRY POINT
# ═══════════════════════════════════════════════════════════════��═══════════

if __name__ == "__main__":
    main()
