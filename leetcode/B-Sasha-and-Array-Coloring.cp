#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int maxColoringCost(vector<int>& a) {
    sort(a.begin(), a.end()); // Sort the array in non-decreasing order
    int n = a.size();
    int maxCost = 0;

    for (int i = 0, j = n - 1; i < j; i++, j--) {
        // Calculate the cost of the current color as max(S) - min(S)
        // where S is the sequence of elements of that color
        int currentCost = a[j] - a[i];
        maxCost += currentCost;
    }

    return maxCost;
}

int main() {
    int t;
    cin >> t;

    while (t--) {
        int n;
        cin >> n;
        vector<int> a(n);

        for (int i = 0; i < n; i++) {
            cin >> a[i];
        }

        int result = maxColoringCost(a);
        cout << result << endl;
    }

    return 0;
}
