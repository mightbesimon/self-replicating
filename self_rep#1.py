filename = 'self_rep#1.py'
import os
with open(filename, 'r') as file: content = file.readline()*0 + file.read()
filename = 'self_rep#%s.py' % (int(filename.split('.')[0].split('#')[1]) + 1)
with open(filename, 'w') as file: file.write(f"filename = '{filename}'\n{content}")
os.system(f'python3 {filename}')