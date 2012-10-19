###
# Gets the distance between two words, calculated by minimum number of
# insertions, substitutions, or deletions.
###

import sys

def WordDistance(word1, word2):
    #print '\nComparing [%s] to [%s]' % (word1, word2)
    if(word1 == word2):
        return 0
    
    if(len(word1)==0 and len(word2)==0):
        # No length, return 0
        return 0;
    if(len(word1) == 0):
        # No word1, return len(word2) (# of deletions)
        # deletion edge case
        return len(word2)
    if(len(word2) == 0):
        # No word2, return len(word1) (# of insertions)
        return len(word1)
    
    # Words don't match.
    char1 = word1[0]
    char2 = word2[0]
    
    if(char1 == char2):
        # Characters match going to next one.
        return WordDistance(word1[1:], word2[1:])

    # Get substitution count.
    substitutionCount = 1 + WordDistance(word1, char1 + word2[1:])
    if(substitutionCount == 1):
        return 1

    # Get deletion count.
    deletionCount = 1 + WordDistance(word1, word2[1:])
    if(deletionCount == 1):
        return 1

    # Get insertion count.
    insertionCount = 1 + WordDistance(word1, char1 + word2)
    if(insertionCount == 1):
        return 1

    return Min3(deletionCount, substitutionCount, insertionCount)

def Min2(num1, num2):
    if (num1 < num2):
        return num1
    else:
        return num2

def Min3(num1, num2, num3):
    return Min2(num1, Min2(num2, num3))


if(len(sys.argv) != 3):
    print 'Usage:\n -> python WordDistance.py [correctWord] [incorrectWord]'
else:
    correctWord   = sys.argv[1]
    incorrectWord = sys.argv[2]
    print 'correct word:   ' + correctWord
    print 'incorrect word: ' + incorrectWord
    print 'distance: %i' % WordDistance(correctWord, incorrectWord)
