 """ Puzzle: Casting a deciding vote
In your small town, you are one of 101 voters choosing amongst 3 candidates for mayor. 
Everyone besides you will vote randomly for 1 of the 3 candidates. The highest vote getter 
will be the winner (ties mean no winner). We're interested in the following question:
what are the odds that you cast the deciding vote that propels your preferred candidate to 
victory? Run through the election many times (e.g. 10,000), each time computing whether 
the election has the characteristic described, and then let us know the proportion of 
times where you would cast the deciding vote.
"""
import random 

def simulation(): 
	""" Returns percentage of times that user represents the
	deciding vote. 

	n - number of times simulation runs
	deciding_vote - number of times user is the deciding vote
	vote_count - a list of the three candidates [cand1, cand2, cand3]; each element is
	 		number of voters that voted for the candidate

	Noted section can be commented if user only wants the odds that user will be
	deciding vote. Noted section will print the characteristics of the election. It 
	should print TRUE if the user is a deciding vote. 
	"""

	n, deciding_vote = 0, 0
	while n < 10000: 
		vote_count = [0, 0, 0]
		election(vote_count)
		n += 1
		cand1, cand2, cand3 = vote_count[0], vote_count[1], vote_count[2]
		# BEGIN COMMENTED SECTION
		if (cand1 == cand2 and cand1 > cand3) or (cand1 == cand3 and cand1 > cand2) or (cand2 == cand3 and cand2 > cand1): 
			# assuming preferred candidate is Candidate #1
			deciding_vote += 1
			print(n, deciding_vote, vote_count, True)
		else: 
			print(n, deciding_vote, vote_count)
		# END COMMENTED SECTION
	return str((deciding_vote / n) * 100) + '%'

def election(vote_count): 
	for i in range(100): 
		vote = random.randint(0, 2)
		vote_count[vote] += 1





