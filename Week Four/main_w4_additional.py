# WEEK 4 - ADDITIONAL EXERCISES

# ---- Exercise 1: The King and the Wise man ----
'''
When the creator of the game of chess showed his invention to the ruler of the country, the
ruler was so pleased that he gave the inventor the right to name his prize for the invention. The
man, who was very wise, asked the king this: that for the first square of the chess board, he
would receive one grain of wheat (in some telling, rice), two for the second one, four on the
third one, and so forth, doubling the amount each time. The ruler, arithmetically unaware,
quickly accepted the inventor's offer, even getting offended by his perceived notion that the
inventor was asking for such a low price and ordered the treasurer to count and hand over the
wheat to the inventor. Given that the chessboard is a 8 × 8 board and given the weight of a
single grain of rice is about 30 mg, calculate the total weight of rice the king must give to the
wise man. The program should print the weight of rice for each chessboard square.
'''

# Probabily overcomplicating this, but I'm going to display this in a table
# for position x, y, the amount of rice is calculated as such (first square is 0,0):
# 2**(y*8+x)

## [[[gain_count, grain_mass, grain_mass_hr],...],...]
chess_board = []

# milligrams, ..., tonnes, kilotonnes, ..., teratonnes
mass_units = ["mg","g","kg","T","KT","MT","GT","TT"]

# Takes a mass (mg) and converts it to a more readable format
# Longest output is 5 characters
def humanReadableAmount(mass: int, includeFrac: bool = False) -> str:
    unit = 0
    while(mass > 1000):
        unit += 1
        mass /= 1000
    if includeFrac:
        return str(round(mass,3))+mass_units[unit]
    else:    
        return str(int(mass))+mass_units[unit]

# calculate grain amounts
for x in range(8):
    row = []
    for y in range(8):
        grain_count = 2**(x*8+y)
        grain_mass = 30*grain_count
        grain_mass_hr = humanReadableAmount(grain_mass)
        cell = [grain_count,grain_mass,grain_mass_hr]
        row.append(cell)
    chess_board.append(row)

# print grain masses in table (all values are rounded)
print("+-----"*len(chess_board[0])+"+")
for x in range(len(chess_board)):
    masses = ['{s:{c}^{n}}'.format(s=cell[2],n=5,c=' ') for cell in chess_board[x]]
    print("|","|".join(map(str,masses)),"|", sep="")
    print("+-----"*len(chess_board[x])+"+")

total_mass = sum([cell[1] for cell in row for row in chess_board])
print("Total mass:",humanReadableAmount(total_mass, True))