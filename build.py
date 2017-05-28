import operator


def solution_asc(dic):
    '''dic.items().sort
    return dic.items()'''

    ascDic = sorted(dic.items(),key = operator.itemgetter(0))
    return ascDic


def solution_desc(dic):
    '''
    Enter your code here
    '''
    ascDic = sorted(dic.items(),key = operator.itemgetter(0),reverse = True)
    return ascDic

solution_asc({1: 2, 3: 4, 4: 3, 2: 1, 0: 0})
solution_desc({1: 2, 3: 4, 4: 3, 2: 1, 0: 0})
