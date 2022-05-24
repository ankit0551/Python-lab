def shut_down(st):
    if st == 'yes':
        return 'Shutting down'
    elif st == 'no':
        return 'Shutdown aborted'
    else:
        return 'i am Sorry babu'

str = input()
print(shut_down(str))
