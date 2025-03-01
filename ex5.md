# 1
## Possible measurement noise when timing a program:
- Unusual amount of best/worst cases resulting in skew
- Environment: Other processes/programs
- Python runtime hangups 
## How timeit addresses these issues:
The timeit function attempts to address these issues by repeating the measurement a large amount of times, relying on minimizing the impact of outliers/noise by averaging the large number of tests.

## How repeat addresses these issues:
The repeat function attempts to address these issues by returning a list of test measurements, which can later be inspected for outliers/excessive noise to trim them off if necessary, or use them if that is the intention of the measurement.

# 2
## Appropriate statistic to apply to timeit
The appropriate statistic to apply to the timeit function is average.\
This is because timeit returns a single number that is the sum of all tests.\
It is designed to deal with outliers by running a large number of tests to average them away.\
timeit does not say anything about minimums or maximums by default.

## Appropriate statistics to apply to repeat
The appropriate statistics to apply to the repeat function are min and max.\
This is because unlike timeit, repeat returns a list of measurements.\
This list can be analyzed for the minimums and maximums from the tests done.
