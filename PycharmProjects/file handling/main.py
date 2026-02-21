""" file=open('data','r+')
print(file.read())
st='anbjdjgfgdxsertyuiolk,mjnhgbvfds'
file.write(st)
file.close() """

"""
file=open('data', 'w')
st='b124'
file.write(st)
file.close() """


"""
file=open('data', 'a')
st='taharin'
file.write(st)
file.close()
"""

"""
file=open('data', 'r+')
print(file.read())
st='vbh'
file.write(st)
file.close()
"""
""""
file=open('data', 'w+')
st='abcdefghi'
file.seek(0,0)
file.write(st)
print(file.read())


file.close()"""



"""

file=open('data', 'r')
data=(file.read(50))

print(data)
file.close()
"""
"""
file=open('data', 'w')
list=['one\n','two\n', 'three\n', 'four\n',  'nine\n']
file.writelines(list)


file.close()
"""



with open('data', 'r') as file:
    data=file.read()
    print(data)