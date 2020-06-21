class SpaceAge:
    """Utilities for calculating Earth age based on solar system orbital periods.

    The following describes orbital periods in relation to Earth:
        - Earth: orbital period 365.25 Earth days, or 31557600 seconds
        - Mercury: orbital period 0.2408467 Earth years
        - Venus: orbital period 0.61519726 Earth years
        - Mars: orbital period 1.8808158 Earth years
        - Jupiter: orbital period 11.862615 Earth years
        - Saturn: orbital period 29.447498 Earth years
        - Uranus: orbital period 84.016846 Earth years
        - Neptune: orbital period 164.79132 Earth years
    """
    def __init__(self, seconds: int) -> None:
        self.seconds = seconds

    def _calculate_age(self, period: float) -> float:
        """Return Earth age in years for given orbital period."""
        earth_year_in_sec = 31557600
        return round(self.seconds / (earth_year_in_sec * period), 2)

    def on_earth(self) -> float:
        """Return age based on orbital period of Earth."""
        period = 1
        return self._calculate_age(period)

    def on_mercury(self) -> float:
        """Return age based on orbital period of Mercury."""
        period = 0.2408467
        return self._calculate_age(period)

    def on_venus(self) -> float:
        """Return age based on orbital period of Venus."""
        period = 0.61519726
        return self._calculate_age(period)

    def on_mars(self) -> float:
        """Return age based on orbital period of Mars."""
        period = 1.8808158
        return self._calculate_age(period)

    def on_jupiter(self) -> float:
        """Return age based on orbital period of Jupiter."""
        period = 11.862615
        return self._calculate_age(period)

    def on_saturn(self) -> float:
        """Return age based on orbital period of Saturn."""
        period = 29.447498
        return self._calculate_age(period)

    def on_uranus(self) -> float:
        """Return age based on orbital period of Uranus."""
        period = 84.016846
        return self._calculate_age(period)

    def on_neptune(self) -> float:
        """Return age based on orbital period of Neptune."""
        period = 164.79132
        return self._calculate_age(period)
