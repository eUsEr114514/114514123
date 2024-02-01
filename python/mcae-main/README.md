# mcae
A minecraft command animation tool.(More English documents to be written)

## 关于

mcae是一个用于制作Minecraft原版指令动画的工具。

它可以用来制作各种粒子动画，方块动画，实体动画，以function序列的方式在游戏中加载。

你可以用它轻松制作类似 “粒子特效”， “无缝剪辑”，“音乐可视化”，“视觉盛宴”， “前方高能”的视频。

当然，作为本项目作者，更希望你能制作出更多有创意的作品，而不是一味模仿前人的作品。

## 快速开始

本来这都是在Github了，你应该没有理由说你不会安装python。但考虑到MC玩家范围太广，还是简单说说。

### 安装

1. 安装python
   1. https://www.python.org/ 这里是python官网，进去后看到Downloads，下面有各种平台，下载后打开。
   2. 安装时记得勾选添加Add to PATH（添加到环境变量）, Install pip（安装pip）（这里不一定每个字都相同，但意思是这个）
2. 安装本项目依赖库
   1. 本项目依赖numpy, PIL 运行
   2. 在终端（Windows也就是cmd）依次输入并执行 `pip install numpy`， `pip install PIL`等待完成即可。中途如果遇到问题，去网上搜索应该就能解决。随着更新，之后可能有其他库，也是差不多的安装方法。
3. 下载本项目代码
   1. 可以在本项目主页的“Code”按钮处选择Download ZIP下载到最新的版本（不稳定）。
   2. 推荐去Release处下载大概测试过的版本（）
   3. 下载后是个压缩包，解压即可
   4. 以上都完成后，可以运行example测试是否正确安装。

### 简单的入门说明

1. 一些你需要知道的游戏内容
   1. Tick：游戏刻。也就是游戏中的时间单位，原版中1秒等于20Tick，所以制作你的动画时记得填对这个参数。
   2. Datapack：数据包。通过编写它可以实现很多功能。这里是用来放function
   3. Function：函数。他是一个文本文件，后缀为.mcfunction，里面可以写多条指令进去。执行时会一次执行完里面的所有指令。
   4. 命令方块：可以用来执行指令，用红石可以激活。
   5. 坐标：x, y, z三个数字，游戏中用来表示位置。按下F3可以查看你自己的坐标和你指向方块的坐标。
   6. 如何加载数据包，函数：
      1. 数据包文件夹较为复杂，建议下个模板直接扔存档里。
      2. 函数文件放在functions文件夹下（如“datapacks\example\data\mcae\functions”）
      3. 文件放好后，进游戏，输入/reload重载。
      4. 使用/function指令执行函数 按Tab可快速补全
      5. 本项目是使用一个命令方块序列执行函数，所以进游戏后先执行类似“/function mcae:ani/build_cb_seq”的指令创建命令方块，再执行第一个function。此外你也可以使用计分板或者其他方式执行函数序列。
2. 准备一个文本编辑器，写代码。这里推荐VScode（轻量，美观）
3. 这是一个简单的例子(更多可以参考example1.py )：

```python
# 这里是导入需要用的模块，如果你不会python，可以不管
import particle
import function
import points


# 粒子相关
# 初始化形状，粒子命令生成器，函数生成器（如果你不会python，可以不管）
shape = points.Shapes()
particle_cmd = particle.CmdBuilder()
ani_func = function.Function()
# ============以下部分需要你能看懂，或者至少知道参数该怎么填写============
# 创建一条由0Tick到20Tick的粒子直线动画
# 每个函数的详细参数都可以在相应代码的注释中查看（虽然还有部分注释未完善）
# 生成一条起点为0, 0, 0 终点为20, 20, 20的直线，每0.2格在这条直线上取一个点。返回所有产生的点
line = shape.line(0, 0, 0, 20, 20, 20, 0.2)
# 生成静态的粒子命令，动画从0Tick开始至20Tick结束，点使用上面生成的直线，粒子名为'end_rod'，
# 粒子运动范围为0, 0, 0， 速度为0， 每条指令产生1个粒子
particle_cmd.static_particle(0, 20, line, 'end_rod', 0, 0, 0, 0, 1)
# 如果想添加更多动画，怎么办？
# 粒子生成器除了粒子画外，思路基本都为1.生成一堆点2.用生成的点生成指令
# 比如我还要画一条线，从20Tick开始40Tick结束可以这样写
# line2 = shape.line(10, 10, 10, 30, 30, 30, 0.2)
# particle_cmd.static_particle(20, 40, line2, 'end_rod', 0, 0, 0, 0, 1)
# ============就这两行，没了。后面的你不想看就当作它是在保存就行了============
# 将上面生成的粒子命令添加到function中，如果制作了多个粒子动画，每个都会保存在particle_cmd.cmds中，只需要在最后添加一次即可
ani_func.add_cmd(particle_cmd.cmds)
# 导出一个命令方块序列，用于执行以上制作的动画
# V1.0.1 可用schedule模式导出，schedule功能需要游戏版本1.14以上
# ani_func.output_cb_seq_function('mcae', 'ani', -10, 5, -10, 'x+', 64, 64)
# 导出函数文件序列
# ani_func.save_seq_file('ani')
# V1.0.1 注意，这里由原来的命令方块序列改为了schedule来执行function序列。
# 游戏中请使用 形如“/function mcae:ani/schedule”的指令运行你的动画
ani_func.save_seq_file('ani', build_schedule=True, namespace='mcae')
# 至此，你可以将目录下的 ani 文件下放入你存档中数据包的functions文件夹下。
# 例如：.minecraft\saves\新的世界\datapacks\example\data\mcae\functions
# 如果你不会使用datapack 可以去Wiki搜索相关条目。
```

### 本项目的一些数据格式

这里是本项目的一些简单的数据格式，可以为贡献代码或者阅读注释不完善的代码时提供帮助。

1. 点(point)：列表 [x, y, z]。如[1, 2, 3]
2. 点列表(point_list)：列表 [[x, y, z], [x2, y2, z2], ....]
3. 命令(cmd)：`__str__`方法返回具体指令。属性由具体指令决定
4. 刻(tick, t0, t1....)：整数 游戏刻
5. motions: 类似点列表 [[x, y, z], [x2, y2, z2], ....]

## TODO

- function
  - ~~函数序列管理（添加，删除）~~
  - ~~函数文件导出（单文件，序列）~~

- midi
  - 读取midi生成信息表

- playsound
  - api
    - 基本命令
  -  应用
    - midi配合资源包生成指令序列

- points
  - ~~api~~
    - 简单图形的点集生成
    - 点集编辑（旋转，移动，缩放等）

- setblock
  - api
    - ~~基本命令~~
    -  批量方块生成
    - 方块移动动画
    - 方块放置动画
  - 应用
    - 像素画
    - midi可视化

- particle
  - ~~api~~
    - 基本命令
    - 批量粒子生成
  - 应用
    - ~~粒子画~~
    - midi可视化

- tp
  - api
    - 基本命令
    - tp动画（实体，玩家）

- summon
  - api
    - 基本命令
    - 批量召唤
    - 特殊数据计算（如运动）

- data
  - api
    - 基本命令
  - 应用
    - 盔甲架钢琴动画

## 开发原因以及随便聊聊

​		这个项目是我在初学python时编写的，大概是19年11月完成的项目，也是我的第一个python项目，这一版出于时间原因，只修改了一些太过于不规范的代码，仍然存在很多不规范的地方（再改就是重构了）。~~（顺便也修了几个bug）~~如果有兴趣，也欢迎来贡献代码。我会把我的更新计划放在后面。

​		在19年时，创作MC特效、剪辑、音乐类视频环境还是不错的，数据也比较可观。之前也加了两个群玩玩，发现经常有提问的，当时有些指令通过查中文Wiki也查不到，只能去英文Wiki查，其次人太多，群友也不可能问一个详细答一个，只能指出一个大概方向，告诉你制作xxx的前置技能是啥。比如粒子这种创意很多的玩法很多时候就要通过程序或者复杂的指令实现。

​		但对于一个普通的游戏玩家，尤其只想简单制作一些作品作为娱乐而已，去学习程序是比较痛苦的事情。学了程序还没完，虽然只是玩个游戏指令，但有些地方也需要专业知识，比如计算有些图形需要线代，像素画需要懂点色彩空间，优化一些指令在游戏中的效率需要相应算法。所以我将自己制作视频的一套工具整理开源了。

​		开源这些工具能帮助到真正想发挥自己创意去创作的人，同时也会有人利用它一键生成一大堆视频投稿，想着跟热度盈利（这个行为看似没什么，但会影响到其他在认真创作的作者的感受）。或者制作存档扔到各种论坛，平台上卖。或者把它移植成mod，扔到各种论坛，平台上卖。（但作为开源项目，也管不了你，玩的开心就好。不过对于移植的说一句，里面很多算法存在bug，我自己到现在都没把所有功能使用过）

写在最后，与本项目无关的内容：

如果想去创作，那就去吧，不要过于在意你是否做的好。（但这并不是鼓励你低创）

希望你是由你的兴趣去创作，而不是完全为了赢得他人的赞赏创作你不喜欢的东西。

坚持一份爱好挺好。