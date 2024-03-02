import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# 定义波浪参数
wave_length = 2 * np.pi  # 波长
amplitude = 1  # 振幅
phaseshift = np.pi / 4  # 相位偏移

# 定义空间域
x = np.linspace(-5, 5, 100)
y = np.linspace(-5, 5, 100)
x, y = np.meshgrid(x, y)

# 使用正弦和余弦函数计算z坐标以模拟波浪效果
z = amplitude * np.sin(x + phaseshift) + amplitude * np.sin(y)

print(x)

# # 绘制三维图形
# fig = plt.figure()
# ax = fig.add_subplot(111, projection='3d')
# ax.plot_surface(x, y, z, rstride=1, cstride=1, cmap='viridis', edgecolor='none')

# # 标题和轴标签
# ax.set_title('3D Wave Pattern')
# ax.set_xlabel('X')
# ax.set_ylabel('Y')
# ax.set_zlabel('Z')

# # 显示图形
# plt.show()