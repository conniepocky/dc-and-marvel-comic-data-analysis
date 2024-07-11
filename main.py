import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

dcdf = pd.read_csv('data/dc-wikia-data.csv')
marveldf = pd.read_csv('data/marvel-wikia-data.csv')

dcdf.rename(columns={'YEAR':'Year'}, inplace=True)

dcdf['Publisher'] = 'DC'
marveldf['Publisher'] = 'Marvel'

df = pd.concat([dcdf, marveldf]) 

#order by apperarances

df = df.sort_values(by='APPEARANCES', ascending=False)

#change names, clean up and remove brackets

df['name'] = df['name'].str.replace('\([^()]*\)', '', regex=True).str.title()

df = df[df['ID'] != 'Identity Unknown']

df = df[df["ALIGN"] != "Reformed Criminals"]

df = df.reset_index(drop=True)

print(df.head(10))

# distribution of first appearance 

dcFirst = plt.figure()

plt.title("DC Distribution of first appearance by year")

sns.histplot(dcdf["Year"], bins=20, kde=True, color='violet')

marvelFirst = plt.figure()

plt.title("Marvel Distribution of first appearance by year")

sns.histplot(marveldf["Year"], bins=20, kde=True, color='orange')

#plot the top 10 characters by appearances

top10 = plt.figure(figsize=(10, 5))

colors = ['red', 'dodgerblue']

sns.barplot(x='APPEARANCES', y='name', data=df.head(10), hue='Publisher', palette=colors)
x = df.head(10)['APPEARANCES']
y = df.head(10)['name']

plt.ylabel('Name')
plt.xlabel("Appearances")

plt.yticks(fontsize=8)

for index, value in enumerate(x):
    plt.text(value, index,
             str(value))
    
plt.title("Top 10 characters by appearances")
    
# good bad and neutral character distribution

goodBadNeutral = plt.figure()

sns.countplot(x='ALIGN', data=df, hue='Publisher', palette=colors)

plt.xlabel("Alignment")
plt.title("Character Alignment Distribution by Publisher")

plt.tight_layout()
plt.show()

