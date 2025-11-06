import os

from datetime import datetime
os.chdir('/Users/onurs/OneDrive/Desktop/')

# print(os.stat('demo.txt'))

# for dirpath, dirnames, filenames in os.walk('/Users/onurs/OneDrive/Desktop/'):
#     print('Current path:', dirpath)
#     print('Directories:', dirnames)
#     print('Files:',filenames)

print(os.path.exists('/tmp/test.txt'))