#include <iostream>

int main() {
    int n;
    std::cin >> n;
    int s;
    int count[5] = {0};
    for (int i = 0; i < n; i++) {
        std::cin >> s;
        count[s]++;
    }
    int cars = count[4];
    cars += count[3];
    count[1] -= count[3];
    cars += (count[2] + 1) / 2;
    if (count[2] % 2 == 1) {
        count[1] -= 2;
    }
    if (count[1] > 0) {
        cars += (count[1] + 3) / 4;
    }
    std::cout << cars << std::endl;
    return 0;
}