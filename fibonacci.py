import sys

from ctypes import cdll, c_uint64

lib = cdll.LoadLibrary("./fibonacci.so")
lib.Fib.argtype = c_uint64
lib.Fib.restype = c_uint64

go_fib = lib.Fib


def fib(n):
    if n == 0 or n == 1:
        return n
    else:
        return fib(n - 1) + fib(n - 2)
  

if __name__ == "__main__":
    if 3 < len(sys.argv) < 2:
        raise AttributeError
    elif len(sys.argv) == 2:
        n = int(sys.argv[1])
        ans = fib(n)
        print(f"{n}-th Fibonnaci:\t{ans}")
    elif len(sys.argv) == 3:
        if sys.argv[1] == "--go":
            n = int(sys.argv[2])
            ans = go_fib(n)
            print(f"{n}-th Fibonnaci:\t{ans}")
    else:
        raise AttributeError

        