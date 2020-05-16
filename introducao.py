import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dataset = pd.read_csv('./ml-latest-small/ratings.csv')

print('Media: ', dataset.rating.mean())
print('Mediana: ', dataset.rating.median())

dataset.rating.plot(kind='hist')
plt.show()

sns.boxplot(dataset.rating)
plt.show()
