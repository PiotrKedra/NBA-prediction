import pandas as pd
from matplotlib import pyplot

# test_data.plot(kind='scatter', x='GAME_ID', y='REB_away')
# pyplot.show()

games = pd.read_csv('resource/games.csv')
games_details = pd.read_csv('resource/games_details.csv')
print(len(games))
print(len(games_details))

games_details.drop(['TEAM_ABBREVIATION', 'TEAM_CITY', 'PLAYER_ID', 'PLAYER_NAME', 'START_POSITION', 'COMMENT', 'MIN'], axis=1, inplace=True)
# drop this because they are already in games table
games_details.drop(['PTS', 'FG_PCT', 'FT_PCT', 'FG3_PCT', 'AST', 'REB'], axis=1, inplace=True)
df = games_details.groupby(['GAME_ID', 'TEAM_ID']).agg({'FGM': 'sum',
                                                        'FGA': 'sum',
                                                        'FG3M': 'sum',
                                                        'FG3A': 'sum',
                                                        'FTM': 'sum',
                                                        'FTA': 'sum',
                                                        'OREB': 'sum',
                                                        'DREB': 'sum',
                                                        'STL': 'sum',
                                                        'BLK': 'sum',
                                                        'TO': 'sum',
                                                        'PF': 'sum',
                                                        'PLUS_MINUS': 'mean'
                                                        })


# games.sort_values('GAME_ID', inplace=True, ignore_index=False)
# games_details.sort_values('GAME_ID', inplace=True, ignore_index=False)
# print('sorted')
# game_full_details = []
# wrong_games = []
# next_index = 0
# for index_G, game_row in games.iterrows():
#     print(index_G)
#     game_id = game_row['GAME_ID']
#     player_per_game = []
#     next_game = False
#     for i in range(next_index, len(games_details)):
#         if game_id == games_details.iloc[i]['GAME_ID']:
#             player_per_game.append(games_details.iloc[i])
#             next_game = True
#         elif next_game is True:
#             next_index = i
#             break
#
# print('wrong games: ' + str(len(wrong_games)))

