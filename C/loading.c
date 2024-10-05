#include <stdio.h>
#include <unistd.h>

int main(void){
  int length=50;
  while (1==1){
    for(int i = 0; i <= length; i++){
      printf("\e[1;1H\e[2J");
      printf("%s","[");
      for(int j = 0; j <= i; j++){
        printf("%s","*");
      }
      for(int j = 0; j < length-i; j++){
        printf("%s","-");
      }
      printf("%s\n", "]");
      usleep(10000);
    }
  }
}
