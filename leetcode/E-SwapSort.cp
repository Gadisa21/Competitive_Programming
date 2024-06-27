#include <iostream>
#include <vector>

void swap(std::vector<int>& arr, int i, int j) {
    int temp = arr[i];
    arr[i] = arr[j];
    arr[j] = temp;
}

int main() {
    int n;
    std::cin >> n;

    std::vector<int> arr(n);
    for (int i = 0; i < n; i++) {
        std::cin >> arr[i];
    }

    std::vector<std::pair<int, int>> swaps;

    for (int i = 0; i < n; i++) {
        int minIndex = i;
        for (int j = i + 1; j < n; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }
        if (minIndex != i) {
            swaps.push_back(std::make_pair(i, minIndex));
            swap(arr, i, minIndex);
        }
    }

    std::cout << swaps.size() << std::endl;
    for (const auto& s : swaps) {
        std::cout << s.first << " " << s.second << std::endl;
    }

    return 0;
}
