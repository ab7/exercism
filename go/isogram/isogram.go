// Package isogram provides a utility function to check
// if a string input is an isogram.
package isogram

import "unicode"

/*
IsIsogram determines if an input string is an isogram.
An isogram is a word without repeating letters.

Examples of an isogram:
  - isogram
  - background
Words that are not isograms:
  - isograms
  - setting

Spaces and hyphens are allowed to appear multiple times.
*/
func IsIsogram(s string) bool {
	set := make(map[rune]bool)
	for _, c := range s {
		if c == ' ' || c == '-' {
			continue
		}
		lowerCase := unicode.ToLower(c)
		if set[lowerCase] {
			return false
		}
		set[lowerCase] = true
	}
	return true
}
