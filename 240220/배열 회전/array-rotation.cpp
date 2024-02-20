#include <iostream>
#include <vector>
#include <algorithm>
using namespace std;

void circle(vector<vector<int>>& a, int y, int x, int n, int m) {
    if (n <= 0 || m <= 0) return;

    vector<int> elements;
    vector<pair<int, int>> indexes;

    int y1 = y, x1 = x, y2 = y + n - 1, x2 = x + m - 1;

    for (int j = x1; j < x2; ++j) {
        elements.push_back(a[y1][j]);
        indexes.push_back({ y1, j });
    }
    for (int i = y1; i < y2; ++i) {
        elements.push_back(a[i][x2]);
        indexes.push_back({ i, x2 });
    }
    for (int j = x2; j > x1; --j) {
        elements.push_back(a[y2][j]);
        indexes.push_back({ y2, j });
    }
    for (int i = y2; i > y1; --i) {
        elements.push_back(a[i][x1]);
        indexes.push_back({ i, x1 });
    }

    // 반시계 방향으로 회전: 첫 번째 요소를 맨 뒤로 이동
    rotate(elements.begin(), elements.begin() + 1, elements.end());

    int idx = 0;
    for (auto [i, j] : indexes) {
        a[i][j] = elements[idx++];
    }

    circle(a, y + 1, x + 1, n - 2, m - 2);
}

int main() {
    int n, m, k;
    cin >> n >> m >> k;

    vector<vector<int>> a(n, vector<int>(m));
    for (int i = 0; i < n; ++i) {
        for (int j = 0; j < m; ++j) {
            cin >> a[i][j];
        }
    }

    for (int _ = 0; _ < k; ++_) {
        circle(a, 0, 0, n, m);
    }

    for (const auto& rows : a) {
        for (const auto& elem : rows) {
            cout << elem << " ";
        }
        cout << "\n";
    }

    return 0;
}