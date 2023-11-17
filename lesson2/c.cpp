#include <iostream>
#include <fstream>
#include <vector>

std::vector<int> count_hash_prefixes(const std::string& inp, int x, int module) {
    std::vector<int> hash_prefixes(inp.length(), 0);

    hash_prefixes[0] = inp[0] % module;
    for (int letter_id = 1; letter_id < inp.length(); ++letter_id) {
        hash_prefixes[letter_id] = (hash_prefixes[letter_id - 1] * x + inp[letter_id]) % module;
    }

    return hash_prefixes;
}

std::vector<int> precount_x_orders(const std::string& inp, int x, int module) {
    std::vector<int> precounted(inp.length() + 1, 0);
    precounted[0] = 1;
    for (int order = 1; order <= inp.length(); ++order) {
        precounted[order] = (x * precounted[order - 1]) % module;
    }

    return precounted;
}

int count_substr_hash(const std::vector<int>& init_hashes, int from_id, int len, const std::vector<int>& precounted_x, int module) {
    if (from_id > 0) {
        return (init_hashes[from_id + len - 1] - (init_hashes[from_id - 1] * precounted_x[len]) % module + module) % module;
    } else {
        return init_hashes[from_id + len - 1] % module;
    }
}

int main() {
    std::ifstream file("input.txt");
    std::string s;
    std::getline(file, s);

    std::vector<int> z_func_res(s.length(), 0);

    int l_elem_id = 0;

    for (int i = 1; i < s.length(); ++i) {
        bool done = false;

        z_func_res[i] = std::min(z_func_res[i - l_elem_id], l_elem_id + z_func_res[l_elem_id] - i);
        z_func_res[i] = std::max(z_func_res[i], 0);

        while (z_func_res[i] < s.length() - i && s[i + z_func_res[i]] == s[z_func_res[i]]) {
            z_func_res[i] += 1;
        }

        if (l_elem_id + z_func_res[l_elem_id] < i + z_func_res[i]) {
            l_elem_id = i;
        }
    }
    for (int i =0; i <  z_func_res.size()-1; i++) {
        std::cout << z_func_res[i] << " ";
    }
        std::cout << z_func_res.back();
    
    // this one works 
    return 0;
}