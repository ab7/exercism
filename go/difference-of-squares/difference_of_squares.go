// Package diffsquares implements utility functions to calculate the
// difference between the square of the sum and the sum of the
// squares of N natural numbers.
package diffsquares

// SquareOfSum calculates the square of the sum for the first n natural numbers.
// See Faulhaber's formula.
func SquareOfSum(n int) int {
	return ((n * (n + 1)) / 2) * ((n * (n + 1)) / 2)
}

// SumOfSquares calculates the sum of the square of the first n natural numbers.
// See Faulhaber's formula.
func SumOfSquares(n int) int {
	return (n * (n + 1) * (2*n + 1)) / 6
}

// Difference calculates the difference of SquareOfSum and SumOfSquares output.
func Difference(n int) int {
	return SquareOfSum(n) - SumOfSquares(n)
}
