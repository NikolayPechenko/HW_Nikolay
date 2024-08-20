import datetime
import multiprocessing


def read_info(name):
    all_data = []
    with open(name, 'r') as file:
        while True:
            line = file.readline()
            if not line:
                break
            all_data.append(line)


file_list = []
for i in range(4):
    file_list.append(f'file {i+1}.txt')


# start = datetime.datetime.now()
# for j in file_list:
#     read_info(j)
# end = datetime.datetime.now()
# print(end - start)

start = datetime.datetime.now()
if __name__ == '__main__':
    with multiprocessing.Pool(processes=4) as pool:
        start = datetime.datetime.now()
        pool.map(read_info, file_list)
    end = datetime.datetime.now()
    print(end - start)
