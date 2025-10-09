'''class Solution(object):
    def mergeAlternately(self, word1, word2):
        
        #It starts with the word1, and then goes with word2
        solution = ''
        size1 = len(word1)
        size2 = len(word2)
        
        for i in range(min(size1, size2)):
            solution += word1[i] + word2[i]
        
        if size2 > size1:
            solution += word2[size1:]
        elif size1 > size2:
            solution += word1[size2:]
        else:
            pass
        #if the word2 is bigger than word1, the final letters
        #will go till the end

        return solution'''
class Solution(object):
    def mergeAlternately(self, word1, word2):
        m = len(word1)
        n = len(word2)
        i = 0
        j = 0
        result = []

        while i < m or j < n:
            if i < m:
                result += word1[i]
                i += 1
            if j < n:
                result += word2[j]
                j += 1

        return "".join(result)


def main():
    word1 = input("input word1:     \n")
    word2 = input("input word2:     \n")

    solution = Solution()

    print(f"Solution:    {solution.mergeAlternately(word1, word2)}")


if __name__ == '__main__':
    main()