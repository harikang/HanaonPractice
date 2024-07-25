import sys
import datetime
# import random 
# import numpy as np
# import torch
# import torch.nn as nn
from practice import *

if __name__ == '__main__':
    #제어가 필요할 때, 이 패턴을 사용함. 
    #     arg = sys.argv
    #     print(arg)
    # l = list(map(int,input().split()))
    
    # model = Model(l[0],l[1],l[2])
    # data  = torch.Tensor(np.random.rand(10, 10))
    # print(data.shape, data)
    # out = model(data)
    # print(out.shape, out)
    # if __name__=="__main__":
    #     import os
    #     os.open
    #     txt_path = Path('D:\workspace_hanabank\project_section06\0722.txt')
    #     print(txt_path.absolute) #절대경로를 return함. 
    # a = (1,2,3,4,5,6)
    # b =('A','B','C')
    # c = {'가','나','다'}
    # for i in zip(a,b,c):
    #     print(i)

    # keys = ["a","b","c"]
    # values = [1,2,3]
    # a = '?' +"&".join(map(lambda k, v: f'{k}={v}',keys,values))
    # print(a)
    # point = Point(3,2)
    # print(point.__str__())
    # print(point.__repr__())
    # zip()과 iter()를 사용한 이디엄
    # s = range(12)
    # n = 3
    # val = list(
    #     zip(
    #         *[iter(s)]*n
    #         )
    #     )
    # print(val)
    # cdict = CountDict()
    # cdict[1] = 0
    # cdict[2] = 0
    # cdict.__getitem__(1)
    # cdict.__getitem__(1)
    # cdict.__getitem__(1)
    # cdict.__setitem__(2,100)

    # cdict.count()

    # # 반환값은 제너레이터 이터레이터
    # gen = gen_function(2)
    # gen
    # 존재하는 임의의 파일 경로를 반환
    r = reader('D:\workspace_hanabank\Chapter07\src.txt')
    writer('D:\workspace_hanabank\Chapter07\dest.txt', r)
