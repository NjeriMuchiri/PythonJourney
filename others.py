def new_line():
    print('\n')
new_line()
# rotating the list of numbers by 3:
nums = [1,2,3,4,5,6,7]
k = 3
nums = (nums[len(nums) - k:len(nums)]) + nums[0: len(nums) - k]
print(nums)
new_line()
# #by 2
# numbs = [-1,-100,3,99]
# k = 2
# numbs = (numbs[len(numbs) - k:len(numbs)]) + numbs[0: len(numbs) - k]
# print(numbs)


A = [34,23,1,24,75,33,54,8]
K = 60
# class Solution:
#     def twoSumlessThank(self, A: list[int], k:int) -> int:
#         A = sorted(A)
#         i = 0
#         j = len(A) - 1
        
#         S = -1
        
#         while i < j:
#             if A[i] + A[j] < K:
#                 S = max(S, A[i] + A[j])
#                 i += 1
#             else:
#                 j -= 1
#         return S
# sum1 = Solution()
# print(sum1.twoSumlessThank([34,23,1,24,75,33,54,8], 60))    
# print(sum1.twoSumlessThank([10,20,30], 15))  
       
new_line()
class Summin:
    def twoSumless(self, A, K):
        S = -1
        if len(A) == 1:
            return -1
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                temp = A[i] + A[j]
                if temp < K:
                    S = max(S,temp)
        return S
ob1 = Summin()
print(ob1.twoSumless([34,23,1,24,75,33,54,8], 60)) 
print(ob1.twoSumless([10,20,30], 15))  

new_line()
#turing solutions below for a max sum of numbers
class Summin:
    def twoSumless(self, A, K):
        A = [34,23,1,24,75,33,54,8]
        K = 60
        S = -1
        if len(A) == 1:
            return -1
        for i in range(len(A)):
            for j in range(i + 1, len(A)):
                temp = A[i] + A[j]
                if temp < K:
                    S = max(S,temp)
        return S
ob1 = Summin()
print(ob1.twoSumless([A], K)) 
# print(ob1.twoSumless([10,20,30], 15)) 
new_line()     
# finding the lucky integer in an array #turing
class Solution:
    def findLucky(self,arr:list[int])->int:
         myDict = {}
         arrLen = len(arr)
         for i in range(len(arr)):
            if arr[i] <= arrLen:
              myDict[arr[i]] = myDict.get(arr[i], 0) + 1
         defaultReturnVal = -1
         for key,value in myDict.items():
             if key == value and key > defaultReturnVal:
                 defaultReturnVal = key
         return defaultReturnVal
     
obj1 = Solution()
print(obj1.findLucky([2,2,3,4]))
print(obj1.findLucky([1,2,2,3,3,3]))
print(obj1.findLucky([2,2,2,3,3]))
print(obj1.findLucky([5]))
print(obj1.findLucky([7,7,7,7,7,7]))
new_line()

#turing baseball game
class Solution:
    def calPoints(self, ops: list[str]) -> int:
        
        stack = []
        
        for op in ops:
            if op == "+":
                stack.append(stack[-1] + stack[-2])
            
            elif op == "D":
                  stack.append(2 * stack[-1])
            elif op == "C":
                  stack.pop()
            else:
                  stack.append(int(op))
        return sum(stack)
baseball = Solution()
print(baseball.calPoints(["5","2","C","D","+"]))

new_line()








        







