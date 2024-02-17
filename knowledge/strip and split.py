# strip方法，去除字符串两遍的指定字符----------------------
string_one = "   第一个字符串    "
way_one = string_one.strip()      # 默认去除空格
print(way_one)

string_two = "#$^*$#@ 第二个字符串$%^&("
way_two = string_two.strip("@#$%^&*( ")     # 传入参数为什么就去除什么
print(way_two)

# spilt方法，用于给字符串拆分，存储在一个列表中
string_three = "Python Java C C++ JavaScript Go Rust Kotlin Php"
way_three = string_three.split()    # 默认以空格进行拆分
print(way_three)


