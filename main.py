import os

# To Open File and Read Data
def open_file():
    file=open('example.txt','r')
    data=file.read()
    print(data)
    file.close()
# To Write Data in File
def write_file(word):
    file=open('example.txt','w')
    file.write(f'{word}')
    file.close()
    return word
# To Add Content To File
def edit(word):
    file=open('example.txt','a')
    file.write(f'\n{word}')
    file.close()
    return word
print('=============================================================================')
print('Choose from here [ 1- Open File 2- Write File 3- Add Content To The File]')
print('=============================================================================')
choose=int(input('Enter Your Number: '))
if choose==1:
    open_file() 
elif choose==2:
    print(write_file('Hellow World'))
elif choose==3:
    print(edit('Hellow There'))

