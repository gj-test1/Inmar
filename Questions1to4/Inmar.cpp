#include <iostream>
#include <string>
#include <boost/algorithm/string.hpp>

using namespace std;
using namespace boost;


class Test4class
{
public:

    int sum(int x, int y)
    {
        return (x+y);
    }
};

void main()
{
    // test #1
    cout << "Test #1 \n" << endl;
    for (int i = 1; i <= 100; i++)
    {
        if ( i % 3 == 0 )
        {
            cout << i << ": fizz \n";
        }
        
        if ( i % 5 == 0 )
        {
            cout << i << ": buzz \n";
        }
        
        if ( (i % 3 == 0) && (i % 5 == 0) )
        {
            cout << i << ": fizzbuzz \n";
        }
    }
    cout << "========================= \n" << endl;

    // test #2
    cout << "\n\nTest #2 \n" << endl;
    string str = "abcdef";
    string revStr = string(str.rbegin(), str.rend());
    cout << str << " ==> " << revStr << endl;
    cout << "========================= \n" << endl;

    // test #3
    cout << "\n\nTest #3 \n" << endl;
    
    string ssn = "123-45-6789";
    cout << "*** Input the SSN == : " ;
    cin >> ssn;
    cout << "Got input : " << ssn << endl;

    // Should use regular expression here, but having problem linking the library
    bool badSsn = false;
    if (ssn.find('-') != string::npos)
    {
        // make sure "-" is located at the 4th and 7th position
        if (ssn[3] != '-' || ssn[6] != '-') 
        {
            badSsn = true;
            cout << "Bad SSN format w/ hyphen!\n";
            return;
        }
    }

    boost::replace_all(ssn, "-", "");

    if (!badSsn && ssn.length() == 9)
    {
        cout << ssn << endl;
        for(size_t i = 0; i < ssn.length(); i++)
        {
            if (!isdigit(ssn[i]))
            {
                badSsn = true;
                break;
            }
        }
    }
    
    if (badSsn)
    {
        cout << "Bad SSN format!\n";
    }
    else
    {
        cout << "Good SSN #!\n";
    }
    cout << "========================= \n" << endl;

    // test #4
    cout << "\n\nTest #4 \n" << endl;

    Test4class t4c;
    int total = t4c.sum(2, 3);
    cout << "Sum is : " << total << endl;
	total = t4c.sum(-100, 2);
    cout << "Sum is : " << total << endl;

	// Since the negative testing will not pass the compilation, so the tests cannot be run
	// Possible test cases:
	// 1. Input strings instead of numbers
	// 2. make the summation exceed the scope of interger
	
}

