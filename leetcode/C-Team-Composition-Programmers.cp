#include <iostream>
#include <algorithm> // For swap() function

using namespace std;

void solveTestCase() {
    int a, b;
    cin >> a >> b;
    
    if (a < b) swap(a, b);

    // Calculate the maximum number of teams
    int diff = a - b;
    int teamsWithProgrammersAndMathematicians = min(b, diff / 2);
    int remainingProgrammers = b - teamsWithProgrammersAndMathematicians;
    int remainingTeamsWithProgrammersOnly = remainingProgrammers / 2;

    // Total maximum teams
    int maxTeams = teamsWithProgrammersAndMathematicians + remainingTeamsWithProgrammersOnly;
    cout << maxTeams << "\n";
}

int main() {
    ios_base::sync_with_stdio(false);
    cin.tie(NULL);

    int t;
    cin >> t;

    while (t--) {
        solveTestCase();
    }

    return 0;
}
