#include <stdio.h>
#include <math.h>

int main() {
    double num, result;

    printf("Ingresa un número: ");
    scanf("%lf", &num);

    result = sqrt(num);

    printf("La raíz cuadrada de %.2lf es %.2lf\n", num, result);

    return 0;
}

En este codigo a diferencia del otro podremos sacar raises cuadradas