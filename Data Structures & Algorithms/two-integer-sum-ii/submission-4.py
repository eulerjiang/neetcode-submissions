class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        n1, n2 = 0, 0
        for i, num in enumerate(numbers):
            if target - num in numbers and (target - num != num):
                n1, n2 = num, target-num
                break

        index1, index2 = 0, 0
        for i, num in enumerate(numbers):
            if num == n1:
                index1 = i
            if num == n2:
                index2 = i

        return [index1 + 1, index2 + 1]
        
        