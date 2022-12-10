def read(fname):
    with open(fname, 'r') as f:
        return f.read()

data_day1 = read('data/data1.txt')
data_day2 = read('data/data2.txt')
data_day3 = read('data/data3.txt')
data_day4 = read('data/data4.txt')
data_day5 = read('data/data5.txt')
data_day6 = read('data/data6.txt')
data_day7 = read('data/data7.txt')
data_day8 = read('data/data8.txt')
data_day8 = [[int(c) for c in line] for line in data_day8.split('\n')]
data_day9 = read('data/data9.txt')
data_day10 = read('data/data10.txt')

