import pandas as pd

is_churn_url = 'https://drive.google.com/file/d/1ht-gdHgbzcVVR6pNzMk0EAvCzwuLRNl1/view?usp=sharing'
is_churn_url = 'https://drive.google.com/uc?id=' + is_churn_url.split('/')[-2]
is_churn_df = pd.read_csv(is_churn_url)

transactions_url = 'https://drive.google.com/file/d/1Oxa2j6mIVSlNcMDjwHWPc45gEEKuN5LE/view?usp=sharing'
transactions_url = 'https://drive.google.com/uc?id=' + transactions_url.split('/')[-2]
transactions_df = pd.read_csv(transactions_url)

user_logs_url = 'https://drive.google.com/file/d/1SYU8tvSsl-JceeLRml6Vf22VcN0oatBA/view?usp=sharing'
user_logs_url = 'https://drive.google.com/uc?id=' + user_logs_url.split('/')[-2]
user_logs_df = pd.read_csv(user_logs_url)

members_url = 'https://drive.google.com/file/d/14Cs1efsS8hUDzqZTDbYn4nroTbVyrjuN/view?usp=sharing'
members_url = 'https://drive.google.com/uc?id=' + members_url.split('/')[-2]
members_df = pd.read_csv(members_url)
