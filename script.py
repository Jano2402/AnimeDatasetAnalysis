import pandas as pd
import numpy as np
import matplotlib.pyplot as plt 

df = pd.read_csv('anime.csv')

# How many animes are TV, OVA, etc.
# Type of anime graph 
count = df["Type"].value_counts()

# First graph 
count.plot(kind='bar')
plt.xlabel('Type')
plt.ylabel('Quantity')
plt.title('Anime Types')
plt.tight_layout()



# 10 Greatest anime scores
df['Score'] = pd.to_numeric(df['Score'], errors='coerce') # Converting the values to numeric
top10 = df.nlargest(10, "Score")

# Second graph
plt.figure(figsize=(10, 6))
bars = plt.bar(top10['Name'], top10['Score'])
plt.xlabel('Name')
plt.ylabel('Score')
plt.title('Top 10 Scores')
plt.xticks(rotation=45)  # Rotates tags because they are too long
plt.tight_layout()

for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        yval + 0,
        f'{yval:.1f}',
        ha='center',
        va='bottom'
    )



# 10 Worst anime scores
less10 = df.nsmallest(10, "Score")

# Third graph
plt.figure(figsize=(10, 6))
bars = plt.bar(less10['Name'], less10['Score'])
plt.xlabel('Name')
plt.ylabel('Score')
plt.title('Less 10 Scores')
plt.xticks(rotation=45)  # Rotates tags because they are too long
plt.tight_layout()

for bar in bars:
    yval = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        yval + 0,
        f'{yval:.1f}',
        ha='center',
        va='bottom'
    )



# Animes with the most episodes


# This shows all the graphs
plt.show()