__author__ = 'shihchosen'
import os
import time

source = ['/Users/shihchosen/PycharmProjects/Byte_of_Python/1']
target_dir = '/Users/shihchosen/PycharmProjects/Byte_of_Python/2'

target = target_dir + os.sep + time.strftime('%Y%m%d%H%M%S') + '.zip'

zip_command = "zip -r {0} {1}".format(target, ''.join(source))

if os.system(zip_command) == 0:
    print('Successful backup to', target)
else:
    print('Backup FAILED')