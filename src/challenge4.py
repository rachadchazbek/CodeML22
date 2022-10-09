import pandas as pd

vulnerabilities = ['CWE-119', 'CWE-120', 'CWE-476', 'CWE-468', 'CWE-other']
columns = ['ID', 'function_source', 'CWE-119',
           'CWE-120', 'CWE-476', 'CWE-468', 'CWE-other']
# Path to dataset
path = './data/participants_dataset.csv'

dataset = pd.read_csv(path, names=columns)
print(dataset)
