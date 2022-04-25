import matplotlib.pyplot as plt

x_values = list(range (1,11))
y_values = [x**3 for x in x_values]

plt.scatter (x_values, y_values, c=y_values, cmap=plt.cm.Reds, edgecolors ='none', s=30)

plt.title("Cubid Numbers", fontsize=24)
plt.xlabel("Value", fontsize=14)
plt.ylabel("Cubid of Value", fontsize=14)

plt.tick_params(axis='both', which='major', labelsize=14)
plt.show()