import pandas as pd
from sklearn.linear_model import LinearRegression, LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score


pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

evaluated_df = pd.read_csv('resource/stats_5_match_back_mean.csv')
evaluated_df.drop([
    'GAME_DATE_EST',
    'GAME_ID',
    'HOME_TEAM_ID',
    'VISITOR_TEAM_ID'
], axis=1, inplace=True)
print(evaluated_df)

season2019 = evaluated_df.loc[evaluated_df['SEASON'] == 2019]
season2019.drop(['SEASON'], axis=1, inplace=True)
y_season2019 = season2019['HOME_TEAM_WINS']
x_season2019 = season2019.drop('HOME_TEAM_WINS', axis=1)

training = evaluated_df.loc[evaluated_df['SEASON'] == 2018]
training.drop(['SEASON'], axis=1, inplace=True)
y_train = training['HOME_TEAM_WINS']
x_train = training.drop('HOME_TEAM_WINS', axis=1)

print(x_season2019)
print(x_train)

lin_reg = LinearRegression()
lin_reg.fit(x_train, y_train)
lin_reg_pred = lin_reg.predict(x_season2019)
acc_lin_reg = accuracy_score(y_season2019, lin_reg_pred.round())


log_reg = LogisticRegression(max_iter=23000)
log_reg.fit(x_train, y_train)
log_reg_pred = log_reg.predict(x_season2019)
acc_log_reg = accuracy_score(y_season2019, log_reg_pred)

random_forest = RandomForestClassifier()
random_forest.fit(x_train, y_train)
random_forest_pred = random_forest.predict(x_season2019)
acc_random_forest = accuracy_score(y_season2019, random_forest_pred)

print('Linear regression acc: ', acc_lin_reg)
print('Logistic regression acc: ', acc_log_reg)
print('Random forest acc: ', acc_random_forest)

