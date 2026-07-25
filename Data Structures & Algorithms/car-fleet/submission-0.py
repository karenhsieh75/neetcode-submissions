class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        pair = [[p, s] for p, s in zip(position, speed)]
        stack = [] # store the time when arrive target

        pair.sort()
        pair.reverse() # iterate backward
        for p, s in pair:
            if stack and (target - p) / s <= stack[-1]:
                continue
            else:
                stack.append((target - p) / s)
            
        return len(stack)
            
