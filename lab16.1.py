import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi/3, np.pi/3, 1000)

y = 3.22 * np.exp(0.1 * x) + np.tan(x)

plt.figure(figsize=(8, 6))
plt.plot(x, y, linestyle='-.', color='blue', label=r"$y=3.22e^{0.1x}+\tan{x}$")
plt.title("Графік функції")
plt.xlabel("x")
plt.ylabel("y")
plt.axhline(0, color="black", linewidth=0.5)
plt.axvline(0, color="black", linewidth=0.5)
plt.legend()
plt.grid(True)

plt.savefig("drawings.jpg")
plt.show()
