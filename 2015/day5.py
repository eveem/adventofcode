import re

vowels = 'aeiou'
deny = ['ab', 'cd', 'pq', 'xy']
double_pattern = re.compile(r'(.)\1')

def count_vowel(s):
    return sum(s.count(vowel) for vowel in vowels)

def check_string(s):
    vowel_count = count_vowel(s)
    double_count = re.findall(double_pattern, s)

    if vowel_count >= 3 and len(double_count) > 0:
        for i in deny:
            if i in s:
                if i == 'ab' and 'aab' in s:
                    return True
                return False
        return True

def find_small_palindrome(s):
    l = len(s)
    for i in range(l - 2):
        if s[i] == s[i + 2]:
            return True
    return False

def find_same_substring(s):
    l = len(s)
    for i in range(l - 1):
        for j in range(1, l - 1):
            if s[i] == s[j] and s[i + 1] == s[j + 1] and i != j and abs(i - j) > 1:
                # print(i, j, s[i], s[i + 1], s[j], s[j + 1], s)
                return True
    return False

s = open('input.txt', 'r')
r = 0

for i in s.readlines():
    temp = i.replace('\n', '')
    if find_small_palindrome(temp) and find_same_substring(temp):
        r += 1

print(r)
