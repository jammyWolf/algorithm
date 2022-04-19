def mostCommonWord(paragraph, banned) -> str:
    paragraph = paragraph.lower()
    if paragraph[-1]>='a' and paragraph[-1]<='z':
        paragraph = paragraph+'.'
    word_dict = {}
    ret = ""
    word = ""
    max_count = 0
    for s in paragraph:
        if s>='a' and s<='z':
            word += s

        else:
            if word not in banned and word!='':
                try:
                    word_dict[word] = word_dict[word] + 1
                except:
                    word_dict[word] = 1

                if max_count < word_dict[word]:
                    ret = word
                    max_count = word_dict[word]
            word = ""

    # ret = word_dict[word] if word_dict else ret
    return ret

    


p = "Bob hit a ball, the hit BALL flew far after it was hit."
b = ["hit"]
p = "Bob"
b = []
a = mostCommonWord(p, b)
print(a)