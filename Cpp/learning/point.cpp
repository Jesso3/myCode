#include <iostream>
using namespace std; 

int main () 
{
  const char * foo = "hello!";

  for(int i = 0; i < 10; i++){
    cout << foo[i] << "\n";
  }
}

