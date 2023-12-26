void printmenu()
{
	cout << "\n:::::::::::::::::::::::::::::::::::::::::::::"
		 << "\n::  Data structures and Algorithm Toolbox  ::"
		 << "\n:::::::::::::::::::::::::::::::::::::::::::::\n";

	cout << "\n:::::::::::::::: Program Menu :::::::::::::::\n";

	cout << "1. Search in Array(Binary Search)\n"
		<< "2. Sort Array\n"
		<< "3. Infix to Postfix or Prefix\n"
		<< "4. Heapify\n"
		<< "5. Adj Matrix to Graph And BFS\n" 
		<< "0. Exit\n";

	cout << "\nPlease Enter Your Choice: ";
}

void returnmenu()
{
	char ch1;
	if(k>0)
	{
		cin.get(ch1);
		if(ch1=='\n')
			system("cls");
	}
}

