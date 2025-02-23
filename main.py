import pandas as pd
import model

COUNT = 5

df = pd.read_csv('data.csv')
df['processed'] = df['plot_synopsis'] + ' ' + df['tags']

text = input('Enter the movie prompt: ')
model.generate_result(text, df, COUNT)