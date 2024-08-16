from threading import Thread
import json

res = []
threads = []
files = ['file1.json', 'file2.json', 'file3.json', 'file4.json']


def worker(file):
    with open(file, 'r') as f:
        data = json.load(f)
        res.extend(data)


for i in range(len(files)):
    t = Thread(target=worker, args=(files[i],))
    t.start()
    threads.append(t)

for t in threads:
    t.join()

print(sum(res))
