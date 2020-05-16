import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

ratings = pd.read_csv('./ml-latest-small/ratings.csv')

toy_story_ratings = ratings.query('movieId == 1')
jumanji_ratings = ratings.query('movieId == 2')

plt.boxplot([toy_story_ratings['rating'], jumanji_ratings['rating']])
plt.show()

sns.boxplot(x='movieId', y='rating', data=ratings.query('movieId in [1,2]'))
plt.show()
