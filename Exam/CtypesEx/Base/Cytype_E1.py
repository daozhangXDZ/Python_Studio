# 基本信息和使用printf
from ctypes import *  # @UnusedWildImport

print(windll.kernel32)

msvcrt = cdll.msvcrt
print(msvcrt)

print(msvcrt.printf)
msg_str = b"Hello world!\n"
msvcrt.printf(b"Testing: %s", msg_str)
# 强制刷新缓冲区，立即输出，
# 若无此句，会导致下面的python语句输出结束了才输出下面的字符串
msvcrt.fflush(0);

# 构建并使用C 数据类型
i = c_int(9)
print(i)
print(i.value)

i.value = 1212;
print(i.value)

str_cp = c_char_p(b"learn python ctypes")
print(str_cp)
print(str_cp.value)

str_cp = c_wchar_p("hello python")
print(str_cp)
print(str_cp.value)

# 按引用传参可以使用function(byref(parameter))
# byref(obj[, offset]) Returns a light-weight pointer to obj,
# which must be an instance of a ctypes type. offset defaults to zero,
# and must be an integer that will be added to the internal pointer value.
# byref(obj, offset) corresponds to this C code:
# (((char *)&obj) + offset)
# The returned object can only be used as a foreign function call parameter.
# It behaves similar to pointer(obj), but the construction is a lot faster.
num = c_int()
print("input a int number:")
msvcrt.scanf(b"%d", byref(num))
print(num.value)


# 使用python 定义结构体与共用体
class color_rgb(Structure):
    _fields_ = [
        ('r', c_char),
        ('g', c_char),
        ('b', c_char),
    ]


color = color_rgb()
color.r = 123
color.g = 234
color.b = 222

print(ord(color.b))

color = color_rgb(111, 222, 121)
print(ord(color.b))


# 使用python 定义联合体
class barley(Union):
    _fields_ = [
        ("barley_long", c_long),
        ("barley_int", c_int),
        ("barley_char", c_char * 8)
    ]


val = input("Enter the amount of barley:")
bar = barley(int(val))
print(bar.barley_long, bar.barley_int, bar.barley_char)