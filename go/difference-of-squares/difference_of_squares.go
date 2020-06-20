// Package diffsquares implements utility functions to calculate the
// difference between the square of the sum and the sum of the
// squares of N natural numbers.
package diffsquares

// SquareOfSum calculates the square of the sum for the first n natural numbers.
func SquareOfSum(n int) int {
	sum := 0
	for i := 1; i <= n; i++ {
		sum += i
	}
	return sum * sum
}

// SumOfSquares calculates the sum of the square of the first n natural numbers.
func SumOfSquares(n int) int {
	sum := 0
	for i := 1; i <= n; i++ {
		sum += i * i
	}
	return sum
}

// Difference calculates the difference of SquareOfSum and SumOfSquares output.
func Difference(n int) int {
	return SquareOfSum(n) - SumOfSquares(n)
}
