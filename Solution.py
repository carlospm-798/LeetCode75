import re

class Solution(object):
    def gcdOfStrings(self, str1, str2):
        """
        :type str1: str
        :type str2: str
        :rtype: str
        """
        #First I need to identify the shortest str
        shortest = min((str1, str2), key=len)

        #Now, I need to divide the shortest string by 1 element at time
        #and recreate a substring that match with itself.
        #But, in case that the string don't repeat any letter, we omite
        #this process
        if re.search("(.)\1", shortest):
            print(f'There\'s repeated character in {shortest}')


        return shortest

def main():
    str1 = input("str1:     \n")
    str2 = input("str2:     \n")

    solution = Solution()

    print(f"Solution:       {solution.gcdOfStrings(str1, str2)}\n")


if __name__ == '__main__':
    main()