# importing libraries
import pandas as pd
 
# need to modify the path based on the machine
df = pd.read_csv("CodeML22 datasets\language-identification-datasets.csv")

# split dataframe in 2 sets

trainingDataset = df[df['Language'].notnull()]
evaluationDataset = df[df['Language'].isnull()]

print(trainingDataset)
print(evaluationDataset)