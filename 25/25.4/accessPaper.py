# Day 4: give rolls of paper can be accessed by forklift
# Accessible: fewer than 4 rolls of paper in the eight adjacent position

# input: string 
# e.g:
# ..@@.@@@@.
# @@@.@.@.@@
# @@@@@.@.@@
# output: int num of accessible papers

class Solution:
    
    def parse_inputs(self, input_str):
        # 解析输入，返回 list of row of indicators of empty place(.) or roll of paper(@)
        distribution = input_str.split("\n")
        return distribution
    
    def find_num_of_papers(self, distribution):
        # find num of accessible of paper
        n_accessible_rolls = 0
        len_grid = len(distribution[0])
        height_grid = len(distribution)
        for i in range(height_grid):
            for j in range(len_grid):
                if distribution[i][j] != '@':
                    continue
                if i == 0:
                    if (j == 0 or j == len_grid - 1):
                        # on the corners, skip
                        n_accessible_rolls += 1
                    else:
                        # upmost line
                        adjacent_things = distribution[i][j-1] + distribution[i][j+1] + distribution[i+1][j-1] + distribution[i+1][j] + distribution[i+1][j+1]
                        if adjacent_things.count('@') < 4:
                            n_accessible_rolls += 1
                elif i == height_grid-1:
                    if (j == 0 or j == len_grid - 1):
                        # on the corners, skip
                        n_accessible_rolls += 1
                    else:
                        # downmost line
                        adjacent_things = distribution[i][j-1] + distribution[i][j+1] + distribution[i-1][j-1] + distribution[i-1][j] + distribution[i-1][j+1]
                        if adjacent_things.count('@') < 4:
                            n_accessible_rolls += 1
                elif j == 0:
                    # leftmost line
                    adjacent_things = distribution[i][j+1] + distribution[i+1][j+1] + distribution[i+1][j] + distribution[i-1][j] + distribution[i-1][j+1]
                    if adjacent_things.count('@') < 4:
                            n_accessible_rolls += 1
                elif j == len_grid - 1:
                    # rightmost line
                    adjacent_things = distribution[i][j-1] + distribution[i-1][j-1] + distribution[i-1][j] + distribution[i+1][j-1] + distribution[i+1][j]
                    if adjacent_things.count('@') < 4:
                            n_accessible_rolls += 1
                else:
                    adjacent_things = distribution[i-1][j-1] + distribution[i-1][j] + distribution[i-1][j+1] + distribution[i][j-1] + distribution[i][j+1] + distribution[i+1][j-1] + distribution[i+1][j] + distribution[i+1][j+1]
                    if adjacent_things.count('@') < 4:
                            n_accessible_rolls += 1
        return n_accessible_rolls

    def solve(self, input_str):
        # 主逻辑：把所有范围的 加起来
        distribution = self.parse_inputs(input_str)
        accessible_papers = self.find_num_of_papers(distribution)
        return accessible_papers
            
def main():
    # example input
    # input_str = "..@@.@@@@.\n@@@.@.@.@@\n@@@@@.@.@@\n@.@@@@..@.\n@@.@@@@.@@\n.@@@@@@@.@\n.@.@.@.@@@\n@.@@@.@@@@\n.@@@@@@@@.\n@.@.@@@.@."
    # puzzle input
    input_str = open("/Users/ames/Documents/GitHub/Advent-of-code-challenge/25/25.4/input.txt").read().strip()
    sol = Solution()
    print(sol.solve(input_str))

if __name__ == "__main__":
    main()