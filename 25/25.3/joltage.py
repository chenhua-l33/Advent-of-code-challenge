# Day 3: trying to find largest two digits as joltage
# Invalidity: sequence of digits repeated twice

# input: 
# number
# number,
# ...,
# ...
# output: sum of all joltages

class Solution:
    
    def parse_inputs(self, powers):
        # 解析输入，返回 list of numbers(string?)
        powers = powers.split("/n")
        return powers
    
    def find_max_joltage(self, power):
        # 对一个数字找到最大的joltage
        # power in powers as a string
        len_power = len(power)
        left = 0
        max_left = power[0]

        right = len_power - 1
        max_right = power[right]

        left_max_th = 0
        right_max_th = right
        while left_max_th < right_max_th and left <= len_power-2 and right >= 2:
            left += 1
            right -= 1
            if power[left] > max_left:
                max_left = power[left]
                left_max_th = left
            if power[right] > max_right:
                max_right = power[right]
                right_max_th = right
        return int(max_left+max_right)
    
    def solve(self, powers):
        # 主逻辑：把所有范围的 joltage 加起来
        powers = self.parse_inputs(powers)
        max_joltages = []
        for power in powers:
            max_joltages.append(self.find_max_joltage(power))
        print(max_joltages)
        return sum(max_joltages)
            
def main():
    input_str = "987654321111111/n811111111111119/n234234234234278/n818181911112111"
    sol = Solution()
    print(sol.solve(input_str))

if __name__ == "__main__":
    main()