// Package leap implements routines to perform
// leap year anaylsis based on the Gregorian calendar.
package leap

// IsLeapYear calculates if the given input is a leap year.
func IsLeapYear(y int) bool {
	result := false
	if y%100 == 0 {
		if y%400 == 0 {
			result = true
		}
	} else if y%4 == 0 {
		result = true
	}
	return result
}
