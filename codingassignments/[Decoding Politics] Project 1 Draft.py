import random
import csv
import numpy as np

candidates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] 


def create_csv(): 
	# DON'T RUN ALL THE TIME
	candidates = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J'] 

	first_choice = []
	for i in range(100000):
		prob = random.random()
		if 0 <= prob < 0.20:
			first_choice.append(candidates[3]) 
			# blah blah blah
		elif 0.20 <= prob < 0.4: 
			first_choice.append(candidates[9])
			# blah blah blah
		elif 0.4 <= prob < 0.5: 
			first_choice.append(candidates[0])
			# blah blah blah
		elif 0.5 <= prob < 0.6: 
			first_choice.append(candidates[6])
			# blah blah blah
		elif 0.6 <= prob < 0.7: 
			first_choice.append(candidates[7])
			# blah blah blah
		elif 0.7 <= prob < 0.77: 
			first_choice.append(candidates[4])
			# blah blah blah
		elif 0.77 <= prob < 0.84: 
			first_choice.append(candidates[5])
			# blah blah blah
		elif 0.84 <= prob < 0.90: 
			first_choice.append(candidates[8])
			# blah blah blah
		elif 0.90 <= prob < 0.95: 
			first_choice.append(candidates[2])
			# blah blah blah
		elif 0.95 <= prob < 1.00: 	
			first_choice.append(candidates[1])

	vote_preferences = []
	for i in range(len(first_choice)):
		copy = candidates[:]
		copy.remove(first_choice[i])
		random.shuffle(copy)
		choice = [first_choice[i]] + copy
		vote_preferences.append(choice)
	vote_preferences.insert(0, ['First', 'Second', 'Third', 'Fourth', 'Fifth', 'Sixth', 'Seventh', 'Eighth', 'Ninth', 'Tenth'])

	with open("./vote-preferences.csv", "wt") as file: 
		writer = csv.writer(file)
		writer.writerows(vote_preferences)

def read_data(): 
	data = np.genfromtxt("./vote-preferences.csv", delimiter=',', dtype=str)
	return data[1:]

def round_of_voting(candidates, data): 
	vote_count = [0 for _ in range(len(candidates))]
	for votes in data:
		while votes[0] not in candidates: 
			votes = votes[1:]
		vote_count[candidates.index(votes[0])] += 1
	return vote_count

def first_past_the_post(candidates, data): 
	vote_count = round_of_voting(candidates, data)
	top_vote_count = max(vote_count)
	return candidates[vote_count.index(top_vote_count)], top_vote_count

def only_top_three(data): 
	top_three = []
	for votes in data: 
		votes = list(votes[:3])
		top_three.append(votes)
	return top_three

def setup_next_round(vote_count, candidates):
	lowest_tally = min(vote_count)

	# there's an index error here
	lowest_index = vote_count.index(lowest_tally)
	candidates.pop(lowest_index) 

def ranked_choice(candidates, data): 
	# data = only_top_three(data) # there's a bug here related to deleting all the candidates
	winner = False
	while not winner: 
		vote_count = round_of_voting(candidates, data)
		print(vote_count, candidates[vote_count.index(max(vote_count))], max(vote_count))
		if max(vote_count) > (len(data) / 2):
			winner = True
		else: 
			setup_next_round(vote_count, candidates)
	return candidates[vote_count.index(max(vote_count))]

def proportional_voting(parties, data): 
	party_count = [0 for _ in range(len(parties))]
	for party_vote in data: 
		party_count[candidates.index(party_vote[0])] += 1

	for i in range(len(party_count)): 
		party_count[i] = (parties[i], party_count[i] / len(data))

	return party_count

def main():
	data = read_data()
	#print(first_past_the_post(candidates, data))
	#ranked_choice(candidates, data)
	print(proportional_voting(candidates, data))

main()





