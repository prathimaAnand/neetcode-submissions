from typing import List

def count_unique_words(words: List[str]) -> int:
    my_set = set(words)

    if len(words) == 0:
        return 0

    output = 0
    for ele in my_set:
        output += 1
    return output
    

# do not modify code below this line
print(count_unique_words(["hello", "world", "hello", "goodbye"]))
print(count_unique_words(["hello", "world", "i", "am", "world"]))
print(count_unique_words(["hello", "hello", "hello"]))
print(count_unique_words([]))
