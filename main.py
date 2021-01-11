import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

evaluated_df = pd.read_csv('resource/stats_5_match_back.csv')
evaluated_df.drop([
    'GAME_DATE_EST',
    'GAME_ID',
    'HOME_TEAM_ID',
    'VISITOR_TEAM_ID'
], axis=1, inplace=True)
print(evaluated_df)

season2019 = evaluated_df.loc[evaluated_df['SEASON'] == 2019]
y_season2019 = season2019['HOME_TEAM_WINS']
x_season2019 = season2019.drop('HOME_TEAM_WINS', axis=1)

training = evaluated_df[evaluated_df['SEASON'] != 2019]
y_train = training['HOME_TEAM_WINS']
x_train = training.drop('HOME_TEAM_WINS', axis=1)

lin_reg = LinearRegression()
lin_reg.fit(x_train, y_train)
acc_lin_reg = round(lin_reg.score(x_season2019, y_season2019) * 100, 2)

log_reg = LogisticRegression(max_iter=23000)
log_reg.fit(x_train, y_train)
acc_log_reg = round(log_reg.score(x_season2019, y_season2019) * 100, 2)

random_forest = RandomForestClassifier()
random_forest.fit(x_train, y_train)
acc_random_forest = round(random_forest.score(x_season2019, y_season2019) * 100, 2)


print('Linear regression acc: ', acc_lin_reg)
print('Logistic regression acc: ', acc_log_reg)
print('Random forest acc: ', acc_random_forest)

