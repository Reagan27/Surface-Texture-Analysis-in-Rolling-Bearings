import numpy as np
import matplotlib.pyplot as plt

# Parameters
slip_ratios = np.linspace(0, 1, 100)
temperature_rise = 100 * slip_ratios**2

plt.figure(figsize=(12, 6))

#   Temperature Rise vs. Slip Ratios
plt.subplot(1, 2, 1)
plt.plot(slip_ratios, temperature_rise, label="Temperature Rise")
plt.xlabel("Slip Ratio")
plt.ylabel("Temperature Rise (°C)")
plt.title("Influence of Slip Ratios on Contact Area Temperature Rise")
plt.grid(True)
plt.legend()

# Dimple Parameters
plt.subplot(1, 2, 2)
dimple_depth = 0.01
dimple_diameter = 0.3
dimple_spacing = 0.2
plt.bar([1], [dimple_depth], width=0.2, label="Dimple Depth")
plt.bar([2], [dimple_diameter], width=0.2, label="Dimple Diameter")
plt.bar([3], [dimple_spacing], width=0.2, label="Dimple Spacing")
plt.xticks([1, 2, 3], ["Depth", "Diameter", "Spacing"])
plt.ylabel("Dimension (mm)")
plt.title("Contact Area Texture Parameters")
plt.grid(True)
plt.legend()

plt.tight_layout()
plt.show()
