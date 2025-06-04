#include <stdio.h>

int main() {
    char islem;
    float sayi1, sayi2;

    printf("İşlem gir (+, -, *, /): ");
    scanf(" %c", &islem);

    printf("İki sayı girin: ");
    scanf("%f %f", &sayi1, &sayi2);

    switch(islem) {
        case '+':
            printf("Sonuç: %.2f\n", sayi1 + sayi2);
            break;
        case '-':
            printf("Sonuç: %.2f\n", sayi1 - sayi2);
            break;
        case '*':
            printf("Sonuç: %.2f\n", sayi1 * sayi2);
            break;
        case '/':
            if(sayi2 != 0)
                printf("Sonuç: %.2f\n", sayi1 / sayi2);
            else
                printf("Sıfıra bölünemez.\n");
            break;
        default:
            printf("Geçersiz işlem.\n");
    }
    return 0;
}
