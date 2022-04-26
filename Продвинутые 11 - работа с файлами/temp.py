import string

s = 'qwerty12ytrewq'
print('**************',s,type(s))
for j in string.ascii_letters:
    s=s.replace(j,' ')

print(s,'**********')
