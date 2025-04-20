#include <stdio.h>
#include <stdlib.h>
#include <time.h>

int main() {
    srand(time(0));

    printf("Generando 3 números aleatorios:\n");
    for (int i = 0; i < 3; i++) {
        int num = rand() % 101;
        printf("- %d\n", num);
    }

    return 0;
}
