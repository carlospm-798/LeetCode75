class Solution(object):

    def canReach(self, x1, y1, x2, y2):
        visited = set()

        def dfs(x, y):
            if (x, y) in visited:
                return False
            if x > x2 or y > y2:
                return False
            if x == x2 and y == y2:
                return True

            visited.add((x, y))
            return dfs(x + y, y) or dfs(x, x + y)

        return "Yes" if dfs(x1, y1) else "No"


def main():
    print("Hello World.\n")

    solution = Solution()

    print(f"\n  case 1:     1, 1: Starting in 3, 5. Solution must be \'Yes\'.")
    print(f'Solution case 1:    {solution.canReach(1, 1, 3, 5)}\n')

    print(f"\n  case 1:     1, 1: Starting in 2, 2. Solution must be \'No\'.")
    print(f'Solution case 1:    {solution.canReach(1, 1, 2, 2)}\n')

    print(f"\n  case 1:     1, 1: Starting in 3, 5. Solution must be \'Yes\'.")
    print(f'Solution case 1:    {solution.canReach(1, 1, 1, 1)}\n')

if __name__ == '__main__':
    main()

#   This time complexity is high:       O(2^(X2+Y2))