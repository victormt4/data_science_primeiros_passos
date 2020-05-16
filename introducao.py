import pandas as pd
import matplotlib.pyplot as plt

dataset = pd.read_csv('./ml-latest-small/ratings.csv')

print('Media: ', dataset.rating.mean())
print('Mediana: ', dataset.rating.median())

dataset.rating.plot(kind='hist')
plt.show()
