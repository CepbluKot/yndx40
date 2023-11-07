#include <iostream>
#include <fstream>
#include <vector>
#include <ctime>
#include <cstdlib>
#include <algorithm>


std::vector<int> arr;

int make_partition(int x, int begin, int end)
{
    if (end == -1)
    {
        end = arr.size() - 1;
    }

    if (arr.size() >= 2)
    {
        int begin_equals_id = -1;
        int begin_greater_id = -1;
        int curr_elem_id = begin + 1;

        while (curr_elem_id <= end)
        {
            int first_elem = arr[begin];
            int curr_elem = arr[curr_elem_id];
            int prev_elem = arr[curr_elem_id - 1];

            if (first_elem < x)
            {
                if ((prev_elem < x && curr_elem < x) || (prev_elem == x && curr_elem == x) || (prev_elem > x && curr_elem > x))
                {
                    curr_elem_id++;
                    continue;
                }

                if (prev_elem < x && curr_elem == x)
                {
                    begin_equals_id = curr_elem_id;
                    curr_elem_id++;
                    continue;
                }

                if ((prev_elem == x && curr_elem > x) || (prev_elem < x && curr_elem > x))
                {
                    begin_greater_id = curr_elem_id;
                    curr_elem_id++;
                    continue;
                }

                if (prev_elem > x && first_elem < x && curr_elem < x && begin_equals_id != -1 && begin_greater_id != -1)
                {
                    int equals_elem = arr[begin_equals_id];
                    int greater_elem = arr[begin_greater_id];

                    arr[begin_equals_id] = curr_elem;
                    arr[begin_greater_id] = equals_elem;
                    arr[curr_elem_id] = greater_elem;

                    begin_equals_id++;
                    begin_greater_id++;
                    curr_elem_id++;
                    continue;
                }

                if (prev_elem > x && first_elem < x && curr_elem == x && begin_greater_id != -1)
                {
                    std::swap(arr[begin_greater_id], arr[curr_elem_id]);

                    if (begin_equals_id == -1)
                    {
                        begin_equals_id = begin_greater_id;
                    }

                    begin_greater_id++;
                    curr_elem_id++;
                    continue;
                }

                if (prev_elem > x && first_elem < x && curr_elem < x && begin_greater_id != -1 && begin_equals_id == -1)
                {
                    std::swap(arr[begin_greater_id], arr[curr_elem_id]);

                    begin_greater_id++;
                    curr_elem_id++;
                    continue;
                }

                if (prev_elem > x && first_elem < x && curr_elem == x && begin_greater_id != -1)
                {
                    std::swap(arr[begin_greater_id], arr[curr_elem_id]);

                    if (begin_equals_id == -1)
                    {
                        begin_equals_id = begin_greater_id;
                    }

                    begin_greater_id++;
                    curr_elem_id++;
                    continue;
                }

                if (prev_elem == x && first_elem < x && curr_elem < x && begin_equals_id != -1)
                {
                    std::swap(arr[begin_equals_id], arr[curr_elem_id]);

                    if (begin_greater_id == -1)
                    {
                        begin_greater_id = begin_equals_id;
                    }

                    begin_equals_id++;
                    curr_elem_id++;
                    continue;
                }
            }
            else if (first_elem == x)
            {
                begin_equals_id = begin;

                if ((prev_elem == x && curr_elem == x) || (prev_elem > x && curr_elem > x))
                {
                    curr_elem_id++;
                    continue;
                }

                if (prev_elem == x && curr_elem > x)
                {
                    begin_greater_id = curr_elem_id;
                    curr_elem_id++;
                    continue;
                }

                if (prev_elem > x && curr_elem < x && begin_greater_id != -1 && begin_equals_id != -1)
                {
                    int equals_elem = arr[begin_equals_id];
                    int greater_elem = arr[begin_greater_id];

                    arr[begin_equals_id] = curr_elem;
                    arr[curr_elem_id] = greater_elem;
                    arr[begin_greater_id] = equals_elem;

                    begin_greater_id++;
                    begin_equals_id++;
                    curr_elem_id++;
                    continue;
                }

                if (prev_elem > x && curr_elem == x && begin_greater_id != -1)
                {
                    std::swap(arr[curr_elem_id], arr[begin_greater_id]);

                    begin_greater_id++;
                    curr_elem_id++;
                    continue;
                }

                if (prev_elem == x && curr_elem < x && begin_equals_id != -1)
                {
                    std::swap(arr[curr_elem_id], arr[begin_equals_id]);

                    if (begin_greater_id == -1)
                    {
                        begin_greater_id = begin_equals_id;
                    }

                    begin_equals_id++;
                    curr_elem_id++;
                    continue;
                }
            }
            else
            {
                begin_greater_id = begin;

                if (prev_elem > x && curr_elem > x)
                {
                    curr_elem_id++;
                    continue;
                }

                if ((prev_elem > x && curr_elem == x && begin_greater_id != -1) || (prev_elem > x && curr_elem < x && begin_greater_id != -1))
                {
                    std::swap(arr[curr_elem_id], arr[begin_greater_id]);

                    if (begin_equals_id == -1 && curr_elem == x)
                    {
                        begin_equals_id = begin_greater_id;
                    }

                    begin_greater_id++;
                    curr_elem_id++;
                    continue;
                }
            }
        }

        if (begin_equals_id != -1 && begin_greater_id != -1)
        {
            return begin_equals_id;
        }
        else if (begin_equals_id != -1)
        {
            return begin_equals_id;
        }
        else if (begin_greater_id != -1)
        {
            return begin_greater_id;
        }
        else
        {
            return arr.size();
        }
    }
    else
    {
        if (arr[0] < x)
        {
            return 1;
        }
        else
        {
            return 0;
        }
    }
}

void fast_sort(int begin, int end)
{
    if (begin < end)
    {
        int supp_elem = arr[std::rand()%((end - begin) + 1) + begin];
        int smaller_part_end_id = make_partition(supp_elem, begin, end);
        fast_sort(begin, smaller_part_end_id - 1);
        fast_sort(smaller_part_end_id + 1, end);
    }
}

int main()
{
    std::ifstream input("input.txt");
    int n;
    input >> n;
    arr.resize(n);
    for (int i = 0; i < n; i++)
    {
        input >> arr[i];
    }
    input.close();

    if (!std::is_sorted(arr.begin(), arr.end()))
    {
        fast_sort(0, arr.size() - 1);
    }

    
        std::ofstream output("output.txt");
        for (int i = 0; i < arr.size(); i++)
        {
            output << arr[i] << " ";
        }
        output.close();

    

    return 0;
}
