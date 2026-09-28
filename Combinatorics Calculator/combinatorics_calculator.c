#include <stdio.h>
#include <ctype.h>

int fact(int num) {
    if (num < 0) return 0;
    if (num == 0) return 1;
    return num * fact(num - 1);
}

int perm(int a, int b) {
    if (b < 0) return 0;
    if (a < b) return 0;
    int total = 1;
    for (int i = 0; i < b; i++) total *= (a - i);
    return total;
}

int comb(int a, int b) {
    if (b < 0 || a < 0) return 0;
    if (a < b) return 0;
    int p = perm(a, b);
    int f = fact(b);
    return (f == 0) ? 0 : (p / f);
}

int homo(int a, int b) {
    if (a <= 0 || b < 0) return 0;
    return comb(a + b - 1, b);
}

int poww10(int ind) {
    int r = 1;
    for (int i = 0; i < ind; i++) r *= 10;
    return r;
}

int main(void) {
    char arr[100];
    char corporh = 0;
    char ints1c[100] = {0}, ints2c[100] = {0};
    int ints1cind = 0, ints2cind = 0;
    int done = 0;

    printf("입력 : ");
    if (scanf("%99s", arr) != 1) { puts("ERROR"); return 1; }

    for (int i = 0; arr[i] != '\0'; i++) {
        if (isdigit((unsigned char)arr[i])) {
            if (!done) ints1c[ints1cind++] = arr[i];
            else        ints2c[ints2cind++] = arr[i];
        } else {
            if (!done) { corporh = arr[i]; done = 1; }
            else { }
        }
    }

    if (ints1cind == 0 || corporh == 0 || ints2cind == 0) {
        puts("ERROR"); return 1;
    }

    int ints1 = 0, ints2 = 0;
    for (int i = 0; i < ints1cind; i++)
        ints1 += poww10(ints1cind - i - 1) * (ints1c[i] - '0');
    for (int i = 0; i < ints2cind; i++)
        ints2 += poww10(ints2cind - i - 1) * (ints2c[i] - '0');

    int out;
    switch (corporh) {
        case 'c': case 'C': out = comb(ints1, ints2); break;
        case 'p': case 'P': out = perm(ints1, ints2); break;
        case 'h': case 'H': out = homo(ints1, ints2); break;
        default: puts("ERROR"); return 1;
    }
    printf("%d\n", out);
    return 0;
}
