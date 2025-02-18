import re
ss = str(input())
sss = re.sub('_([a-z])',lambda letter: letter.group(1).upper(),ss)
print(sss)