import matplotlib.pyplot as plt

def quint(num):
    return 3*num**5 - 2*num**4 + 4*num**3 - 26*num**2 - 28*num +48

x_values = list(range(-200,200))
y_values = list()

for x in x_values:
    y_values.append(quint(x))

plt.plot(x_values,y_values)

plt.xlabel("Value",fontsize=10)
plt.ylabel("F(x)",fontsize=10)

plt.axis([-200,200,min(y_values),max(y_values)])

plt.show()
