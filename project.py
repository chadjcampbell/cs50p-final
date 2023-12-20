import os
import time
import sys


def main():
    os.system('clear')
    while True:
        single_print('LOGON: ', 0.1)
        username = input()
        if username.lower().strip() == 'joshua':
            break
    fake_norad()
    single_print('GREETINGS PROFESSOR FALKEN.',0.1)
    print('')
    


def single_print(string, speed):
    for char in string:
        sys.stdout.write(char + '\a')
        sys.stdout.flush()
        time.sleep(speed)


def fake_norad():
    single_print('jmnsZJrExk6f8xSaRCbuQl9vcT85K5YQs2rCYIRN0194KtIO1hXEMqcWtPwpSbPq',0.02)
    os.system('clear')
    single_print('wSRq1wztrXkoslH03h7Y139KVib4VRMHRmoEywKbi23JqOUmR5cXRz5n28HoAvdIIGtWxbs4BaBy4cWwWKUxCjtdKACxg11lZlP8iYe4QxKIgl18fzUz6jiVlNJLDvIgZCA2EG8rUqcWdpi82',0.01)
    os.system('clear')
    single_print('▒▒▒▒9vcT85▒▒▒  ▒03h7Y1▒▒▒ ▒▒▒▒▒▒▒ ▒▒▒▒▒▒KtIO1h▒▒▒ 867-5309 ▒▒▒▒▒ ▒▒▒▒▒▒aBy4c▒▒▒▒ ▒▒▒▒▒▒▒▒',0.02)
    os.system('clear')

def function_n():
    ...


if __name__ == "__main__":
    main()