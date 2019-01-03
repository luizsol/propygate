# We start by importing the Measurement class

from propygate import Measurement

# Now we create some measurements

# This is one way of creating a measurement of 10 ± 0.2
m1 = Measurement(10, error=0.2)

# This is another way
m1 = Measurement(10, 0.2)  # Easy, right?

# Now you can treat this measurement (mostly) as any other numeric variable
# in python

# You can add it to other measurements
m2 = Measurement(4.4, 0.05)
print(m1 + m2)  # 14.4 ± 0.20615528128088306

# Subtract them
print(m1 - m2)  # 5.6 ± 0.20615528128088306

# Divide them
print(m1 / m2)  # 2.2727272727272725 ± 0.05227926003669418

# Multiply them
print(m1 * m2)  # 44.0 ± 1.0121264743103995

# Exponentiate them (but not one by another!)
import math

print(m1 ** (math.pi))  # 1385.1601859244622 ± 87.02961448163397

# You can also use python's default numeric types to make your calculations

print(3.333 + m2)  # 7.7330000000000005 ± 0.05

# But sadly there are some drawbacks to this package, here are them

# Using math standard functions such as sqrt, sin, cos etc. will fail
try:
    print(math.sqrt(m1))
except:
    print('Told ya!')

# For this more advanced stuff you may want to use the uncertainties
# (https://pythonhosted.org/uncertainties/) package

# Here's a tip: instead of using sqrt just exponentiate it to 1/2:

print(m1 ** (1 / 2))  # 3.1622776601683795 ± 0.0316227766016838
