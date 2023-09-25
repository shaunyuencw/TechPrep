def find_anagrams(s, pattern):
    window_start = 0
    matched = 0
    char_frequency = {}
    result_indices = []

    for char in pattern:
        if char not in char_frequency:
            char_frequency[char] = 0
        char_frequency[char] += 1

    for window_end in range(len(s)):
        if s[window_end] in char_frequency:
            char_frequency[s[window_end]] -= 1
            if char_frequency[s[window_end]] == 0:
                matched += 1

        if matched == len(char_frequency):
            result_indices.append(window_start)

        if window_end >= len(pattern) - 1:
            if s[window_start] in char_frequency:
                if char_frequency[s[window_start]] == 0:
                    matched -= 1
                char_frequency[s[window_start]] += 1
            window_start += 1

    return result_indices
