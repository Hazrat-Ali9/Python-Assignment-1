def split_balanced_string(S):
    count = 0
    balanced_strings = []
    curr_count_L = 0
    curr_count_R = 0

    for char in S:
        if char == 'L':
            curr_count_L += 1
        elif char == 'R':
            curr_count_R += 1

        if curr_count_L == curr_count_R:
            balanced_strings.append(S[:curr_count_L + curr_count_R])
            count += 1
            S = S[curr_count_L + curr_count_R:]
            curr_count_L = 0
            curr_count_R = 0

    return count, balanced_strings

S = input().strip()
count, balanced_strings = split_balanced_string(S)
print(count)
for string in balanced_strings:
    print(string)