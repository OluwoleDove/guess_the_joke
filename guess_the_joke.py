import numpy as np
import pandas as pd
from numpy import random
# Load the dataset
df = pd.read_csv("guess_the_joke/datasource/dataset.csv")
df.dropna(inplace = True)

df.describe()

data = df.loc[df['text'].str.contains('Why') | df['text'].str.contains('What')]
data.groupby(['humor']).count()

new_array = data.to_numpy()
true_array = []
false_array = []
my_array = []
for i in new_array:
    if i[-1] == True:
        true_array.append(i[0])
    else:
        false_array.append(i[0])
        
my_array.append(true_array)
my_array.append(false_array)

my_joke = random.choice(random.choice(my_array, p=[len(true_array)/len(new_array), 1 - (len(true_array)/len(new_array))]))
if my_joke in true_array:
    print(f'{my_joke} IS HUMOROUS')
else:
    print(f'{my_joke} is NOT HUMOROUS')