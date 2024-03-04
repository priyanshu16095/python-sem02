def sortDict(dict1):
    dict2 = dict(sorted(dict1.items(), key=lambda item: item[1], reverse=True))
    return dict2

dict1 = {'stu1': 85, 'stu2': 92, 'stu3': 78, 'stu4': 95, 'stu5': 89}
dict2 = sortDict(dict1)
print(dict2)