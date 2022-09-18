class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        dictlist = []
        for x in range(len(strs)):
            d = dict()
            word = strs[x]
            for n in range(len(word)):
                if word[n] in d:
                    d[word[n]] += 1
                else:
                    d[word[n]] = 1
            dictlist.append(d)
        output = []
        match = []
        for x in range(len(dictlist)):
            flag = False
            for n in range(len(match)):
                if match[n][0] == dictlist[x]:
                    match[n].append(dictlist[x])
                    output[n].append(strs[x])
                    flag = True
            
            if not flag:
                output.append([strs[x]])
                match.append([dictlist[x]])
        return output