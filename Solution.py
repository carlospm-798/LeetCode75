class Solution(object):
    def mergeAlternately(self, word1, word2):
        
        #It starts with the word1, and then goes with word2
        solution = ''
        size1 = len(word1)
        size2 = len(word2)
        
        for i in range(min(size1, size2)):
            solution += word1[i] + word2[i]
        '''
        if len(word2) > size:
            solution += word2[size:]'''
        
        if size2 > size1:
            solution += word2[size1:]
        elif size1 > size2:
            solution += word1[size2:]
        else:
            pass
        #if the word2 is bigger than word1, the final letters
        #will go till the end

        return solution

def main():
    word1 = input("input word1:     \n")
    word2 = input("input word2:     \n")

    solution = Solution()

    print(f"Solution:    {solution.mergeAlternately(word1, word2)}")


if __name__ == '__main__':
    main()