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

    stats = []
    for ele in season2019['HOME_TEAM_ID'].unique():
        stats.append({
            'team_id': ele,
            'home': pd.DataFrame(columns=used_columns),
            'away': pd.DataFrame(columns=used_columns)
        })

    for index, row in season2019.iterrows():
        home_id = row['HOME_TEAM_ID']
        away_id = row['VISITOR_TEAM_ID']
        home_stat_i = None
        away_stat_i = None
        is_home = False
        is_away = False
        for i in range(len(stats)):
            if stats[i]['team_id'] == home_id:
                home_stat_i = i
                if len(stats[i]['home']) != 0:
                    is_home = True
            elif stats[i]['team_id'] == away_id:
                away_stat_i = i
                if len(stats[i]['away']) != 0:
                    is_away = True

        if is_home is True and is_away is True:

            home_stats = stats[home_stat_i]['home']
            away_stats = stats[away_stat_i]['away']

            matches = matches.append({
                'GAME_DATE_EST': row['GAME_DATE_EST'],
                'GAME_ID': row['GAME_ID'],
                'HOME_TEAM_ID': home_id,
                'VISITOR_TEAM_ID': away_id,
                'SEASON': row['SEASON'],
                'FG_PCT_home': home_stats['FG_PCT_home'].mean(),
                'FT_PCT_home': home_stats['FT_PCT_home'].mean(),
                'REB_home': home_stats['REB_home'].sum(),
                'FG_PCT_away': away_stats['FG_PCT_away'].mean(),
                'FT_PCT_away': away_stats['FT_PCT_away'].mean(),
                'REB_away': away_stats['REB_away'].sum(),
                'HOME_TEAM_WINS': row['HOME_TEAM_WINS'],
                'FG3M_home': home_stats['FG3M_home'].sum(),
                'FG3A_home': home_stats['FG3A_home'].sum(),
                'DREB_home': home_stats['DREB_home'].sum(),
                'STL_home': home_stats['STL_home'].sum(),
                'TO_home': home_stats['TO_home'].sum(),
                'PF_home': home_stats['PF_home'].sum(),
                'FG3M_away': away_stats['FG3M_away'].sum(),
                'FG3A_away': away_stats['FG3A_away'].sum(),
                'DREB_away': away_stats['DREB_away'].sum(),
                'STL_away': away_stats['STL_away'].sum(),
                'TO_away': away_stats['TO_away'].sum(),
                'PF_away': away_stats['PF_away'].sum(),
            }, ignore_index=True)

            stats[home_stat_i]['home'] = stats[home_stat_i]['home'].append(row)
            stats[away_stat_i]['away'] = stats[away_stat_i]['away'].append(row)
            if len(stats[home_stat_i]['home']) >= 6:
                stats[home_stat_i]['home'] = stats[home_stat_i]['home'].iloc[1:]
            if len(stats[away_stat_i]['away']) >= 6:
                stats[away_stat_i]['away'] = stats[away_stat_i]['away'].iloc[1:]

        else:
            stats[home_stat_i]['home'] = stats[home_stat_i]['home'].append(row)
            stats[away_stat_i]['away'] = stats[away_stat_i]['away'].append(row)

            if len(stats[home_stat_i]['home']) >= 6:
                stats[home_stat_i]['home'] = stats[home_stat_i]['home'].iloc[1:]
            if len(stats[away_stat_i]['away']) >= 6:
                stats[away_stat_i]['away'] = stats[away_stat_i]['away'].iloc[1:]

    print(matches)


print('Size of data: ' + str(len(matches)))
matches.to_csv(r'resource\stats_5_match_back.csv', index=False)