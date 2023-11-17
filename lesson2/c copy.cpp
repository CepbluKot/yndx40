#include <iostream>
// #include <fstream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <math.h>


using namespace std;

int randint(int lower, int upper) {
    return rand() % (upper - lower + 1) + lower;
}

vector<int> count_hash_prefixes(const string& inp, int x, int module) {
    vector<int> hash_prefixes(inp.size(), 0);

    hash_prefixes[0] = static_cast<int>(inp[0]) % module;
    for (int letter_id = 1; letter_id < inp.size(); ++letter_id) {
        hash_prefixes[letter_id] = (hash_prefixes[letter_id - 1] * x + static_cast<int>(inp[letter_id])) % module;
    }

    return hash_prefixes;
}

vector<int> precount_x_orders(const string& inp, int x, int module) {
    vector<int> precounted(inp.size() + 1, 0);
    precounted[0] = 1;

    for (int order = 1; order <= inp.size(); ++order) {
        precounted[order] = (x * precounted[order - 1]) % module;
    }

    return precounted;
}

int count_substr_hash(const vector<int>& init_hashes, int from_id, int len, const vector<int>& precounted_x, int module) {
    if (from_id > 0) {
        return (init_hashes[from_id + len - 1] - (init_hashes[from_id - 1] * precounted_x[len]) % module + module) % module;
    } else {
        return init_hashes[from_id + len - 1] % module;
    }
}

int main() {
    srand(static_cast<unsigned>(time(0)));

    int default_x_1 = randint(2, 99);
    int default_x_2 = randint(2, 99);
    int default_x_3 = randint(2, 99);

    int module_1 = randint(pow(9, 9) + 7, pow(11, 9) + 7);
    while (module_1 % default_x_1 == 0) {
        module_1 = randint(pow(9, 9) + 7, pow(11, 9) + 7);
    }

    int module_2 = randint(pow(9, 9) + 7, pow(11, 9) + 7);
    while (module_2 % default_x_2 == 0) {
        module_2 = randint(pow(9, 9) + 7, pow(11, 9) + 7);
    }

    int module_3 = randint(pow(9, 9) + 7, pow(11, 9) + 7);
    while (module_3 % default_x_3 == 0) {
        module_3 = randint(pow(9, 9) + 7, pow(11, 9) + 7);
    }

    string s;

    // ifstream nameFileout;

    // nameFileout.open("/home/oleg/Documents/algo4/84");
    cin >> s;
    // std::getline(nameFileout, s);

    vector<int> x_ords_1 = precount_x_orders(s, default_x_1, module_1);
    vector<int> x_ords_2 = precount_x_orders(s, default_x_2, module_2);
    vector<int> x_ords_3 = precount_x_orders(s, default_x_3, module_3);

    vector<int> hash_prefs_1 = count_hash_prefixes(s, default_x_1, module_1);
    vector<int> hash_prefs_2 = count_hash_prefixes(s, default_x_2, module_2);
    vector<int> hash_prefs_3 = count_hash_prefixes(s, default_x_3, module_3);

    vector<int> z_func_res(s.size(), 0);

    for (int i = 1; i < s.size(); ++i) {
        bool done = false;

        int l = 1;
        int r = s.size() - i;

        int k = (r + l) / 2;

        if (l == r) {
            int pref_1_begin_id = 0;
            int pref_2_begin_id = i;

            int pref_1_hash_1 = count_substr_hash(hash_prefs_1, pref_1_begin_id, k, x_ords_1, module_1);
            int pref_2_hash_1 = count_substr_hash(hash_prefs_1, pref_2_begin_id, k, x_ords_1, module_1);

            int pref_1_hash_2 = count_substr_hash(hash_prefs_2, pref_1_begin_id, k, x_ords_2, module_2);
            int pref_2_hash_2 = count_substr_hash(hash_prefs_2, pref_2_begin_id, k, x_ords_2, module_2);

            int pref_1_hash_3 = count_substr_hash(hash_prefs_3, pref_1_begin_id, k, x_ords_3, module_3);
            int pref_2_hash_3 = count_substr_hash(hash_prefs_3, pref_2_begin_id, k, x_ords_3, module_3);

            if (pref_1_hash_1 == pref_2_hash_1 || pref_1_hash_2 == pref_2_hash_2 || pref_1_hash_3 == pref_2_hash_3) {
                z_func_res[i] = k;
            }
        }

        while (l < r) {
            if (i + k <= s.size()) {
                int pref_1_begin_id = 0;
                int pref_2_begin_id = i;

                int pref_1_hash_1 = count_substr_hash(hash_prefs_1, pref_1_begin_id, k, x_ords_1, module_1);
                int pref_2_hash_1 = count_substr_hash(hash_prefs_1, pref_2_begin_id, k, x_ords_1, module_1);

                int pref_1_hash_2 = count_substr_hash(hash_prefs_2, pref_1_begin_id, k, x_ords_2, module_2);
                int pref_2_hash_2 = count_substr_hash(hash_prefs_2, pref_2_begin_id, k, x_ords_2, module_2);

                int pref_1_hash_3 = count_substr_hash(hash_prefs_3, pref_1_begin_id, k, x_ords_3, module_3);
                int pref_2_hash_3 = count_substr_hash(hash_prefs_3, pref_2_begin_id, k, x_ords_3, module_3);

                if ((pref_1_hash_1 == pref_2_hash_1) || (pref_1_hash_2 == pref_2_hash_2) || (pref_1_hash_3 == pref_2_hash_3)) {
                    z_func_res[i] = k;
                    l = k;
                    k = (r + l) / 2 + 1;
                } else if (l < r) {
                    if (r - l == 1) {
                        break;
                    }
                    r = k;
                    k = (r + l) / 2;
                }
            } else {
                r = s.size() - i;
                k = (r + l) / 2;
            }
        }
    }

    for (int i = 0; i < z_func_res.size(); ++i) {
        cout << z_func_res[i] << " ";
    }

    return 0;
}
