import pandas as pd

pd.set_option('display.max_columns', None)
pd.set_option('display.width', 1000)

evaluated_df = pd.read_csv('resource/evaluated_data.csv')

print(evaluated_df)
