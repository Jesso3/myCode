#include <iostream>
#include <unistd.h>
#include <stdlib.h>
using namespace std;

void print();
void draw();

const int width = 20;
const int height = 20;
enum eDirection {Right, Left, Up, Down, Stop} dir;
char key = ' ';

int main() {
  draw();
  return 0;
}

void draw() 
{
  while (true)
  {
    system("clear");
    cout << ( dir==Left ) << endl;
    sleep(1);
    if (key == ' ')
      key = getchar();
    for(int i = 0; i < width; i++){
      cout << key;
    }
    cout << endl;
    sleep(1);
  }
}

void print()  {
  while (true) {
    cout << "#" << endl;
    sleep(1);
    system("clear");
    sleep(1);
  }
}
