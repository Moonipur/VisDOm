from __init__ import *

def MinMax(data_list):
    min_ = min(data_list)
    max_ = max(data_list)
    norm = [((x - min_) / (max_ - min_)) for x in data_list]

    return(norm)

def Zscore(data_list):
    def average(lst):
        return (sum(lst) / len(lst))
    
    def std(lst, mean):
        variance = sum([((x - mean) ** 2) for x in lst]) / len(lst)
        return(math.sqrt(variance))

    mean = average(data_list)
    sd = std(data_list, mean)
    stand = [((x - mean) / sd) for x in data_list]

    return(stand)