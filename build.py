import operator


def solution_asc(dic):
    '''dic.items().sort
    return dic.items()'''

    ascDic = sorted(dic.items(),key = operator.itemgetter(2))
    print ascDic


def solution_desc(dic):
    '''
    Enter your code here
    '''
    descList = dic.items()
    descList.reverse()
    return  descList

solution_asc({1: 2, 3: 4, 4: 3, 2: 1, 0: 0})
solution_desc({1: 2, 3: 4, 4: 3, 2: 1, 0: 0})
