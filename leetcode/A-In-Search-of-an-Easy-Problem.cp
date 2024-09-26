#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;

    std::vector<int> opinions(n);
    for (int i = 0; i < n; i++) {
        std::cin >> opinions[i];
    }

    bool isHard = false;
    for (int i = 0; i < n; i++) {
        if (opinions[i] == 1) {
            isHard = true;
            break;
        }
    }

    if (isHard) {
        std::cout << "HARD" << std::endl;
    } else {
        std::cout << "EASY" << std::endl;
    }

    return 0;
}
