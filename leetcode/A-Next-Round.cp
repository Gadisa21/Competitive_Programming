#include <iostream>
#include <vector>

using namespace std;

int main() {
    int n, k;
    cin >> n >> k;

    vector<int> scores(n);
    for (int i = 0; i < n; i++) {
        cin >> scores[i];
    }

    int advancedCount = 0;
    int kthScore = scores[k - 1];

    for (int i = 0; i < n; i++) {
        if (scores[i] >= kthScore && scores[i] > 0) {
            advancedCount++;
        } else {
            break;  // No need to check further
        }
    }

    cout << advancedCount << endl;

    return 0;
}
