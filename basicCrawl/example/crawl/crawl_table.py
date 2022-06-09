import pandas as pd

df_list = pd.read_html('https://www.rottentomatoes.com/critics/latest_reviews/')
df = df_list[2]
df.head()