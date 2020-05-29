def countSort(word):
    sortedWord = ''
    char_hash = [0]*26
    for char in word:
        char_hash[ord(char)-ord('a')] += 1 
    for i in range(26):
        if char_hash[i]:
            sortedWord += chr(ord('a')+i)*char_hash[i]
    return sortedWord

def groupAnagramWords(strs):
    word_hash_map = dict()
    for word in strs:
        sortedWord = countSort(word)
        if sortedWord in word_hash_map:
            word_hash_map[sortedWord].append(word)
        else:
            word_hash_map[sortedWord] = [word]
    return [word_list for _, word_list in word_hash_map.items()]
print(groupAnagramWords(['abc', 'bcd', 'cba', 'cbd', 'efg']))