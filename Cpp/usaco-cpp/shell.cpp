/* Use the slash-star style comments or the system won't see your
   identification information */
/*
ID: jesseo1
TASK: shell 
LANG: C++                 
*/
/* LANG can be C++11 or C++14 for those more recent releases */
#include <iostream>
#include <fstream>
#include <string>

using namespace std;

int main() {
    ofstream fout ("shell.out");
    ifstream fin ("shell.in");
    int a, b;
    fin >> a >> b;
    fout << a+b << endl;
    return 0;
}
