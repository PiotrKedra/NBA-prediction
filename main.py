import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

games = pd.read_csv('resource/games.csv')
games_details = pd.read_csv('resource/games_details.csv')

games.drop(['TEAM_ID_home', 'TEAM_ID_away'], axis=1, inplace=True)

games_details.drop(['TEAM_ABBREVIATION', 'TEAM_CITY', 'PLAYER_ID', 'PLAYER_NAME', 'START_POSITION', 'COMMENT', 'MIN'],
                   axis=1, inplace=True)
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
games.sort_values('GAME_ID', inplace=True, ignore_index=False)

columns = ['GAME_DATE_EST',
           'GAME_ID',
           'GAME_STATUS_TEXT',
           'HOME_TEAM_ID',
           'VISITOR_TEAM_ID',
           'SEASON',
           'PTS_home',
           'FG_PCT_home',
           'FT_PCT_home',
           'FG3_PCT_home',
           'AST_home',
           'REB_home',
           'PTS_away',
           'FG_PCT_away',
           'FT_PCT_away',
           'FG3_PCT_away',
           'AST_away',
           'REB_away',
           'HOME_TEAM_WINS',
           'FGM_home',
           'FGA_home',
           'FG3M_home',
           'FG3A_home',
           'FTM_home',
           'FTA_home',
           'OREB_home',
           'DREB_home',
           'STL_home',
           'BLK_home',
           'TO_home',
           'PF_home',
           'PLUS_MINUS_home',
           'FGM_away',
           'FGA_away',
           'FG3M_away',
           'FG3A_away',
           'FTM_away',
           'FTA_away',
           'OREB_away',
           'DREB_away',
           'STL_away',
           'BLK_away',
           'TO_away',
           'PF_away',
           'PLUS_MINUS_away',]

MERGED = pd.DataFrame(columns=columns)
for i in range(0, len(df)):
    print(i)
    for j, game in games.iterrows():
        if game['GAME_ID'] == df.iloc[i].name[0]:
            if df.iloc[i].name[0] != df.iloc[i+1].name[0]:
                break
            if df.iloc[i].name[1] == game['HOME_TEAM_ID']:
                home_index = i
                away_index = i+1
            else:
                home_index = i + 1
                away_index = i
            MERGED = MERGED.append({
                'GAME_DATE_EST': game['GAME_DATE_EST'],
                'GAME_ID': game['GAME_ID'],
                'GAME_STATUS_TEXT': game['GAME_STATUS_TEXT'],
                'HOME_TEAM_ID': game['HOME_TEAM_ID'],
                'VISITOR_TEAM_ID': game['VISITOR_TEAM_ID'],
                'SEASON': game['SEASON'],
                'PTS_home': game['PTS_home'],
                'FG_PCT_home': game['FG_PCT_home'],
                'FT_PCT_home': game['FT_PCT_home'],
                'FG3_PCT_home': game['FG3_PCT_home'],
                'AST_home': game['AST_home'],
                'REB_home': game['REB_home'],
                'PTS_away': game['PTS_away'],
                'FG_PCT_away': game['FG_PCT_away'],
                'FT_PCT_away': game['FT_PCT_away'],
                'FG3_PCT_away': game['FG3_PCT_away'],
                'AST_away': game['AST_away'],
                'REB_away': game['REB_away'],
                'HOME_TEAM_WINS': game['HOME_TEAM_WINS'],
                'FGM_home': df.iloc[home_index]['FGM'],
                'FGA_home': df.iloc[home_index]['FGA'],
                'FG3M_home': df.iloc[home_index]['FG3M'],
                'FG3A_home': df.iloc[home_index]['FG3A'],
                'FTM_home': df.iloc[home_index]['FTM'],
                'FTA_home': df.iloc[home_index]['FTA'],
                'OREB_home': df.iloc[home_index]['OREB'],
                'DREB_home': df.iloc[home_index]['DREB'],
                'STL_home': df.iloc[home_index]['STL'],
                'BLK_home': df.iloc[home_index]['BLK'],
                'TO_home': df.iloc[home_index]['TO'],
                'PF_home': df.iloc[home_index]['PF'],
                'PLUS_MINUS_home': df.iloc[home_index]['PLUS_MINUS'],
                'FGM_away': df.iloc[away_index]['FGM'],
                'FGA_away': df.iloc[away_index]['FGA'],
                'FG3M_away': df.iloc[away_index]['FG3M'],
                'FG3A_away': df.iloc[away_index]['FG3A'],
                'FTM_away': df.iloc[away_index]['FTM'],
                'FTA_away': df.iloc[away_index]['FTA'],
                'OREB_away': df.iloc[away_index]['OREB'],
                'DREB_away': df.iloc[away_index]['DREB'],
                'STL_away': df.iloc[away_index]['STL'],
                'BLK_away': df.iloc[away_index]['BLK'],
                'TO_away': df.iloc[away_index]['TO'],
                'PF_away': df.iloc[away_index]['PF'],
                'PLUS_MINUS_away': df.iloc[away_index]['PLUS_MINUS'],
            }, ignore_index=True)
            games.drop(j)
            break
    if i == 1000:
        break

print(MERGED)

