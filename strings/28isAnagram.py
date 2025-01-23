class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        mapp = {}
        mapp2 = {}

        for c in s:
            mapp[c] = mapp.get(c, 0) + 1

        for c in t:
            mapp2[c] = mapp2.get(c, 0) + 1

        if mapp == mapp2:
            return True

        return False 