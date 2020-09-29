import os

path=os.path.dirname(os.path.abspath(__file__))

file_name='aux.txt'
f=os.path.join(path, file_name)

string1=''
string2=''

'''cell_dict={}
for row in range(0,9):
    for col in range(0,9):
        string+=f"self.cell{row}{col}.setProperty('value', int(sudoku[{row},{col}]))\n"

with open('hola.txt', 'w') as f:
    f.write(string)'''

'''for row in range(0,9):
    for col in range(0,9):
        string+=f"current_sudoku[{row},{col}]=int(self.cell{row}{col}.value())\n"'''


for row in range(0,9):
    string1+=f"{row}:[self.cell{row}0,self.cell{row}1,self.cell{row}2,self.cell{row}3,self.cell{row}4,self.cell{row}5,self.cell{row}6,self.cell{row}7,self.cell{row}8],"
for col in range (0,9):
    string2+=f"{col}:[self.cell0{col},self.cell1{col},self.cell2{col},self.cell3{col},self.cell4{col},self.cell5{col},self.cell6{col},self.cell7{col},self.cell8{col}],"


with open('getcelldicts.txt', 'w') as f:
    f.write(string1+'\n\n'+string2)

