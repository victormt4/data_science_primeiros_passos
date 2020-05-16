import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ratings = pd.read_csv('./ml-latest-small/ratings.csv')

print('Media: ', ratings.rating.mean())
print('Mediana: ', ratings.rating.median())

plt.title('Historiograma da frequencia das notas:')
ratings.rating.plot(kind='hist')
plt.show()

plt.title('Boxplot da frequencia das notas:')
# plt.figure(figsize=(5, 5))
sns.boxplot(ratings.rating)
plt.show()

movies = pd.read_csv('./ml-latest-small/movies.csv')

ratings_per_movie = ratings.groupby('movieId').mean().rating

plt.title('Historiograma da media das notas por filme:')
ratings_per_movie.plot(kind='hist')
plt.show()

plt.title('Boxplot da media das notas por filme:')
sns.boxplot(ratings_per_movie)
plt.show()

plt.title('Historiograma da media das notas por filme usando Seaborn:')
sns.distplot(ratings_per_movie)
plt.show()
