// Package space implements a simple library to calculate
// the age of a person on the various planets in our solar system.
package space

type Planet string

// Map of one year on each planet in relation to a single Earth year.
var planet_year_map = map[Planet]float64{
	"Mercury": 0.2408467,
	"Venus":   0.61519726,
	"Earth":   1.0,
	"Mars":    1.8808158,
	"Jupiter": 11.862615,
	"Saturn":  29.447498,
	"Uranus":  84.016846,
	"Neptune": 164.79132,
}

const one_earth_year_seconds float64 = 31557600

// Age calculates the age of a person on any planet in our solar system.
// It returns the age in years for the given planet.
func Age(seconds float64, p Planet) float64 {
	adjusted_seconds := planet_year_map[p] * one_earth_year_seconds
	return seconds / adjusted_seconds
}
