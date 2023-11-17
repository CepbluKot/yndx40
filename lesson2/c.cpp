#include <iostream>
#include <vector>
#include <fstream>

using namespace std;

const int default_x_1 = 257;
const int module_1 = 1000000007;

vector<int> count_hash_prefixes(const string& inp, int x, int module) {
    vector<int> hash_prefixes(inp.length(), 0);

    hash_prefixes[0] = (char)inp[0] % module;
    for (int letter_id = 1; letter_id < inp.length(); ++letter_id) {
        hash_prefixes[letter_id] = (hash_prefixes[letter_id-1] * x + inp[letter_id]) % module;
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
        return (init_hashes[from_id + len - 1] - (init_hashes[from_id - 1] * precounted_x[len]) % module + module) % module;
    } else {
        return init_hashes[from_id + len - 1] % module;
    }
}

int main() {
    // freopen("84", "r", stdin); // Open the file '84' for reading
    ifstream nameFileout;

    nameFileout.open("input.txt");

    string s;
    // cin >> s;
    std::getline(nameFileout, s);

    vector<int> x_ords_1 = precount_x_orders(s, default_x_1, module_1);
    vector<int> hash_prefs_1 = count_hash_prefixes(s, default_x_1, module_1);

    vector<int> z_func_res(s.length(), 0);

    for (int i = 1; i < s.length(); ++i) {
        int l = 1;
        int r = s.length() - i;
        int k = (r + l) / 2;

        if (l == r) {
            int pref_1_begin_id = 0;
            int pref_2_begin_id = i;

            int pref_1_hash_1 = count_substr_hash(hash_prefs_1, pref_1_begin_id, k, x_ords_1, module_1);
            int pref_2_hash_1 = count_substr_hash(hash_prefs_1, pref_2_begin_id, k, x_ords_1, module_1);

            if (pref_1_hash_1 == pref_2_hash_1) {
                z_func_res[i] = k;
            }
        }

        while (l < r) {
            if (i + k <= s.length()) {
                int pref_1_begin_id = 0;
                int pref_2_begin_id = i;

                int pref_1_hash_1 = count_substr_hash(hash_prefs_1, pref_1_begin_id, k, x_ords_1, module_1);
                int pref_2_hash_1 = count_substr_hash(hash_prefs_1, pref_2_begin_id, k, x_ords_1, module_1);

                if (pref_1_hash_1 == pref_2_hash_1) {
                    z_func_res[i] = k;
                    l = k;
                    k = (r + l) / 2 + 1;
                } else {
                    if (r - l == 1) {
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

    for (int i = 0; i < s.length(); ++i) {
        cout << z_func_res[i] << " ";
    }

    return 0;
}
