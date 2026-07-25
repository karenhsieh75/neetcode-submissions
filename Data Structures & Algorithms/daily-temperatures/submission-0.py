class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        index_stack = []
        result = [0] * len(temperatures)

        stack.append(temperatures[0])
        index_stack.append(0)

        for i in range(1, len(temperatures)):

            while stack and stack[-1] < temperatures[i]:
                stack.pop()
                index = index_stack.pop()
                result[index] = i - index
            
            stack.append(temperatures[i])
            index_stack.append(i)
        
        return result

        [38,30]
        i = 3
        days = 1
        [1,0,1,0,0,0,0]
                    