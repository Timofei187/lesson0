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