import pandas as pd
from matplotlib import pyplot

test_data = pd.read_csv('resource/games.csv')
print(test_data)

test_data.plot(kind='scatter', x='GAME_ID', y='REB_away')
pyplot.show()

