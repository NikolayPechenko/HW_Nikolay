import json
from random import randint


res = []
files = ['file1.json', 'file2.json', 'file3.json', 'file4.json']

# for file in files:
#     for i in range(10000):
#         res.append(randint(1, 1000))
#     with open(file, 'w') as f:
#         json.dump(res, f)  # так как у файла формат json, добавили туда данные из res с помощью этих действий
#     res = []


res_to_count = []
for file in files:
    with open(file, 'r') as f:
        data = json.load(f)
        res_to_count.extend(data)
print(sum(res_to_count))  # пример без потокаов
