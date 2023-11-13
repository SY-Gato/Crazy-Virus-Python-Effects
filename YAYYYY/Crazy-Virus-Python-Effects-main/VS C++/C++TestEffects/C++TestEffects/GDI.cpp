#include <string>
#include <iostream>
#include <Windows.h>
using namespace std;

void GDI();
void clear_screen();
void askquestion();

HWND hwnd = GetDesktopWindow();
HDC hdc = GetDC(hwnd);

int main()
{
    askquestion();
};
void askquestion()
{
    std::string firstwarn = "Program Does No Actual Damage To Computer. Made for educational purposes only.";
    int width = 1024;
    firstwarn += std::to_string(width);

    LPWSTR ws = new wchar_t[firstwarn.size() + 1];
    copy(firstwarn.begin(), firstwarn.end(), ws);
    ws[firstwarn.size()] = 0;

    MessageBox(hwnd, ws, L"HAHA", MB_OK | MB_ICONQUESTION);
};
void GDI()
{
    hwnd = GetDesktopWindow();
    hdc = GetDC(hwnd);

    int y = GetSystemMetrics(0);
    int x = GetSystemMetrics(1);

    for (int i = 0; i < 1; i++)
    {
        hdc = GetDC(hwnd);

        for (int l = 0; l < 15; l++)
        {
            StretchBlt(hdc, 0, 0 - 10, x, y + 20, hdc, 0, 0, x, y, SRCCOPY);
            StretchBlt(hdc, 0 - 10, 0, x + 20, y, hdc, 0, 0, x, y, SRCCOPY);
            Sleep(200);
        }
    }
    clear_screen();
    Sleep(3500);
    for (int i = 0; i < 200; i++)
    {
        hwnd = GetDesktopWindow();
        hdc = GetDC(hwnd);
        BitBlt(hdc, 0, 1 + (rand() % 10), 1 + (rand() % x), y, hdc, 0, 0, SRCCOPY);
        DeleteDC(hdc);
        Sleep(100);
    };
    Sleep(1000);
    clear_screen();
}
void clear_screen()
{
    for (int num = 0; num < 10; num++)
    {
        InvalidateRect(0, 0, true);
        Sleep(10);
    }
};
