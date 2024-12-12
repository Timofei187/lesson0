def calculate_structure_sum1(data):
    sum_ = 0
    for i in data:
        # print('for', type(i))
        if isinstance(i, list)  or isinstance(i, tuple) or isinstance(i, set):
            # print('if isinstance', i)
            sum_ += calculate_structure_sum(i)
        if isinstance(i, dict):
            for key, value in i.items():
                sum_ += len(key)
                sum_ += value
        if isinstance(i, int):
            sum_ += i
        if isinstance(i, str):
            sum_ += len(i)
        # print('sum', sum_, 'i', i)
    return sum_

def calculate_structure_sum(data):
    sum_ = 0
    if isinstance(data, list) or isinstance(data, tuple) or isinstance(data, set):
        for i in data:
            sum_ += calculate_structure_sum(i)
    if isinstance(data, dict):
        for key, value in data.items():
            sum_ += len(key)
            sum_ += calculate_structure_sum(value)
    if isinstance(data, int):
        sum_ += data
    if isinstance(data, str):
        sum_ += len(data)
    return sum_

data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]


result = calculate_structure_sum(data_structure)

print(result)