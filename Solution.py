class Solution(object):

    def canReach(self, x, y, x2, y2):
        
        while(x2 >= x and y2 >= y):
            if (x2 == x and y2 == y):
                return True
            
            if (x2 > y2):
                if (y2 > y):
                    #x2 %= y2
                    x2 = x2%y2
                else:
                    return (x2 - x) % y == 0
            elif (y2 > x2):
                if (x2 > x):
                    #y2 %= x2
                    y2 = y2%x2
                else:
                    return (y2 - y) % x == 0
            else:
                return False

        return False
    


def main():
    print("Hello World.\n\n")

    solution = Solution()

    print("Solution case 1:     start:  1, 1, end:  3, 5. Solution must be \'Yes\'")
    print(f"Solution:   {solution.canReach(1,1,3,5)}")

    print(f"\n  case 2:     1, 1: Starting in 2, 2. Solution must be \'No\'.")
    print(f'Solution case 2:    {solution.canReach(1, 1, 2, 2)}\n')

    print(f"\n  case 3:     1, 1: Starting in 1, 1. Solution must be \'Yes\'.")
    print(f'Solution case 3:    {solution.canReach(1, 1, 1, 1)}\n')

    print(f"\n  case 4:     10, 2: Starting in 2, 11. Solution must be \'No\'.")
    print(f'Solution case 4:    {solution.canReach(10, 2, 2, 11)}\n')

    print(f"\n  case 5:     10, 4: Starting in 10, 20. Solution must be \'No\'.")
    print(f'Solution case 5:    {solution.canReach(10, 4, 10, 20)}\n')


if __name__ == '__main__':
    main()