/*
ID: jesse_o1
LANG: C
PROB: gift1 
*/
#include <stdio.h>
#include <stdlib.h>

struct person{
  char* name;
  int amount;
};

int main () {
    FILE *fin  = fopen ("./gift1.in", "r");

    int num;
    fscanf (fin, "%d\n", &num);  
    printf ("%d\n", num);

    struct person people[5];

  for(int i = 0; i < num; i++){
    people[i].amount = 0;
    
    people[i].name = (char*)malloc(14*sizeof(char));
    fscanf(fin, "%s\n",people[i].name);
    printf("%s %d\n",people[i].name, people[i].amount);
  }

      char name[14];
      int amount[2];

      fscanf(fin, "%s %d %d", name, &amount[0], &amount[1]);
      printf("%s %d %d\n", name, amount[0], amount[1]);

   return 0; 
}
