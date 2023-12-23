#include <iostream>
#include <vector>

int main() {
    int n;
    std::cin >> n;

    std::vector<int> studs_data(n);
    for (int i = 0; i < n; ++i) {
        std::cin >> studs_data[i];
    }

    for (int starosta_id = 0; starosta_id < n - 1; ++starosta_id) {
        int counts = 0;
        int starosta_points = studs_data[starosta_id];

        for (int other_student_id = 0; other_student_id < n; ++other_student_id) {
            if (other_student_id != starosta_id) {
                counts += std::abs(studs_data[other_student_id] - studs_data[starosta_id]);
            }
        }

        std::cout << counts << " ";
    }

    int counts = 0;
    int starosta_points = studs_data[n - 1];

    for (int other_student_id = 0; other_student_id < n; ++other_student_id) {
        if (other_student_id != n - 1) {
            counts += std::abs(studs_data[other_student_id] - studs_data[n - 1]);
        }
    }

    std::cout << counts << std::endl;

    return 0;
}
