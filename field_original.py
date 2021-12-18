from typing import List


# field = list('|'*99)
field = list('|\'\'\'\''*20)
field.append('|')
football = u"\U0001F3C8"
field[25] = football

if field.index(football)%5==0:
    field[field.index(football)]= ('\033[4m'+football+'\033[0m')

field_str = ''.join(field)


print(field_str)