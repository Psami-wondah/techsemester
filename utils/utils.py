import math


def distance_between_points(lat1, lng1, lat2, lng2):
    R = 6371e3
    φ1 = lat1 * math.pi / 180
    φ2 = lat2 * math.pi / 180
    Δφ = (lat2 - lat1) * math.pi / 180
    Δλ = (lng2 - lng1) * math.pi / 180
    a = (math.sin(Δφ / 2) * math.sin(Δφ / 2)) + (
        math.cos(φ1) * math.cos(φ2) * math.sin(Δλ / 2) * math.sin(Δλ / 2)
    )
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    d = R * c
    return d
