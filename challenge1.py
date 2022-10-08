# importing libraries
import pandas as pd
import tensorflow as tf
 
# need to modify the path based on the machine
df = pd.read_csv("CodeML22 datasets\language-identification-datasets.csv")

#============================================

# split dataframe in 2 sets
train = df[df['Language'].notnull()]
# probably won't need test because we don't know the answer (y)
test = df[df['Language'].isnull()]

# splits the train data into x
x = train.drop("ID", axis = 1)
x = x.drop("Language", axis = 1)
# splits the train data into y
y = train.drop("ID", axis = 1)
y = y.drop("Text", axis = 1)

#print(x)
#print(y)


