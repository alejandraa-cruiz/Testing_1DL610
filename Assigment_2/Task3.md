# Task 3
Author: Alejandra Cabrera Ruiz

Implementing two test suites, one that achieves predicate coverage and another one that achieves clause coverage for a selection of 7 clauses.
## Understanding
The `air_traffic_control` file implements a decision-making system over particular conditions that combined determine if a plane is allowed to land or not.

Note:
- Derived predicate `runway_available` is a logical condition resulted from 2 other predicates (`runway_clear` and `alternate_runway_available`)
  - runway_available = `runway_clear` OR `alternate_runway_available`
- Predicate `p` combines conditions `runway_available`, `safe_speed`, `not_emergency`, `safe_weather` and `acceptable_traffic`
  - `p = runway available AND safe speed AND NOT emergency AND safe weather AND acceptable traffic`
  - runway_available is a logical expression but not a clause on its own
  - `p` indirectly includes `runway_clear` and `alternate_runway_available`
  
### Important definitions
- Expression: A combination of variables, constants, and operators (arithmetic or logical) that evaluates to a value.
- Logical expression: An expression that evaluates to a Boolean value (True or False) and can include logical operators like and, or, and not.
- Predicate: Any expression that evaluates to a Boolean value (t/f).
- Clause: basic building block of a predicate. Contains no logical operators.


### Evaluating conditions
The following table condenses the `air_traffic_control` derived conditions, conditions and thresholds that lead to decision_making of the landing status.

| **Condition**                | **Clause Logic**                                                                                                                        | **Evaluates to True When...**                            | **Evaluates to False When...**                          |
|------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|----------------------------------------------------------|---------------------------------------------------------|
| `runway_clear`               | Boolean                                                                                                                                 | Runway is clear (`True`).                                | Runway is not clear (`False`).                          |
| `alternate_runway_available` | Boolean                                                                                                                                 | Alternate runway is available (`True`).                  | No alternate runway is available (`False`).             |
| `emergency`                  | Boolean                                                                                                                                 | Plane is in an emergency (`True`).                       | Plane is not in an emergency (`False`).                 |
| `priority_status`            | Boolean                                                                                                                                 | Plane has priority clearance (`True`).                   | Plane does not have priority clearance (`False`).       |
| `runway_available`           | `runway_clear or alternate_runway_available`                                                                                            | Either runway is clear or alternate is available.        | Both runways are unavailable.                           |
| `safe_speed`                 | `plane_speed < landing_speed_threshold`, <br> `landing_speed_threshold = 150 knots`                                                     | Plane speed < 150 knots.                                 | Plane speed ≥ 150 knots.                                |
| `safe_weather`               | `wind_speed <= max_wind_speed` and `visibility >= min_visibility`, <br> `max_wind_speed = 40 knots` <br> `min_visibility = 1000 meters` | Wind speed ≤ 40 knots and visibility ≥ 1000 m.           | Wind speed > 40 knots or visibility < 1000 m.           |
| `acceptable_trafic`          | `airport_traffic <= max_air_traffic`, <br> `max_air_traffic = 5 planes`                                                                 | 5 or fewer planes are in the airspace.                   | More than 5 planes are in the airspace.                 |
| `traffic_override`           | `priority_status and airport_traffic <= max_air_traffic + 3`                                                                            | Priority status is true and traffic ≤ 8 planes.          | Priority status is false or traffic > 8 planes.         |
| `weather_override`           | `priority_status and not safe_weather`                                                                                                  | Priority status is `True` and `safe_weather` is `False`. | Priority status is `False` or `safe_weather` is `True`. |

### Decision-making 
Expressed in the table are the combination of conditions that lead to particular decisions

| **Decision**    | **Reason**                                 | **Conditions**                                                                                                                                                                                       | **Values That Evaluate Conditions**                                                                                                                                                                                                                                                                                                     |
|-----------------|--------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| Landing Allowed | All conditions met for landing.            | `runway_available = True` and `safe_speed = True` and `not emergency = True` and `safe_weather = True` and `acceptable_traffic = True`                                                               | - `runway_clear = True` or `alternate_runway_available = True` <br> - `plane_speed < 150 knots` <br> - `emergency = False` <br> - `wind_speed ≤ 40 knots` and `visibility ≥ 1000 meters` <br> - `airport_traffic ≤ 5 planes`                                                                                                            |
| Landing Allowed | Landing allowed with priority overrides.   | `runway_available = True` and `safe_speed = True` and `not emergency = True` and (`acceptable_traffic = True` or `traffic_override = True`) and (`safe_weather = True` or `weather_override = True`) | - `runway_clear = True` or `alternate_runway_available = True` <br> - `plane_speed < 150 knots` <br> - `emergency = False` <br> - `airport_traffic ≤ 8 planes` with `priority_status = True` (for `traffic_override`) <br> - Unsafe weather (`wind_speed > 40 knots` or `visibility < 1000 meters`) allowed if `priority_status = True` |
| Landing Allowed | Emergency landing with priority clearance. | `emergency = True` and `priority_status = True`                                                                                                                                                      | - `emergency = True` <br> - `priority_status = True`                                                                                                                                                                                                                                                                                    |
| Landing Denied  | Conditions not met for safe landing.       | All other combinations of conditions where none of the above rules are satisfied.                                                                                                                    | - `runway_clear = False` and `alternate_runway_available = False` <br> - `plane_speed ≥ 150 knots` <br> - `wind_speed > 40 knots` or `visibility < 1000 meters` <br> - `airport_traffic > 8 planes` without priority clearance                                                                                                          |

## Predicate coverage 
In predicate coverage, also known as decision coverage, every logical predicate evaluates at least one to True or False during testing.

### Test suite
Predicate coverage is achieved for `p` because test case 1 evaluates to `True` and test cases 2,3 and 4 evaluate to `False`. For derived predicate `runway_available` test cases 1,2 and 3 evaluate to `True`, while test case 4 evaluates to `False`, achieving also predicate coverage. Is important to notice that the evaluation of `p` does not determine weather the airplane can land and should not be mistaken with the decision-making process. Case 4, for example, overrides the predicate and allows the plane to land due to `emergency = True` and `priority = True`.

| **Case** | `runway_clear` | `alternate_runway_available` | `plane_speed` | `emergency` | `wind_speed` | `visibility` | `airport_traffic` | `priority_status` | **Expected Outcome** |
|----------|----------------|------------------------------|---------------|-------------|--------------|--------------|-------------------|-------------------|----------------------|
| PC 1     | True           | True                         | 100           | False       | 30           | 2000         | 5                 | False             | Landing Allowed      |
| PC 2     | True           | False                        | 150           | False       | 40           | 1000         | 4                 | False             | Landing Denied       |
| PC 3     | False          | True                         | 100           | False       | 40           | 600          | 4                 | False             | Landing Denied       |
| PC 4     | False          | False                        | 80            | True        | 35           | 1500         | 3                 | True              | Landing Allowed      |

### Implementation
Only one function was implemented `test_air_traffic_control` which receives all the parameters defined for the class. For passing the parameters the test uses `mark.parametrize`.

## Clause Coverage
In clause coverage, also known as condition coverage,  each clause must evaluate to both True and False at least once during testing. We will evaluate 7 clauses.

### Test suite
Clause coverage in the test suite is achieved for all classes. I decided not to choose only 7 since I realized with few test cases I could test the complete clause coverage which accounts for guaranteeing to test each clause independently.

| **Case** | `runway_clear` | `alternate_runway_available` | `plane_speed` | `emergency` | `wind_speed` | `visibility` | `airport_traffic` | `priority_status` | **Expected Outcome** |
|----------|----------------|------------------------------|---------------|-------------|--------------|--------------|-------------------|-------------------|----------------------|
| CC 1     | True           | True                         | 100           | False       | 40           | 2000         | 5                 | False             | Landing Allowed      |
| CC 2     | True           | False                        | 160           | False       | 80           | 2000         | 6                 | False             | Landing Denied       |
| CC 3     | False          | True                         | 100           | False       | 40           | 800          | 3                 | False             | Landing Denied       |
| CC 4     | False          | False                        | 100           | True        | 50           | 600          | 2                 | True              | Landing Allowed      |

Demonstration:
1. `runway_clear`:
   - **True** in Case 1 and Case 2.
   - **False** in Case 3 and Case 4.

2. `alternate_runway_available`:
   - **True** in Case 1 and Case 3.
   - **False** in Case 2 and Case 4.

3. `plane_speed < 150` (safe_speed):
   - **True** in Case 1, Case 3, and Case 4 (plane speeds = 100, 100, 100).
   - **False** in Case 2 (plane speed = 160).

4. `emergency`:
   - **False** in Case 1, Case 2, and Case 3 (emergency = False).
   - **True** in Case 4 (emergency = True).

5. `wind_speed <= 40` (safe_weather):
   - **True** in Case 1 and Case 3 (wind speed = 40, 40).
   - **False** in Case 2 and Case 4 (wind speed = 80, 50).

6. `visibility >= 1000` (safe_weather):
   - **True** in Case 1 and Case 2 (visibility = 2000).
   - **False** in Case 3 and Case 4 (visibility = 800, 600).

7. `airport_traffic <= 5` (acceptable_traffic):
   - **True** in Case 3 and Case 4 (airport traffic = 3, 2).
   - **False** in Case 1 and Case 2 (airport traffic = 5, 6).

8. `priority_status`:
   - **False** in Case 1, Case 2, and Case 3 (priority status = False).
   - **True** in Case 4 (priority status = True). 

### Subsumption
My test set for clause coverage subsumes predicate coverage. It evaluates `p` to `True` in CC 1; and to `False` in CC 2, CC 3 and CC 4. For derived predicate `runway_available` it evaluates to `True` in CC 1, CC 2 and CC 3; and to `False` in CC 4.

### Implementation
The same function used in Predicate Coverage testing (`test_air_traffic_control`) was used and only new test values were added, still using `mark.parametrize`.

## Claus Coverage one at a time
To fully demonstrate clause coverage by modifying one clause a time another test set was defined.

### Test Suite
A base case is defined on CC 5 and then only a value at a time is modified. The last 3 test cases test particular conditions (ex. traffic override).

| **Case**  | `runway_clear` | `alternate_runway_available` | `plane_speed` | `emergency` | `wind_speed` | `visibility` | `airport_traffic` | `priority_status` | **Expected Outcome** |
|-----------|----------------|------------------------------|---------------|-------------|--------------|--------------|-------------------|-------------------|----------------------|
| **CC 5**  | True           | True                         | 100           | False       | 40           | 2000         | 5                 | False             | Landing Allowed      |
| **CC 6**  | False          | True                         | 100           | False       | 40           | 2000         | 5                 | False             | Landing Allowed      |
| **CC 7**  | True           | False                        | 100           | False       | 40           | 2000         | 5                 | False             | Landing Allowed      |
| **CC 8**  | True           | True                         | 160           | False       | 40           | 2000         | 5                 | Landing Denied    |
| **CC 9**  | True           | True                         | 100           | True        | 40           | 2000         | 5                 | False             | Landing Denied       |
| **CC 10** | True           | True                         | 100           | False       | 45           | 2000         | 5                 | False             | Landing Denied       |
| **CC 11** | True           | True                         | 100           | False       | 40           | 800          | 5                 | False             | Landing Denied       |
| **CC 12** | True           | True                         | 100           | False       | 40           | 2000         | 8                 | False             | Landing Denied       |
| **CC 13** | True           | True                         | 100           | False       | 40           | 2000         | 8                 | True              | Landing Allowed      |
| **CC 14** | True           | True                         | 100           | False       | 50           | 2000         | 5                 | True              | Landing Allowed      |
| **CC 15** | True           | True                         | 100           | True        | 40           | 2000         | 5                 | True              | Landing Allowed      |

### Implementation
The same function used in Predicate Coverage testing (`test_air_traffic_control`) was used and only new test values were added, still using `mark.parametrize`.