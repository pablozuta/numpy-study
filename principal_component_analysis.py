import numpy as np 
from sklearn.decomposition import PCA 
import matplotlib.pyplot as plt

# generate random data
np.random.seed(0)
data = np.random.rand(100, 3)

# perform PCA
pca = PCA(n_components=2)
principal_components = pca.fit_transform(data)


# print explained variance ratio
print("Explained variance ratio: ", pca.explained_variance_ratio_)

# plot the principal components
plt.scatter(principal_components[:, 0], principal_components[:, 1])
plt.title("Principal Component")
plt.xlabel("PC1")
plt.ylabel("PC2")
plt.show()