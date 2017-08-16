from ctypes import *
msvcrt = cdll.msvcrt
p = c_long(0)
print("python value = ",p.value)
msvcrt.printf(b"ctypes value = %d",p);
msvcrt.fflush(0);