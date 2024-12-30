'''
"Looks like the Chief's not here. Next!" One of The Historians pulls out a device and pushes the only button on it. After a brief flash, you recognize the interior of the Ceres monitoring station!

As the search for the Chief continues, a small Elf who lives on the station tugs on your shirt; she'd like to know if you could help her with her word search (your puzzle input). She only has to find one word: XMAS.

This word search allows words to be horizontal, vertical, diagonal, written backwards, or even overlapping other words. It's a little unusual, though, as you don't merely need to find one instance of XMAS - you need to find all of them. Here are a few ways XMAS might appear, where irrelevant characters have been replaced with .:


..X...
.SAMX.
.A..A.
XMAS.S
.X....
The actual word search will be full of letters instead. For example:

MMMSXXMASM
MSAMXMSMSA
AMXSXMAAMM
MSAMASMSMX
XMASAMXAMM
XXAMMXXAMA
SMSMSASXSS
SAXAMASAAA
MAMMMXMMMM
MXMXAXMASX
In this word search, XMAS occurs a total of 18 times; here's the same word search again, but where letters not involved in any XMAS have been replaced with .:

....XXMAS.
.SAMXMS...
...S..A...
..A.A.MS.X
XMASAMX.MM
X.....XA.A
S.S.S.S.SS
.A.A.A.A.A
..M.M.M.MM
.X.X.XMASX
'''
# Take a look at the little Elf's word search. How many times does XMAS appear?

# file = open('Day3_input.txt', 'r')

# inputFile = file.read()

file = open('input/Day4.txt', 'r')
inputFile = file.read()

# str.count(substring) counts the occurences of a substring in str

occurance = 0

list1d = inputFile.split('\n')
list2d = [list(row) for row in list1d]
height = len(list1d)
width = len(list2d[0])




horizontalList = inputFile.splitlines()

for line in horizontalList:
    occurance += line.count('XMAS')
    occurance += line.count('SAMX')



verticalList = ['' for _ in range(len(horizontalList[0]))]

i = len(horizontalList[0])
j = 0
for row_index, row in enumerate(list2d):
    for col_index, item in enumerate(row):
        verticalList[col_index] = verticalList[col_index] + item


for line in verticalList:
    occurance += line.count('XMAS')
    occurance += line.count('SAMX')


# diagonalListTOPLEFT = ''
# diagonalListBottomLEFT = ''

# Check diagonal occurrences
for i in range(height):
    for j in range(width):
        # Check bottom-right diagonal
        if i + 3 < height and j + 3 < width:
            if (list2d[i][j] == 'X' and list2d[i+1][j+1] == 'M' and
                list2d[i+2][j+2] == 'A' and list2d[i+3][j+3] == 'S'):
                occurance += 1
        # Check bottom-left diagonal
        if i + 3 < height and j - 3 >= 0:
            if (list2d[i][j] == 'X' and list2d[i+1][j-1] == 'M' and
                list2d[i+2][j-2] == 'A' and list2d[i+3][j-3] == 'S'):
                occurance += 1
        # Check top-right diagonal
        if i - 3 >= 0 and j + 3 < width:
            if (list2d[i][j] == 'X' and list2d[i-1][j+1] == 'M' and
                list2d[i-2][j+2] == 'A' and list2d[i-3][j+3] == 'S'):
                occurance += 1
        # Check top-left diagonal
        if i - 3 >= 0 and j - 3 >= 0:
            if (list2d[i][j] == 'X' and list2d[i-1][j-1] == 'M' and
                list2d[i-2][j-2] == 'A' and list2d[i-3][j-3] == 'S'):
                occurance += 1


print (occurance)
# Answer: 2644


'''
--- Part Two ---
The Elf looks quizzically at you. Did you misunderstand the assignment?

Looking for the instructions, you flip over the word search to find that this isn't actually an XMAS puzzle; it's an X-MAS puzzle in which you're supposed to find two MAS in the shape of an X. One way to achieve that is like this:

M.S
.A.
M.S
Irrelevant characters have again been replaced with . in the above diagram. Within the X, each MAS can be written forwards or backwards.

Here's the same example from before, but this time all of the X-MASes have been kept instead:

.M.S......
..A..MSMS.
.M.S.MAA..
..A.ASMSM.
.M.S.M....
..........
S.S.S.S.S.
.A.A.A.A..
M.M.M.M.M.
..........
In this example, an X-MAS appears 9 times.

'''

# Flip the word search from the instructions back over to the word search side and try again. How many times does an X-MAS appear?


newOccurance = 0
# Check diagonal occurrences
for i in range(height):
    for j in range(width):
        # check the optimal A
        if 0 < i < height - 1 and 0 < j < width - 1 :
            # check x-mas(es)
            # M S
            #  A
            # M S
            if (list2d[i][j] == 'A' and list2d[i+1][j+1] == 'S' and list2d[i-1][j+1] == 'S' and
                list2d[i+1][j-1] == 'M' and list2d[i-1][j-1] == 'M'):
                    newOccurance += 1
            # S M
            #  A
            # S M
            elif(list2d[i][j] == 'A' and list2d[i+1][j+1] == 'M' and list2d[i-1][j+1] == 'M' and
                list2d[i+1][j-1] == 'S' and list2d[i-1][j-1] == 'S'):
                    newOccurance += 1
            # M M
            #  A
            # S S
            elif(list2d[i][j] == 'A' and list2d[i+1][j+1] == 'S' and list2d[i-1][j+1] == 'M' and
                list2d[i+1][j-1] == 'S' and list2d[i-1][j-1] == 'M'):
                    newOccurance += 1
            # S S
            #  A
            # M M
            elif(list2d[i][j] == 'A' and list2d[i+1][j+1] == 'M' and list2d[i-1][j+1] == 'S' and
                list2d[i+1][j-1] == 'M' and list2d[i-1][j-1] == 'S'):
                    newOccurance += 1
print(newOccurance)
# Answer: 1952
