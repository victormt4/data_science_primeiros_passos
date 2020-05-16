import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

movies = pd.read_csv('./tmdb_5000/tmdb_5000_movies.csv')

print(movies.original_language.unique())  # valores únicos

language_freq = movies['original_language'].value_counts().to_frame().reset_index()
language_freq.columns = ['original_language', 'count']  # alterando nome das colunas

sns.barplot(data=language_freq, x='original_language', y='count')
plt.show()

sns.catplot(data=movies, kind='count', x="original_language")
plt.show()
