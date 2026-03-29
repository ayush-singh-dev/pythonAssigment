#include <iostream>
#include <stack>
#include <cmath>
using namespace std;

// Stack using array
#define MAX 100
int stackArr[MAX];
int top = -1;

// PUSH
void push(int value)
{
    if (top == MAX - 1)
    {
        cout << "Stack Overflow\n";
    }
    else
    {
        top++;
        stackArr[top] = value;
        cout << value << " pushed into stack\n";
    }
}

// POP
void pop()
{
    if (top == -1)
    {
        cout << "Stack Underflow\n";
    }
    else
    {
        cout << stackArr[top] << " popped from stack\n";
        top--;
    }
}

// DISPLAY
void display()
{
    if (top == -1)
    {
        cout << "Stack is empty\n";
    }
    else
    {
        cout << "Stack elements:\n";
        for (int i = top; i >= 0; i--)
        {
            cout << stackArr[i] << endl;
        }
    }
}

// RECURSION (FACTORIAL)
int factorial(int n)
{
    if (n == 0 || n == 1)
        return 1;
    else
        return n * factorial(n - 1);
}

// POLISH NOTATION (POSTFIX EVALUATION)
int evaluatePostfix(string exp)
{
    stack<int> s;

    for (int i = 0; i < exp.length(); i++)
    {

        if (isdigit(exp[i]))
        {
            s.push(exp[i] - '0');
        }
        else
        {
            int val2 = s.top();
            s.pop();
            int val1 = s.top();
            s.pop();

            switch (exp[i])
            {
            case '+':
                s.push(val1 + val2);
                break;
            case '-':
                s.push(val1 - val2);
                break;
            case '*':
                s.push(val1 * val2);
                break;
            case '/':
                s.push(val1 / val2);
                break;
            }
        }
    }
    return s.top();
}

// MAIN MENU
int main()
{
    int choice, value, n;
    string exp;

    do
    {
        cout << "\n===== STACK MENU =====\n";
        cout << "1. Push\n";
        cout << "2. Pop\n";
        cout << "3. Display\n";
        cout << "4. Recursion (Factorial)\n";
        cout << "5. Polish Notation (Postfix)\n";
        cout << "6. Exit\n";
        cout << "Enter your choice: ";
        cin >> choice;

        switch (choice)
        {

        case 1:
            cout << "Enter value: ";
            cin >> value;
            push(value);
            break;

        case 2:
            pop();
            break;

        case 3:
            display();
            break;

        case 4:
            cout << "Enter number: ";
            cin >> n;
            cout << "Factorial = " << factorial(n) << endl;
            break;

        case 5:
            cout << "Enter postfix expression (single digit operands): ";
            cin >> exp;
            cout << "Result = " << evaluatePostfix(exp) << endl;
            break;

        case 6:
            cout << "Exiting program...\n";
            break;

        default:
            cout << "Invalid choice\n";
        }

    } while (choice != 6);

    return 0;
}