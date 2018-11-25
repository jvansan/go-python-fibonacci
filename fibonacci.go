package main

import (
	"C"
)

// Fib is a simple recursive Fibonacci function
// This is required to export function
//export Fib
func Fib(n uint64) uint64 {
	if n == 0 || n == 1 {
		return n
	}
	return Fib(n-1) + Fib(n-2)
}

func main() {}
