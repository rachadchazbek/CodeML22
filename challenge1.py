# importing libraries
import pandas as pd
import tensorflow as tf
 
# need to modify the path based on the machine
df = pd.read_csv("CodeML22 datasets\language-identification-datasets.csv")

# split dataframe in 2 sets
train = df[df['Language'].notnull()]
test = df[df['Language'].isnull()]

# splits the train data into x
train_x = train.drop("ID", axis = 1)
train_x = train_x.drop("Language", axis = 1)
# splits the train data into y
train_y = train.drop("ID", axis = 1)
train_y = train_y.drop("Text", axis = 1)

print(train_x)
print(train_y)

