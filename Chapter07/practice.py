# import torch.nn as nn
# import torch
import json #directory 
from collections import defaultdict
# class Model(nn.Module):
#     def __init__(self,input,output,kernel):
#         super(Model,self).__init__()
#         self.input = input
#         self.output = output
#         self.kernel = kernel
#         self.conv1 = nn.Conv1d(input,output,kernel) 
#     def forward(self,x):
#         out = self.conv1(x)
#         return out
    
# def print():
#     return None

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    # def __len__(self):
    #     return 3
    def __repr__(self):
        return f'Point({self.x}, {self.y})'
    def __str__(self):
        return eval("self.x") #f'({self.x}, {self.y})'

class Config:
    def __init__(self, filename):
        self.config = json.load(open(filename))
    def __getattr__(self, name):
        if name in self.config:
            return self.config[name]
        # 존재하지 않는 설정값으로의 엑세스 시 에러
        raise AttributeError()


class CountDict:
    def __init__(self):
        self._data = {}
        self._get_count = defaultdict(int)
        self._set_count = defaultdict(int)
    def __getitem__(self, key):
        self._get_count[key] += 1
        return self._data[key]
    def __setitem__(self, key, value):
        self._set_count[key] += 1
        self._data[key] = value
    @property
    def count(self):
        return {
            'set': list(self._set_count.items()),
            'get': list(self._get_count.items()),
        }

def gen_function(n):
    print('start')
    while n:
        print(f'yield: {n}')
        yield n  # 여기에서 일시 중단됨
        n -= 1

def convert(line):
    return line.upper()

def reader(src):
    with open(src) as f:
        for line in f:
            yield line

def writer(dest, reader):
    with open(dest, 'w') as f:
        for line in reader:
            f.write(convert(line))
            