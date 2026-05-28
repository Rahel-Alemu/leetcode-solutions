class Solution(object):
    def stringIndices(self, wordsContainer, wordsQuery):
        lengths = [len(w) for w in wordsContainer]
        
        trie_best = [-1]
        trie_children = [{}]
        
        for i, word in enumerate(wordsContainer):
            curr = 0
            length = lengths[i]
            
            if trie_best[0] == -1 or length < lengths[trie_best[0]]:
                trie_best[0] = i
                
            for char in reversed(word):
                if char not in trie_children[curr]:
                    new_node = len(trie_best)
                    trie_best.append(i)
                    trie_children.append({})
                    trie_children[curr][char] = new_node
                    curr = new_node
                else:
                    curr = trie_children[curr][char]
                    if length < lengths[trie_best[curr]]:
                        trie_best[curr] = i
                        
        ans = []
        for query in wordsQuery:
            curr = 0
            for char in reversed(query):
                if char in trie_children[curr]:
                    curr = trie_children[curr][char]
                else:
                    break
            ans.append(trie_best[curr])
            
        return ans