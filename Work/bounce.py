# bounce.py
#
# Exercise 1.5

height = 100 # The ball is dropped from 100 metres.
rebound_factor = 3/5 # The ball bounces only 3/5 its orignal height every bounce.

for i in range(10):
    print(round(height*rebound_factor, 4)) # round function to round to the 4th decimal place.
    height = height*rebound_factor