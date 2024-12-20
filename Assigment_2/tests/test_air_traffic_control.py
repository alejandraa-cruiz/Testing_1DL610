import pytest
from pytest import mark
from Assigment_2.air_traffic_control import air_traffic_control

@mark.parametrize(
    "runway_clear, alternate_runway_available, plane_speed, emergency, wind_speed, visibility, airport_traffic, priority_status, expected_decision",
    [
        (True, True, 100, False, 30, 2000, 5, False, "Landing Allowed"),    #PC 1
        (True, False, 150, False, 40, 1000, 4, False, "Landing Denied"),    #PC 2
        (False, True, 100, False, 40, 600, 4, False, "Landing Denied"),     #PC 3
        (False, False, 80, True, 35, 1500, 3, True, "Landing Allowed"),     #PC 4
        (True, True, 100, False, 40, 2000, 5, False, "Landing Allowed"),    #CC 1
        (True, False, 160, False, 40, 2000, 6, False, "Landing Denied"),    #CC 2
        (False, True, 100, False, 40, 800, 3, False, "Landing Denied"),     #CC 3
        (False, False, 100, True, 50, 600, 2, True, "Landing Allowed"),     #CC 4
        (True, True, 100, False, 40, 2000, 5, False, "Landing Allowed"),    # CC 5
        (False, True, 100, False, 40, 2000, 5, False, "Landing Allowed"),   # CC 6
        (True, False, 100, False, 40, 2000, 5, False, "Landing Allowed"),   # CC 7
        (True, True, 160, False, 40, 2000, 5, False, "Landing Denied"),     # CC 8
        (True, True, 100, True, 40, 2000, 5, False, "Landing Denied"),      # CC 9
        (True, True, 100, False, 45, 2000, 5, False, "Landing Denied"),     # CC 10
        (True, True, 100, False, 40, 800, 5, False, "Landing Denied"),      # CC 11
        (True, True, 100, False, 40, 2000, 8, False, "Landing Denied"),     # CC 12
        (True, True, 100, False, 40, 2000, 8, True, "Landing Allowed"),     # CC 13
        (True, True, 100, False, 50, 2000, 5, True, "Landing Allowed"),     # CC 14
        (True, True, 100, True, 40, 2000, 5, True, "Landing Allowed"),      # CC 15
    ],
)

def test_air_traffic_control(
        runway_clear,
        alternate_runway_available,
        plane_speed,
        emergency,
        wind_speed,
        visibility,
        airport_traffic,
        priority_status,
        expected_decision,
):
    result = air_traffic_control(runway_clear, alternate_runway_available, plane_speed, emergency, wind_speed, visibility, airport_traffic, priority_status)
    assert result == expected_decision
