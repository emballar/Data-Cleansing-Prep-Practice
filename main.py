import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

df = pd.read_csv('assignment_seven.csv')

#remove names
df = df.drop(columns=['full_name'])

#remove rows with missing values
df = df.dropna()

#download new data frame as output.csv
df.to_csv('output.csv')

#find the top 5 products in the data frame
top5 = df['products'].value_counts()[:5]

print('The top 5 purchased products are \n', top5)

#create new dframe with top 5 and make a viz
top5df = pd.DataFrame({'product' :['Acetaminophen','Ibuprofen','TITANIUM DIOXIDE', 'ALCOHOL', 'Salicylic Acid'], 'frequency' : [13,10,10,8,8]})

sns.set(style="whitegrid")

plt.title('Top 5 Purchased Products', fontsize=20)

sns.barplot(x="product", y="frequency", color="b", data = top5df)

plt.tick_params(axis='x', which='major', labelsize=8)

plt.savefig('top5viz.png')

plt.show()