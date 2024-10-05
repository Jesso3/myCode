#include <iostream>
#include <ctime>
using namespace std;

int main() {
  time_t initial;
  time_t after;
  time_t difference;
  // stores time in current_time
  time(&initial);

  for(int i = 0; i < 1000000000; i++){
    cout << "";
  }

  time(&after);

  cout << after - initial << endl;

  return 0;
}
