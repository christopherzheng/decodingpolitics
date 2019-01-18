import pandas as pd
import random
import itertools


def create_csv(): 
	# maybe do more candidates/names?
	candidates = ['A', 'B', 'C', 'D', 'E'] 

	candidates_ordering = list(itertools.permutations(candidates))

	votes = []
	for i in range(100000):
		votes.append(candidates_ordering[random.randint(0, len(candidates_ordering) - 1)])

	df = pd.DataFrame(votes, columns=['First', 'Second', 'Third', 'Fourth', 'Fifth'])

	print(df['First'].value_counts())
	
	df.to_csv("./test.csv")




"""
1. Create a better CSV
2. 



"""