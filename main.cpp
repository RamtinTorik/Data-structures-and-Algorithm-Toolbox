// 40111360027 , ramtin torik , Data structures and Algorithm Toolbox Project
// 40111360027 ، رامتین طریک ، Data structures and Algorithm Toolbox Project


#include <iostream>
#include <fstream>
#include <cstring>
#include "other.cpp"
#include "cases.cpp"
using namespace std;

// void read_contacts_book()
// {

// }

int main()
{
    system("cls");
    while (true)
    {
        returnmenu();
        printmenu();
        cin >> initial_input;
        getchar();
        system("cls");
        switch (initial_input)
        {
            case '1':
            {
                // system("cls");
                // cout << "case 1\n";
                savecontacts();
                k++;
                break;
            }

            case '2':
            {
                // system("cls");
                // cout << "case 2\n";
                displaycontacts();
                k++;
                break;
            }

            case '3':
            {
                // system("cls");
                // cout << "case 3\n";
                searchcontact();
                cout << "\nPlease press enter to return menu...";
                k++;
                break;
            }
            case '4':
            {
                // system("cls");
                cout << ":::::::::::: Update Contact :::::::::::::\n";
                updatecontact(searchcontact());
                k++;
                break;
            }

            case '5':
            {
                // system("cls");
                // cout << "case 5\n";
                deletespecificcontact();
                k++;
                break;
            }

            case '0':
            {
                // system("cls");
                // cout << "case 0\n";
                cout << "\nI hope to see you in the future!... ^_^\n";
                k++;
                exit(0);
                break;
            }
            
            default:
            {
                // cout << "default";
                cout << "Please enter correct number :)\n";
                cout << "Please press enter to return menu...";
                k++;
                break;
            }

        }
    }

    return 0;
}







































// void user_input()
// {
//     vector<int> myvec;
//     while(true)
//     {
//         char c[10];
//         cin >> c;
//         if(48 <= int(c) && int(c) <= 57)
//         {   
//             myvec.push_back(int(c));
//         }
//     }
// }

// int main()
// {
//     cout << "please enter your input:" << endl;
//     user_input();
    
//     return 0;
// }