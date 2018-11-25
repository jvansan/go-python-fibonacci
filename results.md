## Architecture

*MacBook Air (13-inch, 2017)*
*macOS Mojave v10.14*
*1.8 GHz Intel Core i5*
*8 GB 1600 MHz DDR3*


## Summary

| *N*  | Python (s) | Go (s) |
|------|------------|--------|
|  10  |  0.06      |  0.05  |
|  20  |  0.06      |  0.06  |
|  30  |  0.56      |  0.06  |
|  40  |  54.52     |  0.85  |
|  50  |  7004.33   | 114.97 |


## Larger N Results

`time python fibonacci.py --go 40`

Output:

```
40-th Fibonnaci:        102334155
python fibonacci.py --go 40  0.85s user 0.02s system 99% cpu 0.874 total
```

`time python fibonacci.py 40`

Output:

```
40-th Fibonnaci:        102334155
python fibonacci.py 40  54.52s user 0.17s system 98% cpu 55.390 total
```

`time python fibonacci.py --go 50`

Output:

```
50-th Fibonnaci:        -298632863
python fibonacci.py --go 50  101.47s user 0.60s system 98% cpu 1:43.11 total
```

**This is clearly an overflow problem and a reminder to be careful in defining C and Go types.**

**Bug fixed**

```
50-th Fibonnaci:        12586269025
python fibonacci.py --go 50  114.97s user 0.65s system 96% cpu 1:59.50 total
```


`time python fibonacci.py 50`

Output:

```
50-th Fibonnaci:        12586269025
python fibonacci.py 50  7004.33s user 33.46s system 61% cpu 3:12:10.30 total
```