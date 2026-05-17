class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashmap = {}

        for ch in s:
            if ch not in hashmap:
                hashmap[ch] = 1
            else: 
                hashmap[ch] += 1

        for ch in t:
            if ch not in hashmap:
                return False
            else:
                if (hashmap[ch] - 1) < 0:
                    return False
                hashmap[ch] -= 1

        for value in hashmap.values():
            if value != 0:
                return False

        return True

