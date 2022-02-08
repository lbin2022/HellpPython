import re

ori = '''This is b loooog string for re test. \
        Please take a good look at your bags!\
        That's all for yourself!!'''
comp = re.compile('oo', re.A)
print('Type of comp is {} \nValue of comp is {}'.format(type(comp), comp))
