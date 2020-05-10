// Package raindrops implements routines to process
// numbers into raindrop sounds.
package raindrops

import "strconv"

// Convert returns raindrop sounds based on the factor of an integer.
// The rules of `raindrops` are that if a given number:
//
// - has 3 as a factor, add 'Pling' to the result.
// - has 5 as a factor, add 'Plang' to the result.
// - has 7 as a factor, add 'Plong' to the result.
// - does not have any of 3, 5, or 7 as a factor,
//   the result should be the digits of the number.
func Convert(n int) string {
	sound := ""
	if n%3 == 0 {
		sound += "Pling"
	}
	if n%5 == 0 {
		sound += "Plang"
	}
	if n%7 == 0 {
		sound += "Plong"
	}
	if sound == "" {
		return strconv.Itoa(n)
	}
	return sound
}
