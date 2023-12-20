# 2.1 A)
def count_unique(input_str):
    input_str = input_str.lower()
    consonants_set = set()
    duplicates_set = set()

    for char in input_str:
        if char.isalpha() and char not in 'aeiou':
            if char in consonants_set:
                duplicates_set.add(char)
            else:
                consonants_set.add(char)

    consonants_set -= duplicates_set
return len(consonants_set)

# 2.1 B)
Time complexity: O(n), where n is the length of the input string.
Space complexity: O(n), where n is the length of the input string.
Assumptions:
The set operations (addition and subtraction) are considered to be constant time on average.



#2.2
  # Non-recursive solution：
def count_squares_non_recursive(X):
    return sum(i**2 for i in range(1, X + 1))

# Recursive solution
def count_squares_recursive(X):
    if X == 0:
        return 0
    else:
        return X**2 + count_squares_recursive(X - 1)
