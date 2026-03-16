# Day 2: trying to find invalid ID
# Invalidity: sequence of digits repeated twice

# input: "number-number,...,..."
# output: sum of all invalid IDs

class Solution:
    
    def parse_ranges(self, input_str):
        # 解析输入，返回 list of (start, end)
        input_str = input_str.split(",")
        ranges = []
        for range in input_str:
            start, end = range.split("-")
            ranges.append((int(start),int(end)))
        return ranges
    
    def is_invalid(self, n):
        # 判断一个数是否是 invalid ID（某段数字重复两次）
        str_n = str(n)
        len_n = len(str_n)
        if len_n % 2 != 0:
            return False
        else:
            half_len = len_n//2
            first_half = str_n[:half_len]
            second_half = str_n[half_len:]
            return int(first_half) == int(second_half)
    
    def find_invalid_in_range(self, start, end):
        # 找出某个范围内所有 invalid IDs
        invalid_ids = []
        starting = start
        while starting <= end:
            start_len = len(str(starting))
            if (start_len % 2 != 0):
                starting = pow(10, start_len) #made a mistake here due to length of string n should correspond to number 10 to the power of n-1
            else:
                if self.is_invalid(starting):
                    invalid_ids.append(starting)
                starting += 1
        return invalid_ids
    
    def solve(self, input_str):
        # 主逻辑：把所有范围的 invalid IDs 加起来
        ranges = self.parse_ranges(input_str)
        invalid_ids = []
        for range in ranges:
            start = range[0]
            end = range[1]
            invalid_ID = self.find_invalid_in_range(start,end)
            invalid_ids.extend(invalid_ID)
        
        return sum(invalid_ids)
            
            
def main():
    input_str = "12077-25471,4343258-4520548,53-81,43661-93348,6077-11830,2121124544-2121279534,631383-666113,5204516-5270916,411268-591930,783-1147,7575717634-7575795422,8613757494-8613800013,4-19,573518173-573624458,134794-312366,18345305-18402485,109442-132958,59361146-59451093,1171-2793,736409-927243,27424-41933,93-216,22119318-22282041,2854-4778,318142-398442,9477235089-9477417488,679497-734823,28-49,968753-1053291,267179606-267355722,326-780,1533294120-1533349219"
    sol = Solution()
    print(sol.solve(input_str))


if __name__ == "__main__":
    main()