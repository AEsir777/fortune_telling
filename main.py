

class Symbol():
    PEACE = '大安'
    LINGERING = '留连'
    JOY = '速喜'
    MOUTH = '赤口'
    LITTLE = '小吉'
    VOID = '空亡'

symbol = [(Symbol.PEACE, 'great peace'), (Symbol.LINGERING, 'Lingering Fate'), 
          (Symbol.JOY, 'swift joy'), (Symbol.MOUTH, 'red mouth'), 
          (Symbol.LITTLE, 'little fortune'), (Symbol.VOID, 'void')]

def inc(num):
    if num == len(symbol):
        num = 0
    else:
        num += 1
    return(num)

# 24hr
def to_lunar_date(year, month, day, hour):
    return (year, month, day, hour)

def get_symbol(month, day, hour):
    i = 0
    while month > 1:
        i = inc(i)
        month -= 1
    res1 = symbol[i]

    while day > 1:
        i = inc(i)
        day -= 1
    res2 = symbol[i]

    while hour > 1:
        i = inc(i)
        hour -= 1
    res3 = symbol[i]

    print(res1, res2, res3)
    
    match res2[0]:
        case Symbol.PEACE:
            match res3[0]:
                case Symbol.PEACE:
                    print('失物家中寻')
                case Symbol.LINGERING:
                    print('办事不周全，失物西北去，婚姻晚几天')
                case Symbol.JOY:
                    print('事事自己起，失物当日见，婚姻自己提')
                case Symbol.MOUTH:
                    print('办事不顺手，失物不用找，婚姻两分手')
                case Symbol.LITTLE:
                    print('事事从己及，失物不出门，婚姻成就地')
                case Symbol.VOID:
                    print('病人要上床，失物无踪影，事事不顺情')
        case Symbol.LINGERING:
            match res3.first:
                case Symbol.PEACE:
                    print('办事两分张，婚姻有喜事，先苦后来甜')
                case Symbol.LINGERING:
                    print('

get_symbol(9, 23, 10)

    
