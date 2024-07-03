#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

int countElementsLessThanOrEqual(vector<int>& a, int target) {
    int left = 0;
    int right = a.size() - 1;
    int result = -1;

    while (left <= right) {
        int mid = left + (right - left) / 2;
        if (a[mid] <= target) {
            result = mid;
            left = mid + 1;
        } else {
            right = mid - 1;
        }
    }

    return result + 1;
}

int main() {
    int n, m;
    cin >> n >> m;

    vector<int> a(n);
    vector<int> b(m);

    for (int i = 0; i < n; i++) {
        cin >> a[i];
    }

    for (int i = 0; i < m; i++) {
        cin >> b[i];
    }

    sort(a.begin(), a.end());

    for (int i = 0; i < m; i++) {
        int count = countElementsLessThanOrEqual(a, b[i]);
        cout << count << " ";
    }

    cout << endl;

    return 0;
}
