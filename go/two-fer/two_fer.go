// Package twofer implements routines to process two for one strings.
package twofer

import "fmt"

// ShareWith returns a twofer (two for one) string with optional name input.
func ShareWith(name string) string {
	if name == "" {
		name = "you"
	}
	return fmt.Sprintf("One for %s, one for me.", name)
}
