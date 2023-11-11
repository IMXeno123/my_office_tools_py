#define _CRT_SECURE_NO_WARNINGS 1
#include <stdio.h>
#include <string.h>
#include <locale.h>
#include <wchar.h>
#include <windows.system.h>
#include <stdbool.h>
#include <math.h>

struct my_swap
{
	int x;
	int y;
};

int test() {
	int input = 0;
	int res_ = scanf("%d", &input);
	if (input == 1)
	{
		wprintf(L"真");
		int i;
		for (i = 0; i < 5; i++) {
			printf("\nfuck");
		}
	}
	else {
		wprintf(L"假");
		printf("%d\n", res_);
		int i = 1;
		while (i <= 300) {
			printf("%d shit\n", i);
			i++;
		}
	}
	return 1;
}

int add(int x, int y) {
	return x + y;
}

void array_() {
	int arr[] = { 0,1,2,3,4,5,6,7,8,9 };
	int i;
	for (i = 0; i < (sizeof(arr) / sizeof(arr[0])); i++) {
		printf("%d\n", arr[i]);
	}

}

int divison() {
	int a = 7;
	a = -a;
	int b = 2;
	int c = a % b;
	c += a;
	wprintf(L"%d", c);
	return c;
}

int morethan() {
	int a = 10;
	int* q = &a;
	int b = *q;
	int r = a > b ? a : b;
	//int* p1, * p2, * p3 = (& a, & a, & a);
	printf("%zu\n", sizeof(char*));
	return r;
}

void jsys() {
	int a = 0;
	int b = 0;
	int c = scanf("%d %d", &a, &b);
	int j = a / b;
	int i = a % b;
	printf("%d  %d\n", j, i);
	printf("%d", c);
}

void ifsentence() {
	if (3 == 5) {
		printf("shit");
	}
	else if (5 == 5) {
		printf("eee");
	}
	else {
		printf("hehe");
	}
}

void whileloop() {
	int i = 0;
	while (i < 100) {
		i++;
		printf("%d ", i);
	}
}

void getcharr() {
	char password[20] = { 0 };
	printf("input your password: ");
	int a = scanf("%s", password);
	int ch = '\0';
	while ((ch = getchar()) != '\n') {
		;
	}
	printf("Y/N: ");
	int ret = getchar();
	if ('Y' == ret) {
		printf("Yes");
	}
	else {
		printf("No");
	}
}

void srtm() {
	int year = 0;
	int month = 0;
	int day = 0;
	int a = scanf("%4d%2d%2d", &year, &month, &day);
	printf("year=%d\n", year);
	printf("month=%02d\n", month);
	printf("day=%02d\n", day);
}

void xscjoutput() {
	int id = 0;
	float c = 0.0f;
	float math = 0.0f;
	float english = 0.0f;
	int a = scanf("%d;%f,%f,%f", &id, &c, &math, &english);
	int b = printf("Id of %d is %.2f %.2f %.2f", id, c, math, english);
	printf("\n%d", b);

}

void zsoutput() {
	//int a = 0;
	//int b = 0;
	//int c = 0;
	//int d = 0;
	//int j = scanf("%d %d %d %d", &a ,&b, &c, &d);
	int arr[4] = { 0 };
	for (int i = 0;i < 4;i++) {
		int a = scanf("%d", &arr[i]);
	}
	int max = arr[0];
	for (int i = 0;i < (sizeof(arr) / sizeof(arr[0]));i++) {
		if (arr[i] > max) {
			max = arr[i];
			Sleep(1000);
		}
	}
	printf("%d", max);
}

void paoma()
{
	char arr1[] = "welcome to bitt!!!!";
	char arr2[] = "###################";
	int left = 0;
	int right = (int)strlen(arr2) - 1;
	while (left <= right)
	{
		arr2[left] = arr1[left];
		arr2[right] = arr1[right];
		printf("%s\n", arr2);
		Sleep(1000);
		system("cls");
		left++;
		right--;
	}
	;
}

void login()
{
	char pw[20] = "123456";
	char npw[20] = { 0 };
	for (int i = 0;i < 3;i++)
	{
		printf("please input the password: ");
		int a = scanf("%s", npw);
		if (strcmp(npw, pw) == 0)
		{
			printf("success\n");
			break;
		}
		else
		{
			printf("fail\n");
			if (i == 2)
			{
				printf("\nfuck!\n");

			}
		}
	}


}

//char input(char *s)
//{
//	printf("%s\n", s);
//	char str[] = { 0 };
//	int a = scanf("%s", str);
//	return str;
//}

//char** print_string(char *s)
//{
//	printf("%s\n", s);
//	char str[] = { 0 };
//	int a = scanf("%s", str);
//	return str;
//}

void gotot()
{
	printf("fuck you\n");
	int i = 0;
again:
	printf("yeah daddy\n");
	i++;

	if (i < 3)
	{
		goto again;
	}

}

int getmax(int a, int b)
{
	if (a > b)
	{
		printf("%d\n", a);
		return a;
	}
	else
	{
		printf("%d\n", b);
		return b;
	}
}

struct my_swap swap(int x, int y)
{
	struct my_swap p;
	int j = x;
	p.x = y;
	p.y = j;
	return p;
}

bool is_prime(int n) {
	int j = 0;
	for (j = 2;j <= sqrt(n);j++) {
		if (n % j == 0) {
			return false;
		}
	}
	return true;
}

int main() {
	system("chcp 65001");
	setlocale(LC_ALL, "chs");
	//??
	int i = 0;
	for (i = 100;i <= 200;i++) {
		if (is_prime(i)) {
			printf("%d ", i);
		}
	}
	return 0;
};