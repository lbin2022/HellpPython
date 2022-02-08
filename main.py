def main(name):
    ss_dict = {'d': 'd', 'dd': 'dd', 'ddad': 'dad', 'dbabd': 'dbabd', 'dadad': 'dad', 'abcb': 'bcb',
                     'aabcbaa': 'aabcbaa', 'bcbcb': 'bcbcb'}


    for k, v in ss_dict.items():
        print('units: {} with expect result: {} and read result:{}'.format(str(k).ljust(15, ' '), str(v).ljust(15, ' '),
                                                                           Solution.longestPalindrome0(k)))


if __name__ == '__main__':
    main('PyCharm')
