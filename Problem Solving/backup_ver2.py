__author__ = 'shihchosen'
import os
import time

source = ['/Users/shihchosen/PycharmProjects/Byte_of_Python/1']
target_dir = '/Users/shihchosen/PycharmProjects/Byte_of_Python/2'

today = target_dir + os.sep + time.strftime('%Y%m%d')
now = time.strftime('%H%M%S')

if not os.path.exists(today):
    os.mkdir(today)
    print('Successfully created directory', today)

target = today + os.sep + now + '.zip'

zip_command = "zip -r {0} {1}".format(target, ''.join(source))

if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')