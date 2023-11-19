import pandas as pd

# select the first 4000 rows and the last 2000 rows of dataset train.csv and save it as is_churn.csv

train_url = 'https://drive.google.com/file/d/1KrjZf19Q4PI7lyRDpAbGcGxkoUUKrPL1/view?usp=sharing'
train_url = 'https://drive.google.com/uc?id=' + train_url.split('/')[-2]
train_df1 = pd.read_csv(train_url).head(4000)
train_df2 = pd.read_csv(train_url).tail(2000)
train_df = pd.concat([train_df1, train_df2])

train_df.to_csv('is_churn.csv', encoding='utf-8', index=False)

# select the rows of dataset transactions.csv whose 'msno' is in is_churn.csv and save it as transactions.csv

transaction_path = '/Users/liuying/Downloads/transactions.csv'
transaction_df = pd.read_csv(transaction_path)
transaction_filtered = transaction_df[transaction_df['msno'].isin(churn_df['msno'])]

transaction_filtered.to_csv('transactions.csv', encoding='utf-8', index=False)

# select the rows of dataset members.csv whose 'msno' is in is_churn.csv and save it as members.csv

members_path = '/Users/liuying/Downloads/members_v3.csv'
members_df = pd.read_csv(members_path)
menmbers_filtered = members_df[members_df['msno'].isin(churn_df['msno'])]

menmbers_filtered.to_csv('members.csv', encoding='utf-8', index=False)

# select the rows of dataset user_logs.csv whose 'msno' is in is_churn.csv and save it as user_logs.csv

user_logs_path = '/Users/liuying/Downloads/user_logs.csv'
user_logs_df = pd.read_csv(user_logs_path)
user_logs_filtered = user_logs_df[user_logs_df['msno'].isin(churn_df['msno'])]

user_logs_filtered.to_csv('user_logs.csv', encoding='utf-8', index=False)




