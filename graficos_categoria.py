import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

movies = pd.read_csv('./tmdb_5000/tmdb_5000_movies.csv')

print(movies.original_language.unique())  # valores únicos

language_count = movies['original_language'].value_counts().to_frame().reset_index()
language_count.columns = ['original_language', 'total']  # alterando nome das colunas

sns.barplot(data=language_count, x='original_language', y='total')
plt.show()

# sns.catplot(data=movies, kind='count', x="original_language")
# plt.show()

total_en = movies['original_language'].value_counts().loc['en']
total_other = movies['original_language'].value_counts().sum() - total_en

data = pd.DataFrame({
    'language': ['english', 'other'],
    'total': [total_en, total_other]
})
sns.barplot(data=data, x='language', y='total')
plt.show()

sns.catplot(data=movies.query('original_language != "en"'), kind='count', x="original_language")
plt.show()
