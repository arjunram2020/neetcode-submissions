class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #dictionary of strings
        output = []
        dict = {}
        for st in strs:
            if str(sorted(st)) in dict:
                dict[str(sorted(st))].append(st)
            if str(sorted(st)) not in dict:
                dict[str(sorted(st))] = [st]
        for dic in dict:
            output.append(dict[dic])
        return output

