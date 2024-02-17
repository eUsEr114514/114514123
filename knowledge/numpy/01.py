import numpy as np

# numpy中所有的计算都是围绕着数组array进行的
original_list = [1, 2, 3, 4, 5]
convert = np.array(original_list)
print(convert)

# 用np.shape来获取数组的尺寸
print(np.shape(original_list))  # (行数,列数)一列不显示数字

# 用np.zeros创建一个全零的数组
print(np.zeros((3,2)))          # (行数,列数)

# 用np.ones创建一个全是一的数组
print(np.ones((2,3)))           # (行数,列数)

# 用np.arange创建一个递增或递减的数组
print(np.arange(1,7))           # （左开右闭）

# 用np.linsopace可以返回某个区间等间距分布的数
print(np.linspace(5,7,5))   # (起始值,初始值,多少个数)

# 用np.random.rand随机生成应该数组
print(np.random.randn(5))       # (起始值,结束值)（在此区间随机生成数）

# 相同尺寸的数组可以直接进行四则运算
plus1 = np.array([1,1,4])
plus2 = np.array([5,1,4])
print(plus1 + plus2)

# 用np.dot讲两个数组进行点乘运算（相同位置的元素相乘再相加）
dot1 = np.array([1,1,4])
dot2 = np.array([5,1,4])
print(np.dot(dot1,dot2))

# 用@进行矩阵的乘法运算（等同于np.matmul()函数）
matmul1 = np.array([[7,5],
                   [2,4]])
matmul2 = np.array([[1,0],
                   [5,2]])
print(matmul1 @ matmul2)

# 用np.sqrt对所有数依次求平方根
sqrt_array = np.array([9,5,4])
print(np.sqrt(sqrt_array))

# 用np.sin，np.cos，np.log进行相应的数学运算（log运算以自然常数e为底数）

# 用np.power进行幂运算
power = np.array([7,5])
print(np.power(power,2))        # (数组，多少次方)

# 用np.sum返回所有数据的总和
sum = np.array([i for i in range(1,101)])
print(np.sum(sum))

# 用np.mean返回数据的平均值
mean = np.array([1,2,4,5,7,8,10])
print(np.mean(mean))

# 用np.median返回数据的中位数
median = np.array([1,2,4,5,7,8,10])
print(np.median(median))

# 用np.var和np.std会返回数据的方差和标准方差
var_or_std = np.array([1,1,4,5,1,4])
print(np.var(var_or_std))
print(np.std(var_or_std))




