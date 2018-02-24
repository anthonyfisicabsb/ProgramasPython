import matplotlib.pyplot as plt

x_values = list(range(0,5001))
y_values=list()

for x in x_values:
    y_values.append(x*x*x)

plt.scatter(x_values,y_values,c="green",s=20)
plt.title("Cubic Numbers",fontsize=12)
plt.xlabel("Value",fontsize=12)
plt.ylabel("Cubic Value",fontsize=12)

plt.axis([0,500,0,125000000])

plt.show()
