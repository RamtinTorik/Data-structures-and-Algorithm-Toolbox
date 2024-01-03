import os
import time

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
    stack = list()
    
    
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
                print("case3")
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
                print(
                "Please enter correct number :)")
                return_menu()
                
main()

# selection_sort()
# arr = enter_array()

# binary_search(arr)
# bubblesort(arr)
# }
# print(binary_search())



























