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
	
	df.to_csv("./codingassignments/test.csv")



def ranked_choice(): 
	pass

def proportional_voting(): 
	pass




def exhaustive_election(candidates): 
	vote_count = [0 for _ in range(len(candidates))]
	for _ in range(100000):
		# prob = random.random()
		
		### NEED TO FIGURE OUT HOW TO DO SOME VOTING SYSTEM THAT ISN'T RANDOM		
	pass


def exhaustive_ballot(): 
	candidates = ['A', 'B', 'C', 'D', 'E']

	while len(candidates_ordering) > 1: 
		vote_count = exhaustive_election(candidates)

		if no candidate reaches half of total votes: 
			remove candidate with fewest votes
		else: 
			candidate with most votes is winner
		
		if there is a winner: 
			break


	return candidate


	""" 
	Questions for students to answer: 
	1) Find an example of where this type of system is being used.
	2) Why is this system not more commonly-used? In other words, what are the disadvantages?

	"""


def main(): 

	voter_preferences = pd.read_csv("./codingassignments/test.csv")

	for x in ['First', 'Second', 'Third', 'Fourth', 'Fifth']: 
		print(voter_preferences[x].value_counts())
	#print(type(voter_preferences['First'].value_counts()))



