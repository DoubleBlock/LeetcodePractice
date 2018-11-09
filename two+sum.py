def ReturnIndex(sums, target):
    d = {}
    for i, sum in enumerate(sums):
        if (target - sum) in d:
            return [d[target - sum], i]
        d[sum] = i


lists= [2, 7, 9, 11]



ReturnIndex(lists, 9)