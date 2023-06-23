from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

# ============ Load dataset ============
#df = pd.read_csv("../dataset/"+config['dataset_name'])
df = pd.read_csv('../dataset/HV1_G1_RadarRight_ClutterRemoved_100samples.csv')
data = df.to_numpy()

data_set = data.reshape(960, 90, 189)
Xtr = data_set[18]

Y = np.linspace(0, 90, 90)
X = np.linspace(0, 189, 189)
Y, X = np.meshgrid(X, Y)
Z = Xtr

fig = plt.figure()
ax = Axes3D(fig)
ax.plot_surface(X, Y, Z, cmap='coolwarm')

ax.set_xlabel('X values')
ax.set_ylabel('Y values')
ax.set_zlabel('Z values')
#plt.title("3D Plot")
plt.show()
