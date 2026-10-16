def get_longer_word(word1: str, word2: str) -> str:
    # pass
    len_w1 = len(word1)
    len_w2 = len(word2)
    
    if (len_w1 == len_w2):
        return word1
    elif (len_w1 > len_w2):
        # max_len = max(len_w1, len_w2)
        # print(max_len)
        return word1
    else:
        return word2



# do not modify below this line
print(get_longer_word("yellow", "orange"))
print(get_longer_word("red", "blue"))
print(get_longer_word("green", "blue"))
