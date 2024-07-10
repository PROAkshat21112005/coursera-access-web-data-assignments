code for the assignments in pyhton
import re
hand= open('regex_sum_2044215.txt')
total=0
for line in hand:
    line=line.rstrip()
    x=re.findall('[0-9]+',line)
    for i in x:
        i=int(i)
        total=total+i
print(total)
