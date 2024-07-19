#include <iostream>
using namespace std;

int main()
{
  char foo = 'a';
  char* bar = &foo;
  int i = 0;

  while (true){
    try{
      cout << *(bar-i);
      i++;
    }
    catch (...){
      cout << "No!";
      break;
    }
  }
}
