# Daily Challenge: Solve The Matrix 
    # To decrypt the matrix, Neo reads each column from top to bottom,  
    # starting from the leftmost column, selecting only the alpha characters and connecting them. 
    # Then he replaces every group of symbols between two alpha characters by a space. 
 
matrix_string="""
7ii
Tsx
h%?
i #
sM 
$a 
#t%
^r!
""" 
rows=[] 
row=[] 
for char in matrix_string: 
    if char == "\n": 
        continue 
    if len(row)<3: 
        row.append(char) 
    if len(row) == 3: 
        rows.append(row) 
        row=[] 
# print(rows)
str_1,str_2,str_3="","","" 
for row in rows: 
    str_1=str_1 + row[0] 
    str_2=str_2 + row[1] 
    str_3=str_3 + row[2] 
 
final_str=str_1+str_2+str_3 
# print((final_str))

for char in final_str: 
    if char.isalpha() == False: 
        final_str= final_str.replace(char," ") 
 
final_str=final_str.split() 
final_str=" ".join(final_str)
print(final_str)