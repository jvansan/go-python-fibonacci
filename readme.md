# go-python-fibonacci

A simple test of wrapping a Go function for use in Python code.

To test this the naive recursive function for calculating the n-th Fibonacci
number is used.

First build the Go shared library which is then called from Python using the
`ctypes` 
[foreign function library](https://docs.python.org/3/library/ctypes.html).

## Software

`python 3.5+`

`go version go1.11.1+`

## Build instructions

`go build -o fibonacci.so -buildmode=c-shared fibonacci.go`

## Usage

*Python version*

`python fibonacci.py INPUT`

*Go version*

`python fibonacci.py --go INPUT`

*Output*

`INPUT-th Fibonacci number: OUTPUT`

----

See `results.md` for speed test results.

**Useful Resources**

* [this article](https://medium.com/learning-the-go-programming-language/calling-go-functions-from-other-languages-4c7d8bcc69bf), 
* `ctypes` documentation
