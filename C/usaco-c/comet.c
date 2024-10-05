/*
ID: jesse_o1
LANG: C
PROG: ride
*/
#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main() {
    FILE *fin = fopen("ride.in", "r");
    FILE *fout = fopen("ride.out", "w");


    char str1[10], str2[10];

    fscanf(fin, "%s %s", str1, str2); 

    int p1 = 1;
    int p2 = 1;

    for (int i = 0; i < strlen(str1); i++) {
        p1 *= (int)str1[i] - 'A' + 1; 
    }

    for (int i = 0; i < strlen(str2); i++) {
        p2 *= (int)str2[i] - 'A' + 1;    }

    if (p1 % 47 == p2 % 47) {
        fprintf(fout, "GO\n");
    } else {
        fprintf(fout, "STAY\n");
    }

    fclose(fin);
    fclose(fout);
}

