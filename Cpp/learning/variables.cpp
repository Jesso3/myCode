#include <iostream>
using namespace std;

int main()
{
  int a, b;
  int result;

  a = 0x15;
  b = 2;
  a++;
  result = a - b;
  cout << "a: " << a << " b: " << b << " difference: " << result;

  return 0;
}
