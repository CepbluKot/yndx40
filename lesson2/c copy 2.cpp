#include <iostream>
#include <vector>
#include <cstdlib>
#include <ctime>
#include <random>


using namespace std;


vector<int> count_hash_prefixes(const string& inp, int x, int module) {
    vector<int> hash_prefixes(inp.length(), 0);

    hash_prefixes[0] = static_cast<int>(inp[0]) % module;
    for (int letter_id = 1; letter_id < inp.length(); ++letter_id) {
        hash_prefixes[letter_id] = (hash_prefixes[letter_id - 1] * x + static_cast<int>(inp[letter_id])) % module;
    }

    return hash_prefixes;
}

vector<int> precount_x_orders(const string& inp, int x, int module) {
    vector<int> precounted(inp.length() + 1, 0);
    precounted[0] = 1;

    for (int order = 1; order <= inp.length(); ++order) {
        precounted[order] = (x * precounted[order - 1]) % module;
    }

    return precounted;
}

int count_substr_hash(const vector<int>& init_hashes, int from_id, int len, const vector<int>& precounted_x, int module) {
    if (from_id > 0) {
        return (init_hashes[from_id + len - 1] - (init_hashes[from_id - 1] * precounted_x[len])) % module;
    } else {
        return init_hashes[from_id + len - 1] % module;
    }
}

int main() {
    std::random_device rd;     // Only used once to initialise (seed) engine
    std::mt19937 rng(rd());    // Random-number engine used (Mersenne-Twister in this case)
    std::uniform_int_distribution<int> uni1(2,300); // Guaranteed unbiased
    std::uniform_int_distribution<long int> uni2(1'000'000'006, 2'000'000'008); // Guaranteed unbiased

    int default_x_1 = 257;
    int default_x_2 = uni1(rng);
    int default_x_3 = uni1(rng);
    int default_x_4 = uni1(rng);
    int default_x_5 = uni1(rng);
    int default_x_6 = uni1(rng);
    int default_x_7 = uni1(rng);
    int default_x_8 = uni1(rng);

    long int module_1 = 1000000000 + 7;
    // long int module_1 = uni2(rng);
    // while (module_1 % default_x_1 == 0) {
    //     module_1 = uni2(rng);
    // }

    long int module_2 = uni2(rng);
    while (module_2 % default_x_2 == 0) {
        module_2 = uni2(rng);
    }

    long int module_3 = uni2(rng);
    while (module_3 % default_x_3 == 0) {
        module_3 = uni2(rng);
    }

    long int module_4 = uni2(rng);
    while (module_4 % default_x_4 == 0) {
        module_4 = uni2(rng);
    }

    long int module_5 = uni2(rng);
    while (module_5 % default_x_5 == 0) {
        module_5 = uni2(rng);
    }

    long int module_6 = uni2(rng);
    while (module_6 % default_x_6 == 0) {
        module_6 = uni2(rng);
    }

    long int module_7 = uni2(rng);
    while (module_7 % default_x_7 == 0) {
        module_7 = uni2(rng);
    }

    long int module_8 = uni2(rng);
    while (module_8 % default_x_8 == 0) {
        module_8 = uni2(rng);
    }

    string s;
    cin >> s;

    vector<int> x_ords_1 = precount_x_orders(s, default_x_1, module_1);
    vector<int> x_ords_2 = precount_x_orders(s, default_x_2, module_2);
    vector<int> x_ords_3 = precount_x_orders(s, default_x_3, module_3);
    vector<int> x_ords_4 = precount_x_orders(s, default_x_4, module_4);
    vector<int> x_ords_5 = precount_x_orders(s, default_x_5, module_5);
    vector<int> x_ords_6 = precount_x_orders(s, default_x_6, module_6);
    vector<int> x_ords_7 = precount_x_orders(s, default_x_7, module_7);
    vector<int> x_ords_8 = precount_x_orders(s, default_x_8, module_8);

    vector<int> hash_prefs_1 = count_hash_prefixes(s, default_x_1, module_1);
    vector<int> hash_prefs_2 = count_hash_prefixes(s, default_x_2, module_2);
    vector<int> hash_prefs_3 = count_hash_prefixes(s, default_x_3, module_3);
    vector<int> hash_prefs_4 = count_hash_prefixes(s, default_x_4, module_4);
    vector<int> hash_prefs_5 = count_hash_prefixes(s, default_x_5, module_5);
    vector<int> hash_prefs_6 = count_hash_prefixes(s, default_x_6, module_6);
    vector<int> hash_prefs_7 = count_hash_prefixes(s, default_x_7, module_7);
    vector<int> hash_prefs_8 = count_hash_prefixes(s, default_x_8, module_8);

    vector<int> z_func_res(s.length(), 0);

    for (int i = 1; i < s.length(); ++i) {
        bool done = false;

        int l = 1;
        int r = s.length() - i;

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

            int pref_1_hash_4 = count_substr_hash(hash_prefs_4, pref_1_begin_id, k, x_ords_4, module_4);
            int pref_2_hash_4 = count_substr_hash(hash_prefs_4, pref_2_begin_id, k, x_ords_4, module_4);

            int pref_1_hash_5 = count_substr_hash(hash_prefs_5, pref_1_begin_id, k, x_ords_5, module_5);
            int pref_2_hash_5 = count_substr_hash(hash_prefs_5, pref_2_begin_id, k, x_ords_5, module_5);

            int pref_1_hash_6 = count_substr_hash(hash_prefs_6, pref_1_begin_id, k, x_ords_6, module_6);
            int pref_2_hash_6 = count_substr_hash(hash_prefs_6, pref_2_begin_id, k, x_ords_6, module_6);

            int pref_1_hash_7 = count_substr_hash(hash_prefs_7, pref_1_begin_id, k, x_ords_7, module_7);
            int pref_2_hash_7 = count_substr_hash(hash_prefs_7, pref_2_begin_id, k, x_ords_7, module_7);

            int pref_1_hash_8 = count_substr_hash(hash_prefs_8, pref_1_begin_id, k, x_ords_8, module_8);
            int pref_2_hash_8 = count_substr_hash(hash_prefs_8, pref_2_begin_id, k, x_ords_8, module_8);


            if ((pref_1_hash_1 == pref_2_hash_1) || (pref_1_hash_2 == pref_2_hash_2) || (pref_1_hash_3 == pref_2_hash_3) || (pref_1_hash_4 == pref_2_hash_4) || (pref_1_hash_5 == pref_2_hash_5) || (pref_1_hash_6 == pref_2_hash_6) || (pref_1_hash_7 == pref_2_hash_7) || (pref_1_hash_8 == pref_2_hash_8)) {
                z_func_res[i] = k;
            }
        }

        while (l < r) {
            if (i + k <= s.length()) {
                int pref_1_begin_id = 0;
                int pref_2_begin_id = i;

                int pref_1_hash_1 = count_substr_hash(hash_prefs_1, pref_1_begin_id, k, x_ords_1, module_1);
                int pref_2_hash_1 = count_substr_hash(hash_prefs_1, pref_2_begin_id, k, x_ords_1, module_1);

                int pref_1_hash_2 = count_substr_hash(hash_prefs_2, pref_1_begin_id, k, x_ords_2, module_2);
                int pref_2_hash_2 = count_substr_hash(hash_prefs_2, pref_2_begin_id, k, x_ords_2, module_2);

                int pref_1_hash_3 = count_substr_hash(hash_prefs_3, pref_1_begin_id, k, x_ords_3, module_3);
                int pref_2_hash_3 = count_substr_hash(hash_prefs_3, pref_2_begin_id, k, x_ords_3, module_3);

                int pref_1_hash_4 = count_substr_hash(hash_prefs_4, pref_1_begin_id, k, x_ords_4, module_4);
                int pref_2_hash_4 = count_substr_hash(hash_prefs_4, pref_2_begin_id, k, x_ords_4, module_4);

                int pref_1_hash_5 = count_substr_hash(hash_prefs_5, pref_1_begin_id, k, x_ords_5, module_5);
                int pref_2_hash_5 = count_substr_hash(hash_prefs_5, pref_2_begin_id, k, x_ords_5, module_5);

                int pref_1_hash_6 = count_substr_hash(hash_prefs_6, pref_1_begin_id, k, x_ords_6, module_6);
                int pref_2_hash_6 = count_substr_hash(hash_prefs_6, pref_2_begin_id, k, x_ords_6, module_6);

                int pref_1_hash_7 = count_substr_hash(hash_prefs_7, pref_1_begin_id, k, x_ords_7, module_7);
                int pref_2_hash_7 = count_substr_hash(hash_prefs_7, pref_2_begin_id, k, x_ords_7, module_7);

                int pref_1_hash_8 = count_substr_hash(hash_prefs_8, pref_1_begin_id, k, x_ords_8, module_8);
                int pref_2_hash_8 = count_substr_hash(hash_prefs_8, pref_2_begin_id, k, x_ords_8, module_8);

                if ((pref_1_hash_1 == pref_2_hash_1) || (pref_1_hash_2 == pref_2_hash_2) || (pref_1_hash_3 == pref_2_hash_3) || (pref_1_hash_4 == pref_2_hash_4) || (pref_1_hash_5 == pref_2_hash_5) || (pref_1_hash_6 == pref_2_hash_6) || (pref_1_hash_7 == pref_2_hash_7) || (pref_1_hash_8 == pref_2_hash_8) &&  (l < r)) {
                    z_func_res[i] = k;
                    l = k;
                    k = (r + l) / 2 + 1;
                } else if (l < r) {
                    if ((r - l )== 1) {
                        break;
                    }
                    r = k;
                    k = (r + l) / 2;
                }
            } else {
                r = s.length() - i;
                k = (r + l) / 2;
            }
        }
    }

    for (int res = 0; res < z_func_res.size()-1; res++)
        std::cout << z_func_res[res] << " ";
    std::cout << z_func_res.back();

    return 0;
}
