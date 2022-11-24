import hashlib
import itertools
import multiprocessing
import time
import os

time_start = time.time()
hash = '7e9fde1979e35a31cc0703871eb548aeb946e07acb87de4cb4d95b28b42418da'

def brute_force_Process(arg):
    main_chars, sub_chars = arg[0], arg[1]
    alphabet = main_chars + sub_chars
    for letter in itertools.product(alphabet, repeat=3):
        passwd = ''.join(letter)
        if passwd.startswith(sub_chars[0]):
            break
        tmp = hashlib.sha256(passwd.encode()).hexdigest()

        if tmp == hash:
            print(f'password: {passwd}')
            break
if __name__ == '__main__':
    with multiprocessing.Pool(processes=11) as pool:
        args = [['0123', '456789abcdefghklmnopqrstuvwxyzABCDEFGH'],
                ['4567', '012389abcdefghklmnopqrstuvwxyzABCDEFGH'],
                ['89ab', '01234567cdefghklmnopqrstuvwxyzABCDEFGH'],
                ['cdef', '0123456789abghklmnopqrstuvwxyzABCDEFGH'],
                ['ghkl', '0123456789abcdefmnopqrstuvwxyzABCDEFGH'],
                ['mnop', '0123456789abcdefghklqrstuvwxyzABCDEFGH'],
                ['qrst', '0123456789abcdefghklmnopuvwxyzABCDEFGH'],
                ['uvwx', '0123456789abcdefghklmnopqrstyzABCDEFGH'],
                ['yzAB', '0123456789abcdefghklmnopqrstuvwxCDEFGH'],
                ['CDEF', '0123456789abcdefghklmnopqrstuvwxyzABGH'],
                ['GH', '0123456789abcdefghklmnopqrstuvwxyzABCDEF']]
        result = pool.map(brute_force_Process, args)
    print('Время:', time.time() - time_start)
