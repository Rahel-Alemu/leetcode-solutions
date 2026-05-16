class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        wordSet = set(wordList)
        if endWord not in wordSet:
            return 0
            
        beginSet = {beginWord}
        endSet = {endWord}
        length = 1
        
        while beginSet and endSet:
            if len(beginSet) > len(endSet):
                beginSet, endSet = endSet, beginSet
                
            nextSet = set()
            for word in beginSet:
                for i in range(len(word)):
                    for c in 'abcdefghijklmnopqrstuvwxyz':
                        if c == word[i]:
                            continue
                        next_word = word[:i] + c + word[i+1:]
                        
                        if next_word in endSet:
                            return length + 1
                        if next_word in wordSet:
                            wordSet.remove(next_word)
                            nextSet.add(next_word)
                            
            beginSet = nextSet
            length += 1
            
        return 0