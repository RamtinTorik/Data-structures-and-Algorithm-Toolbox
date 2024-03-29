import os
import time
import regex
import math

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
            
def enter_array(begin):
    if begin == True:
        try:
            arr = [int(i) for i in list(input("Please enter your array: ").split(','))]
            return arr
        except:
            os.system("cls")
            print("Please enter correct array :)\n")
            return enter_array(True)
    else:
        try:
            arr = [int(i) for i in list(input("Please enter your array: ").split(','))]
            x = [0]
            x.extend(arr)
            return x
        except:
            os.system("cls")
            print("Please enter correct array :)\n")
            return enter_array(False)
    
def enter_number():
    try:
        number = int(input("Please enter your number: "))
        return number
    except:
        os.system("cls")
        print("Please enter correct value :)\n")
        return enter_number()
    
def binary_search():
    number = enter_number()
    arr = enter_array(True)
    arr.sort()
    print("sorted array: ", arr)
    low = 0
    high = len(arr)-1
    while low <= high:
        middle = (low+high)//2
        if arr[middle] == number:
            return middle
        elif arr[middle] < number:
            low = middle + 1
        else:
            high = middle - 1
    return 'x'

def insertion_sort():
    arr = enter_array(True)
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
    arr = enter_array(True)
    n=len(arr)
    print("\n", end ='')
    for i in range(n-1, 0, -1):
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
            os.system("cls")
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
        mystack = []

        for i in range(len(infix)):
            c = infix[i]
            if ('a' <= c <= 'z') or ('A' <= c <= 'Z') or ('0' <= c <= '9'):
                result.append(c)
            elif c == '(':
                mystack.append(c)
            elif c == ')':
                while mystack and mystack[-1] != '(':
                    result.append(mystack.pop())
                mystack.pop()
            else:
                while mystack and (prec(infix[i]) < prec(mystack[-1]) or
                                (prec(infix[i]) == prec(mystack[-1]) and associativity(infix[i]) == 'L')):
                    result.append(mystack.pop())
                mystack.append(c)
            
        while mystack:
            result.append(mystack.pop())

        postfix = ''.join(result)
        return postfix
    
    def infix_to_prefix(infix):
        l = len(infix)
        infix = infix[::-1]
        copy_infix = []
        
        for i in range(l):
            copy_infix.append(infix[i]) 
                
        for i in range(0, l):
            if copy_infix[i] == '(':
                copy_infix[i] = ')'
            elif copy_infix[i] == ')':
                copy_infix[i] = '('

        infix = ''.join(copy_infix)
        
        prefix = infix_to_postfix(infix)
        prefix = prefix[::-1]
    
        return prefix
    
    print("prefix:", infix_to_prefix(mystring))
    print("postfix:",infix_to_postfix(mystring))
    
def heapify():
    
    def max_heapify(mylist, i, length):
        l = 2*i
        r = 2*i + 1
        if (l <= length) and (mylist[l] > mylist[i]):
            largest = l
        else:
            largest = i
        if (r <= length) and (mylist[r] > mylist[largest]):
            largest = r
        if largest != i:
            temp = mylist[i]
            mylist[i] = mylist[largest]
            mylist[largest] = temp
            max_heapify(mylist, largest, length)

    def build_max_heap(mylist):
        length = len(mylist)-1
        for i in range(length//2, 0, -1):
            max_heapify(mylist, i, length)
        return mylist

    mylist = enter_array(False)
    result = build_max_heap(mylist)
    
    print("Max Heap: ", result[1:])
    
def adjmatrix_to_graph_BFS():
    def enter_vertex():
        arr = list(input("Please enter your vertices: ").split(','))
        return arr
    
    def adjmatrix():
        vertices = enter_vertex()
        length = len(vertices)
        matrix = list()
        for i in range(0, length):
            temp_matrix = list()
            for j in range(0, length):
                temp_matrix.append(0)
            matrix.append(temp_matrix)
        return vertices, matrix
    
    def enter_x_y(vertices, len_vertices):
        print(f"input in range(1,{len_vertices}) and enter 'e' to finish")
        x = input("Please enter x: ")
        if x == 'e':
            return -1,-1
        else:
            try:
                y = input("Please enter y: ")
                x = int(x)
                y = int(y)
                if ((x > 0) and (x <= len_vertices)) and ((y > 0) and (y <= len_vertices)):
                    return x,y
                else:
                    os.system("cls")
                    print("Please enter correct input :)")
                    print(vertices)
                    return enter_x_y(vertices, len_vertices)
            except:
                os.system("cls")
                print("Please enter correct input :)")
                print(vertices)
                return enter_x_y(vertices, len_vertices)
        
    def print_change_adjmatrix(vertices, matrix):
        while True:
            counter = 1
            print("\n   ", end=' ')   
            for i in vertices:
                print(f"({counter}){i}", end=' ')
                counter += 1
            print('\n', end='')
            counter = 1
            for j in matrix:
                print(f"({counter}){vertices[counter-1]} ", end=' ')
                for k in j:
                    print(f"{k}   ", end=' ')
                print('\n', end='')
                counter += 1
                
            x,y = enter_x_y(vertices, len(vertices))
            
            if x==-1 or y==-1:
                break
            else:
                matrix[x-1][y-1] = 1
                matrix[y-1][x-1] = 1
                os.system("cls")
                print(vertices)
        return matrix
    
    def build_graph(vertices, matrix):
        mydict = dict()
        counter1 = 0
        for i in matrix:
            counter2 = 0
            mylist = list()
            for j in i:
                if j == 1:
                    mylist.append(vertices[counter2])
                    mydict[vertices[counter1]] = mylist
                counter2 += 1
            counter1 += 1
        return mydict
    
    def graph_to_BFS(vertices, graph):
        my_marked_vertices = dict()
        queue = list()
        keys = graph.keys()
        result = list()
        for key in keys:
            my_marked_vertices[key] = 0
        queue.append(vertices[0])
        my_marked_vertices[vertices[0]] = 1 
        result.append(vertices[0])
        
        while queue != []:
            i = queue.pop(0)
            for adjacent in graph[i]:
                if my_marked_vertices[adjacent] == 0:
                    queue.append(adjacent)
                    my_marked_vertices[adjacent] = 1
                    result.append(adjacent)

        print("BFS: ", ''.join(result))
            
    vertices, matrix = adjmatrix()
    matrix = print_change_adjmatrix(vertices, matrix)
    graph = build_graph(vertices, matrix)
    graph_to_BFS(vertices, graph)
    
def main():
    while True:
        match print_menu():
            case '1':
                os.system("cls")
                result = binary_search()
                if result != 'x':
                    print("\nThe desired number is index" ,result+1)
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
                heapify()
                return_menu()

            case '5':
                os.system("cls")
                adjmatrix_to_graph_BFS()
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
