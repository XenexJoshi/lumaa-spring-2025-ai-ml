import pandas as pd
import model

# Update to change number of recommendations
COUNT = 5

# Importing the data from the data.csv file 
df = pd.read_csv('data.csv')

# Appending plot_synopsis and tags to allow model to use both columns to recommend movies
df['processed'] = df['plot_synopsis'] + ' ' + df['tags']

text = input('Enter the movie prompt: ')

# Outputs the results in a suitable readable format
model.generate_result(text, df, COUNT)