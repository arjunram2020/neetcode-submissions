class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:
        order_dict = {}
        for i in range(len(order)):
            order_dict[order[i]] = i 
        for i in range(1, len(words)):
            word1 = words[i-1]
            word2 = words[i]
            j, k = 0,0
            while j<len(word1) and k<len(word2):
                if order_dict[word2[k]] > order_dict[word1[j]]:
                    break
                if order_dict[word2[k]] < order_dict[word1[j]]:
                    return False
                if order_dict[word2[k]] == order_dict[word1[j]]:
                    j+=1
                    k+=1
            if j < len(word1) and k == len(word2):
                return False
        return True
            




