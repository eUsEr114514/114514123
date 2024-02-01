common_list = [11,22,33,44,55]              #通用列表

#函数映射 map 采用一个函数和一个迭代作为参数，并返回一个新的迭代函数，应用于每个参数
def map_func(x):
    return x + 5
result_map = list(map(map_func,common_list))    #用map函数把command_list列表里的每一个元素
                                            #映射到map_func函数里;格式：(func,list)
print(result_map)

def filter_func(y):
    return y % 2 == 0
result_filter = list(filter(filter_func,common_list))
print(result_filter)

