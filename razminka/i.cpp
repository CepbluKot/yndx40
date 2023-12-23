#include <iostream>
#include <string>

class Solution {
public:
    bool isValid(std::string sequence) {
        // Replace the proper pairs until sequence becomes empty or no pairs are present
        while (true) {
            if (sequence.find("()") != std::string::npos) {
                size_t pos = sequence.find("()");
                sequence.erase(pos, 2);
            } else if (sequence.find("{}") != std::string::npos) {
                size_t pos = sequence.find("{}");
                sequence.erase(pos, 2);
            } else if (sequence.find("[]") != std::string::npos) {
                size_t pos = sequence.find("[]");
                sequence.erase(pos, 2);
            } else {
                return sequence.empty();
            }
        }
    }
};

int main() {
    std::string sequence;
    std::cin >> sequence;

    Solution solution;
    if (solution.isValid(sequence)) {
        std::cout << "yes" << std::endl;
    } else {
        std::cout << "no" << std::endl;
    }

    return 0;
}
