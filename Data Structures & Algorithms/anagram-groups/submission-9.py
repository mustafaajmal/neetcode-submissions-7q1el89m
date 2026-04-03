from collections import Counter, defaultdict

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = defaultdict(list)
        for word in strs:
            word_frequency = tuple(sorted(Counter(word).items()))
            anagrams[word_frequency].append(word)
        anagrams_list = []
        for value in anagrams.values():
            anagrams_list.append(value)
        return anagrams_list