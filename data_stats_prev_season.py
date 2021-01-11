import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

evaluated_df = pd.read_csv('resource/evaluated_data.csv')
evaluated_df.dropna(inplace=True)
used_columns = [
    'GAME_DATE_EST',
    'GAME_ID',
    'HOME_TEAM_ID',
    'VISITOR_TEAM_ID',
    'SEASON',
    'FG_PCT_home',
    'FT_PCT_home',
    'REB_home',
    'FG_PCT_away',
    'FT_PCT_away',
    'REB_away',
    'HOME_TEAM_WINS',
    'FG3M_home',
    'FG3A_home',
    'DREB_home',
    'STL_home',
    'TO_home',
    'PF_home',
    'FG3M_away',
    'FG3A_away',
    'DREB_away',
    'STL_away',
    'TO_away',
    'PF_away']
data = evaluated_df[used_columns]

matches = pd.DataFrame(columns=used_columns)

for season in data['SEASON'].unique():
    print(season)
    season2019 = data.loc[data['SEASON'] == season].sort_values(by=['GAME_DATE_EST'], ascending=False)
    print(season2019)
    home_stat = season2019.groupby(['HOME_TEAM_ID']).agg({
        'FG_PCT_home': 'mean',
        'FT_PCT_home': 'mean',
        'REB_home': 'mean',
        'FG3M_home': 'mean',
        'FG3A_home': 'mean',
        'DREB_home': 'mean',
        'STL_home': 'mean',
        'TO_home': 'mean',
        'PF_home': 'mean',
    })

    away_stat = season2019.groupby(['VISITOR_TEAM_ID']).agg({
        'FG_PCT_away': 'mean',
        'FT_PCT_away': 'mean',
        'REB_away': 'mean',
        'FG3M_away': 'mean',
        'FG3A_away': 'mean',
        'DREB_away': 'mean',
        'STL_away': 'mean',
        'TO_away': 'mean',
        'PF_away': 'mean',
    })

    for index, row in season2019.iterrows():
        home_id = row['HOME_TEAM_ID']
        away_id = row['VISITOR_TEAM_ID']

        home_team = home_stat.iloc[0]
        for i, team in home_stat.iterrows():
            if i == home_id:
                home_team = team
                break

        away_team = away_stat.iloc[0]
        for i, team in away_stat.iterrows():
            if i == away_id:
                away_team = team
                break

        matches = matches.append({
            'GAME_DATE_EST': row['GAME_DATE_EST'],
            'GAME_ID': row['GAME_ID'],
            'HOME_TEAM_ID': home_id,
            'VISITOR_TEAM_ID': away_id,
            'SEASON': row['SEASON'],
            'FG_PCT_home': home_team['FG_PCT_home'],
            'FT_PCT_home': home_team['FT_PCT_home'],
            'REB_home': home_team['REB_home'],
            'FG_PCT_away': away_team['FG_PCT_away'],
            'FT_PCT_away': away_team['FT_PCT_away'],
            'REB_away': away_team['REB_away'],
            'HOME_TEAM_WINS': row['HOME_TEAM_WINS'],
            'FG3M_home': home_team['FG3M_home'],
            'FG3A_home': home_team['FG3A_home'],
            'DREB_home': home_team['DREB_home'],
            'STL_home': home_team['STL_home'],
            'TO_home': home_team['TO_home'],
            'PF_home': home_team['PF_home'],
            'FG3M_away': away_team['FG3M_away'],
            'FG3A_away': away_team['FG3A_away'],
            'DREB_away': away_team['DREB_away'],
            'STL_away': away_team['STL_away'],
            'TO_away': away_team['TO_away'],
            'PF_away': away_team['PF_away'],
        }, ignore_index=True)

    print(matches)


print('Size of data: ' + str(len(matches)))
matches.to_csv(r'resource\stats_prev_season.csv', index=False)
