#!/usr/bin/python3
'''Module that inherits from list type'''


class MyList(list):
    ''' Class that inherits and prints sorted'''
    def print_sorted(self):
        '''print sorted list'''
        print(sorted(self)
