class Solution(object):

    def canReach(self, x, y, x2, y2):
        current = Node(x2, y2)
        path = [current]

        while current.x >= x and current.y >= y:
            if current.x == x and current.y == y:
                return True

            if current.x > current.y:
                new_x = current.x - current.y
                new_y = current.y
            elif current.y > current.x:
                new_x = current.x
                new_y = current.y - current.x
            else:
                break

            parent = Node(new_x, new_y, parent=current)
            path.append(parent)
            current = parent

        return False

class Node:
    def __init__(self, x, y, parent=None):
        self.x = x
        self.y = y
        self.parent = parent
    


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

#   This time complexity is high:       O(Max(X2,Y2))