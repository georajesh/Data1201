import pandas as pd
pd.set_option('display.max_columns', 500)

df = pd.read_csv('data/video_game_sales11.csv')


# 1. Shooters in PS4
# #Filter for PS4
# df_ps4 = df[df['Platform'] =='PS4']
# #Filter for Shooter
# df_shooter = df[df['Genre']=='Shooter']

# shooter_df = df_shooter.groupby(['Platform'])['Name'].count().reset_index()
# print(shooter_df)



# # 2. Global Sales for Nintendo in 2010 - 21
# # print unique values of platform
# # print(df['Platform'].unique())
# nintendo_l = ['Wii','NES','GB','DS','X360','PS3','PS2','SNES','GBA','3DS','PS4','N64','PS','XB','PC','2600','PSP']
# nintendo_df = df[df['Platform'].isin(nintendo_l)]
# #print(nintendo_df.head())


# nintendo = nintendo_df[(nintendo_df['Year'] >= 2000) & nintendo_df['Year'] <= 2010]
# global_nintendo = nintendo['Global_Sales'].sum()
# print(f"Global sales for nintendo is {global_nintendo}")



# 3 The average global sales by Decade
df.loc[((df['Year'] >= 1980) & (df['Year'] < 1990)), 'Decade'] = '1980s'
df.loc[((df['Year'] >= 1990) & (df['Year'] < 2000)), 'Decade'] = '1990s'
df.loc[((df['Year'] >= 2000) & (df['Year'] < 2010)), 'Decade'] = '2000s'
df.loc[(df['Year'] >= 2010), 'Decade'] = '2010+'

salesby_decade = df.groupby(['Decade']).mean('Global_Sales').reset_index()
print(salesby_decade)

