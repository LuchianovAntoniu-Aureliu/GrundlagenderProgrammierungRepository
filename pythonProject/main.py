def swap(word):
    new_word = ''
    j=len(word)-1
    vok='aeiou'
    for i in range(len(word)):
        if word[i] not in vok:
            new_word += word[i]
        else:
            while j > len(word)//2:
                if word[j] in vok:
                    new_word += word[j]
                    j -= 1
                    break
                j -= 1

    return new_word

print(swap('terminator'))