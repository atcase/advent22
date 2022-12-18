from dataclasses import dataclass, field
from functools import reduce
from re import match

@dataclass
class Point:
    x: int
    y: int

@dataclass
class SensorDistance:
    sensor_pos: Point
    beacon_pos: Point
    distance: int = field(init=False)

    def __post_init__(self):
        self.distance = abs(self.sensor_pos.x - self.beacon_pos.x) + abs(self.sensor_pos.y - self.beacon_pos.y)

@dataclass(order=True)
class Range:
    start: int
    end: int

    @classmethod
    def merge(cls, merged: "list[Range]", rhs: "Range"):
        if not merged:
            return [rhs]
        lhs = merged[-1]
        if lhs.start <= rhs.start <= lhs.end:
            merged[-1] = Range(lhs.start, max(lhs.end, rhs.end))
        elif rhs.start <= lhs.start <= rhs.end:
            merged[-1] = Range(rhs.start, max(lhs.end, rhs.end))
        else:
            merged.append(rhs)
        return merged

    def count(self):
        return self.end - self.start + 1

data = open("input")

readings = []
pat = r".*x=(-?\d+), y=(-?\d+).*x=(-?\d+), y=(-?\d+)"
for line in data:
    reading = [int(p) for p in match(pat, line).groups()]
    readings.append(reading)

# convert readings to sensor/beacon distances
sensor_distances: list[SensorDistance] = []
for sx, sy, bx, by in readings:
    manhattan_distance = abs(sx - bx) + abs(sy - by)
    sensor_distances.append(SensorDistance(Point(sx, sy), Point(bx, by)))

# calculate a single row
y = 2000000

# get ranges for each sensor for this row
ranges: list[Range] = []
for sd in sensor_distances:
    y_distance = abs(y - sd.sensor_pos.y)
    x_delta = sd.distance - y_distance
    if x_delta < 0:
        continue
    r = Range(sd.sensor_pos.x - x_delta, sd.sensor_pos.x + x_delta)
    ranges.append(r)
ranges.sort()

# merge any overlapping ranges
merged_ranges = reduce(Range.merge, ranges, [])

# count number of scanned cells
count = sum([r.count() for r in merged_ranges])

# subtract beacons on this row
beacons_this_row = set()
for sd in sensor_distances:
    if sd.beacon_pos.y == y:
        beacons_this_row.add(sd.beacon_pos.x)
count -= len(beacons_this_row)

print(count)
