import math

def total(list):
    try:
        if len(list) ==0:
            raise ValueError
        else:
            return sum(list)
    except ValueError:
        return 0

def average(list):
    if len(list)== 0:
        return math.nan
    else:
        return float(sum(list)/ len(list))

def median(list):
        if len(list) == 0:
            raise ValueError
        else:
            list.sort()
            median = int(len(list)/2)
            if len(list)%2 == 1:
                return list[median]
            else:
                return (list[median] + list[median-1])/2