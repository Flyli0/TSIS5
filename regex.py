'''''''''''''''''''''''''''''''''Task1'''''''''''''''''''''''''''''''''
import re 

ss = str(input())
sss = re.match('ab*',ss)
if sss:
    print('Match')
else:
    print('Not match')

'''''''''''''''''''''''''''''''''Task2'''''''''''''''''''''''''''''''''
ss = str(input())
sss = re.fullmatch('ab{2,3}',ss)
if sss:
    print('Match')
else:
    print('Not match')

'''''''''''''''''''''''''''''''''Task3'''''''''''''''''''''''''''''''''

ss = str(input())
sss = re.match('[a-z]+_[a-z]+',ss)
if sss:
    print('Match')
else:
    print('Not match')

'''''''''''''''''''''''''''''''''Task4'''''''''''''''''''''''''''''''''

ss = str(input())
sss = re.fullmatch('[A-Z]{1}[a-z]+',ss)
if sss:
    print('Match')
else:
    print('Not match')

'''''''''''''''''''''''''''''''''Task5'''''''''''''''''''''''''''''''''

ss = str(input())
sss = re.match('a.*b',ss)
if sss:
    print('Match')
else:
    print('Not match')

'''''''''''''''''''''''''''''''''Task6'''''''''''''''''''''''''''''''''
import re
ss = str(input())
sss = re.sub('[ ,.]',':',ss)
print(sss)

'''''''''''''''''''''''''''''''''Task7'''''''''''''''''''''''''''''''''
import re
ss = str(input())
sss = re.sub('_([a-z])',lambda letter: letter.group(1).upper(),ss)
print(sss)

'''''''''''''''''''''''''''''''''Task7'''''''''''''''''''''''''''''''''