#include <iostream>
#include <string>

int extract(std::string s) {
    int firstNum = -1;
    int lastNum = -1;
    for (int i = 0; i < s.size(); i++) {
        if (s[i] >= '0' && s[i] <= '9') {
            firstNum = s[i] - '0';
            break;
        }
    }
    for (int i = s.size() - 1; i >= 0; i--) {
        if (s[i] >= '0' && s[i] <= '9') {
            lastNum = s[i] - '0';
            break;
        }
    }
    // std::cout << firstNum << " " <<  lastNum << std::endl;
    return firstNum * 10 + lastNum;
}

int main() {
    int sum = 0;
    for (int i = 0; i < 1000; i++) {
        std::string s;
        std::cin >> s;
        sum += extract(s);
    }
    std::cout << sum << std::endl;
}