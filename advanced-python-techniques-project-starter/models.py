"""Represent models for near-Earth objects and their close approaches.

The `NearEarthObject` class represents a near-Earth object. Each has a unique
primary designation, an optional unique name, an optional diameter, and a flag
for whether the object is potentially hazardous.

The `CloseApproach` class represents a close approach to Earth by an NEO. Each
has an approach datetime, a nominal approach distance, and a relative approach
velocity.

A `NearEarthObject` maintains a collection of its close approaches, and a
`CloseApproach` maintains a reference to its NEO.

The functions that construct these objects use information extracted from the
data files from NASA, so these objects should be able to handle all of the
quirks of the data set, such as missing names and unknown diameters.

You'll edit this file in Task 1.
"""

from datetime import datetime

from helpers import datetime_to_str
import math


class NearEarthObject:
    """A near-Earth object (NEO).

    An NEO encapsulates semantic and physical parameters about the object, such
    as its primary designation (required, unique), IAU name (optional), diameter
    in kilometers (optional - sometimes unknown), and whether it's marked as
    potentially hazardous to Earth.

    A `NearEarthObject` also maintains a collection of its close approaches -
    initialized to an empty collection, but eventually populated in the
    `NEODatabase` constructor.
    """

    def __init__(
        self,
        designation: str,
        name: str = None,
        diameter: float = float("nan"),
        hazardous: bool = False,
        approaches: list = None,
    ):
        """Create a new `NearEarthObject`.

        :param designation: The primary designation for this `NearEarthObject`.
        :param name: The IAU name for this `NearEarthObject`.
        :param diameter: The diameter, in kilometers, of this `NearEarthObject`.
        :param hazardous: Whether or not this `NearEarthObject` is potentially hazardous.
        :param approaches: A collection of this `NearEarthObject`'s close approaches to Earth.
        """
        self.designation = designation
        self.name = name
        self.diameter = diameter
        self.hazardous = hazardous
        self.approaches = approaches if approaches else []

    @property
    def fullname(self):
        """Return a representation of the full name of this NEO."""
        return f"{self.designation} ({self.name})" if self.name else self.designation

    def __str__(self):
        """Return `str(self)`."""
        if self.diameter and not math.isnan(self.diameter):
            diameter_str = f"a diameter of {self.diameter:.3f} km"
        else:
            diameter_str = "an unknown diameter"
        hazardous_str = (
            "potentially hazardous" if self.hazardous else "not potentially hazardous"
        )
        return f"NEO {self.fullname} has {diameter_str} and is {hazardous_str}."

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (
            f"NearEarthObject(designation={self.designation!r}, name={self.name!r}, "
            f"diameter={self.diameter:.3f}, hazardous={self.hazardous!r})"
        )

    def serialize(self):
        """Serialize this `NearEarthObject` into a dictionary."""
        return {
            "designation": self.designation,
            "name": self.name,
            "diameter_km": self.diameter,
            "potentially_hazardous": self.hazardous,
        }


class CloseApproach:
    """A close approach to Earth by an NEO.

    A `CloseApproach` encapsulates information about the NEO's close approach to
    Earth, such as the date and time (in UTC) of closest approach, the nominal
    approach distance in astronomical units, and the relative approach velocity
    in kilometers per second.

    A `CloseApproach` also maintains a reference to its `NearEarthObject` -
    initially, this information (the NEO's primary designation) is saved in a
    private attribute, but the referenced NEO is eventually replaced in the
    `NEODatabase` constructor.
    """

    def __init__(
        self, designation: str, time: datetime, distance: float, velocity: float
    ):
        """Create a new `CloseApproach`.

        :param designation: the designation of the NearEarthObject` that is making a
                            close approach to Earth.
        :param time: The date and time, in UTC, at which the NEO passes closest to Earth.
        :param distance: The nominal approach distance, in astronomical units, of the NEO
                         to Earth at the closest point.
        :param velocity: The velocity, in kilometers per second, of the NEO relative to
                         Earth at the closest point.
        """
        self._designation = designation
        self.time = time
        self.distance = distance
        self.velocity = velocity

        # Create an attribute for the referenced NEO, originally None.
        self.neo = None

    @property
    def time_str(self):
        """Return a formatted representation of this `CloseApproach`'s approach time.

        The value in `self.time` should be a Python `datetime` object. While a
        `datetime` object has a string representation, the default representation
        includes seconds - significant figures that don't exist in our input
        data set.

        The `datetime_to_str` method converts a `datetime` object to a
        formatted string that can be used in human-readable representations and
        in serialization to CSV and JSON files.
        """
        return datetime_to_str(self.time)

    def __str__(self):
        """Return `str(self)`."""
        neo_str = self.neo.fullname if self.neo else self._designation
        return (
            f"At {self.time_str}, '{neo_str}' approaches Earth at a distance of "
            f"{self.distance:.2f} au and a velocity of {self.velocity:.2f} km/s."
        )

    def __repr__(self):
        """Return `repr(self)`, a computer-readable string representation of this object."""
        return (
            f"CloseApproach(time={self.time_str!r}, distance={self.distance:.2f}, "
            f"velocity={self.velocity:.2f}, neo={self.neo!r})"
        )

    def serialize(self, flatten=False):
        """
        Serialize this `CloseApproach` into a dictionary.

        :param flatten: if true, include attributes from `self.neo` in the top level dict,
                        otherwise include them as a sub-dictionary.
        """
        serialized = {
            "datetime_utc": self.time_str,
            "distance_au": self.distance,
            "velocity_km_s": self.velocity,
        }
        serialized_neo = self.neo.serialize()
        if flatten:
            serialized = {**serialized, **serialized_neo}
        else:
            serialized["neo"] = serialized_neo
        return serialized
