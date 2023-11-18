def is_nice(s):
    vowels = "aeiou"
    num_vowels = sum(1 for char in s if char in vowels)

    double_letter = any(s[i] == s[i+1] for i in range(len(s) - 1))

    forbidden = ['ab', 'cd', 'pq', 'xy']
    contains_forbidden = any(sub in s for sub in forbidden)

    return num_vowels >= 3 and double_letter and not contains_forbidden

def count_nice_strings_in_file(file_path):
    with open(file_path, 'r') as file:
        strings = file.readlines()
    return sum(1 for s in strings if is_nice(s.strip()))

file_path = 'list.txt'

count = count_nice_strings_in_file(file_path)
print(count)