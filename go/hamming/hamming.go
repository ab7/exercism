// Package hamming implements routines to calculate the
// Hamming Distance between two DNA strands.
package hamming

import "fmt"

// Distance returns the Hamming Distance bewteen
// the provided string inputs that represent DNA strands.
// Only strands of equal length can be processed.
func Distance(a, b string) (int, error) {
	ar, br := []rune(a), []rune(b)
	if len(ar) != len(br) {
		return 0, fmt.Errorf("The length of the DNA strands are not equal: %d != %d",
			len(ar), len(br))
	}
	distance := 0
	for i := range ar {
		if ar[i] != br[i] {
			distance++
		}
	}

	return distance, nil
}
