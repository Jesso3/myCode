/*
ID: jesse_o1
LANG: C
TASK: test
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main () {
    char* str1 = "ABSTAR";
    char* str2 = "USACO";
    int p1 = 1;
    int p2 = 1;
    for(int i = 0; i < strlen(str1); i++){
      p1 *= (int)str1[i]-64;
    }
    for(int i = 0; i < strlen(str2); i++){
      p2 *= (int)str2[i]-64;
    }

    if (p1%47 == p2%47){
      printf("GO\n");
    }
    else{
    printf("STAY\n");
  }
    return 0;
}
