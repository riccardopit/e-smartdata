'''
Using the pickle built-in module, save the following list to the data.pickle file.
ids = ['001', '003', '011']
'''

import pickle


ids = ['001', '003', '011']
with open('data.pickle', 'wb') as f:
    pickle.dump(ids, f)
