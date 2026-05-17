class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []

        result = [0] * len(temperatures)

        for i in range(len(temperatures)):
            while stack and temperatures[i] > stack[-1][0]:
                stackT, stackInd = stack.pop()

                result[stackInd] = i - stackInd

            stack.append([temperatures[i], i])

        return result
