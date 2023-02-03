def new_line():
    print('\n')
new_line()
#Unique strings in an array:
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
         stack = [] #[char, count]
         
         for c in s:
             if stack and stack[-1][0] == c:
                 stack[-1][1] += 1
             else:
                stack.append([c, 1])
             if stack[-1][1] == k:
                stack.pop()
         res =""
         for char, count in stack:
             res +=(char * count)
         return res
charact = Solution()
print(charact.removeDuplicates('acbbbccaa', 3))
print(charact.removeDuplicates('acbbbccaae', 3))
new_line()

#132pattern
