package main

import (
	"C"
)

// This is required to export function
//export Fib
func Fib(n int) int {
	if n == 0 || n == 1 {
		return n
	} else {
		return Fib(n-1) + Fib(n-2)
	}
}

func main() {}
