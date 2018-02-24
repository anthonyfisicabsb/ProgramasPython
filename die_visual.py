import pygal
from die import Die

die_1 = Die(8)
die_2 = Die(8)
die_3 = Die(6)

results = []
for roll_num in range(100000):
    result = die_1.roll() + die_2.roll() + die_3.roll()
    results.append(result)

frequencies = []
hist = pygal.Bar()
hist.x_labels = list()

max_results = die_1.num_sides + die_2.num_sides + die_3.num_sides
for value in range(3, max_results + 1):
    frequency = results.count(value)
    frequencies.append(frequency)
    hist.x_labels.append(str(value))

hist.title = "Results of rolling two D8 and one D6 1000 times."
hist.x_title = "Result"
hist.y_title = "Frequency of result"

hist.add('D8 +D8 +D6', frequencies)
hist.render_to_file('die_visual.svg')
