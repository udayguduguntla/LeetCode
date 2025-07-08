class Solution:
    def compareVersion(self, version1: str, version2: str) -> int:
        v1 = list(map(int,version1.split(".")))
        v2 = list(map(int,version2.split(".")))

        lenv1, lenv2 = len(v1),len(v2)
        if lenv1 < lenv2:  v1.extend([0] * (lenv2 - lenv1))
        elif lenv1 > lenv2:  v2.extend([0] * (lenv1 - lenv2))

        for i in range(len(v1)):
            if v1[i] < v2[i]: return -1
            elif v2[i] < v1[i]: return 1
        return 0