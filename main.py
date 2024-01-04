import os
import time
import regex

def print_menu():
    os.system("cls")
    print(
    ":::::::::::::::::::::::::::::::::::::::::::::"
	"\n::  Data structures and Algorithm Toolbox  ::"
	"\n:::::::::::::::::::::::::::::::::::::::::::::\n"

	"\n:::::::::::::::: Program Menu :::::::::::::::\n"

	"1. Search in Array(Binary Search)\n"
	"2. Sort Array\n"
	"3. Infix to Postfix or Prefix\n"
	"4. Heapify\n"
	"5. Adj Matrix to Graph And BFS\n"
	"0. Exit\n")

    myinput = input("Please Enter Your Choice: ")
    return myinput

def return_menu():
    while(True):
        myinput = input("\nPlease press enter to return menu...")
        if myinput == '':
            main()
            break
        else:
            os.system("cls")
            print("Please enter correct key :)\n")
            
            
def enter_array():
    arr = [int(i) for i in list(input("Please enter your array: ").split(','))]
    return arr
    
def enter_number():
    number = int(input("Please enter your number: "))
    return number
    
def binary_search():
    number = enter_number()
    arr = enter_array()
    arr.sort()
    print("sorted array: ", arr)
    low = 0
    high = len(arr)-1
    while low <= high:
        middle = (low+high)//2
        if arr[middle] == number:
            return middle+1
        elif arr[middle] < number:
            low = middle + 1
        else:
            high = middle - 1
    return 'x'

def insertion_sort():
    arr = enter_array()
    n=len(arr)
    print("\n", end ='')
    for i in range(1, n):
        key = arr[i]
        j = i-1
        while (arr[j] > key) & (j>=0):
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
        print(f"step {i}: ", arr)
    print("\nsorted array: ", arr)
    
    
def selection_sort():
    arr = enter_array()
    n=len(arr)
    print("\n", end ='')
    for i in range(n-1, 0, -1):
        # print(i)
        max = arr[0]
        index = 0
        for j in range(1, i+1):
            if(arr[j]>max):
                max = arr[j]
                index = j
        arr[index] = arr[i]
        arr[i] = max
        print(f"step {n-i}: ", arr)
    print("\nsorted array: ", arr)

def sort_array():
    while True:
        print(
        "1. insertion sort\n"
        "2. selection sort\n")
        myinput = input("Which type of sorting do you choose? ")
        if myinput == '1':
            insertion_sort()
            break
        elif myinput == '2':
            selection_sort()
            break
        else:
            print("Please enter correct number :)")
        
def infix_converter():
    
    while True:
        mystring = input("Please enter your infix string: ")
        result = regex.match(r"^(([+-]*\d+|\((?1)\))([+^*/-](?2))*)$", mystring)
        if "None" in str(result):
            os.system("cls")
            print("please enter infix string ;)")
        else:
            break
            
    def prec(c):
        if c == '^':
            return 3
        elif c == '/' or c == '*':
            return 2
        elif c == '+' or c == '-':
            return 1
        else:
            return -1

    def associativity(c):
        if c == '^':
            return 'R'
        return 'L' # Default to left-associative
    
    def infix_to_postfix(infix):
        result = []
        stack = []

        for i in range(len(infix)):
            c = infix[i]

            # If the scanned character is an operand, add it to the output string.
            if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
                result.append(c)
            # If the scanned character is an ‘(‘, push it to the stack.
            elif c == '(':
                stack.append(c)
            # If the scanned character is an ‘)’, pop and add to the output string from the stack
            # until an ‘(‘ is encountered.
            elif c == ')':
                while stack and stack[-1] != '(':
                    result.append(stack.pop())
                stack.pop() # Pop '('
            # If an operator is scanned
            else:
                while stack and (prec(infix[i]) < prec(stack[-1]) or
                                (prec(infix[i]) == prec(stack[-1]) and associativity(infix[i]) == 'L')):
                    result.append(stack.pop())
                stack.append(c)

        # Pop all the remaining elements from the stack
        while stack:
            result.append(stack.pop())

        postfix = ''.join(result)
        return postfix
    
    def infix_to_prefix(infix):
        l = len(infix)
    
        infix = infix[::-1]
    
        l_infix = []
        
        for i in range(l):
            l_infix.append(infix[i]) 
                
        for i in range(l):
            if l_infix[i] == '(':
                l_infix[i] = ')'
            elif l_infix[i] == ')':
                l_infix[i] = '('

        infix = ''.join(l_infix)
        
        prefix = infix_to_postfix(infix)
        prefix = prefix[::-1]
    
        return prefix
    
    print("prefix:", infix_to_prefix(mystring))
    print("postfix:",infix_to_postfix(mystring))
    # print(infix_to_postfix(mystring))
    
    
def main():
    while True:
        match print_menu():
            case '1':
                os.system("cls")
                result = binary_search()
                if result != 'x':
                    print("\nThe desired number is index" ,result)
                else:
                    print("\ndoesn't exist... :(")
                return_menu()

            case '2':
                os.system("cls")
                sort_array()
                return_menu()
                
            case '3':
                os.system("cls")
                infix_converter()
                return_menu()
            
            case '4':
                os.system("cls")
                print("case 4")
                return_menu()

            case '5':
                os.system("cls")
                print("case 5")
                return_menu()
                
            case '0':
                os.system("cls")
                print("\nI hope to see you in the future!... ^_^\n")
                exit(1)
            case _:
                os.system("cls")
                print("Please enter correct number :)")
                return_menu()
                
main()

# selection_sort()
# arr = enter_array()

# binary_search(arr)
# bubblesort(arr)
# }
# print(binary_search())



























