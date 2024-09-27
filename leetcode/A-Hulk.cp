#include <iostream>
#include <string>

using namespace std;

string drBannerFeeling(int n) {
    string feeling = "";

    for (int i = 1; i <= n; i++) {
        if (i % 2 == 1) {
            feeling += "I hate ";
        } else {
            feeling += "I love ";
        }

        if (i != n) {
            feeling += "that ";
        }
    }

    feeling += "it";

    return feeling;
}

int main() {
    int n;
    cin >> n;

    string result = drBannerFeeling(n);
    cout << result << endl;

    return 0;
}
