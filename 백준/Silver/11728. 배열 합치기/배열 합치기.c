#define _CRT_SECURE_NO_WARNINGS
#include <stdio.h>

int main()
{
    int a, b, c;
    int *arrA, *arrB, *arrC;
    int iA = 0, iB = 0, iC = 0;

    scanf("%d %d", &a, &b);
    c = a + b;

    arrA = (int*)malloc(sizeof(int) * a);
    arrB = (int*)malloc(sizeof(int) * b);
    arrC = (int*)malloc(sizeof(int) * c);

    // 배열 입력
    for (int i = 0; i < a; i++)
        scanf("%d", &arrA[i]);
    for (int i = 0; i < b; i++)
        scanf("%d", &arrB[i]);

    // 작은 순으로 C에 입력
    while (iA < a && iB < b) {
        if (arrA[iA] <= arrB[iB])
            arrC[iC++] = arrA[iA++];
        else
            arrC[iC++] = arrB[iB++];
    }

    // 남은 원소 입력
    while (iA < a)
        arrC[iC++] = arrA[iA++];
    while (iB < b)
        arrC[iC++] = arrB[iB++];

    for (int i = 0; i < c; i++)
        printf("%d ", arrC[i]);
}