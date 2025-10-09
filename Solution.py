class Solution(object):
    def mergeAlternately(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: str
        """
        return word1 + word2

def main():
    word1 = input("input word1:     \n")
    word2 = input("input word2:     \n")

    solution = Solution()

    print(f"Solution:    {solution.mergeAlternately(word1, word2)}")


if __name__ == '__main__':
    main()