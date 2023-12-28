import os

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
                print("case2")
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
# print(binary_search())

# def make_tree():
#     arr = list()
#     add
#     while True:
#         myinput = int(input())

























