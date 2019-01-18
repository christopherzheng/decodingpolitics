#!/usr/bin/env python
# coding: utf-8

# # Lab 1: Using Python to Simulate Hypothetical Elections

# Welcome to our class! We are excited to provide an introduction to how technology and data can be used for political analysis. 
# 
# Each week, you will complete a lab like this one in order to reinforce technical concepts and see practical applications towards political topics. Hands on practice is the best way to grasp technical concepts, so completing labs are important for your conceptual knowledge.
# 
# This class will introduce you to Python. This coding langugage is one of the most popular langugages to learn programming with and will help lay the foundations for future programming in classes such as Data 8 or CS61A.

# Labs are important and make up 5% of the class grade. They also count towards the "effort" category. If you have any questions about anything covered in the labs or lecture, please feel free to reach out to us! Additionally, as data science and technical classes are collaborative in nature, we encourage collaboration among you and your classmates. However, there are limits to this, which are sharing code and directly providing answers to others.

# ### Today's Lab- Using Python to Simulate Hypothetical Elections

# In today's lab, you will learn how to:
# 
# 1. Practice writing and evaluating expressions in Python. 
# 2. Understand what functions are and how they can be used to make code more efficient.
# 3. Learn what different parts of code do.
# 
# This will be in context will this week's political topic: elections.

# #### A Note on Documentation

# In[71]:


# This line is a single line comment- in order to create a comment, you use the "#" symbol. 

""" This is a multi line comment. Comments can be used to indicate what the code 
    that you are writing does, what errors (or bugs) you are running into, etc. 
    In order to create a single lined comment, you use the "#" symbol. 
    Multi line comments use ". These are used primarily for documentation.
    The code below imports data science packages we will use that will help with the analysis conducted in this lab.
    We'd like you to try to add a comment to any code that you write so that we can understand what the function or 
    algorithm is supposed to do.
"""

from datascience import *
import numpy as np


# ## 1. Casting a Deciding Vote

# In your small town, you are one of 101 voters choosing amongst 3 candidates for mayor. 
# Everyone besides you will vote randomly for 1 of the 3 candidates. The highest vote getter will be the winner (ties mean no winner). 
# 
# We're interested in the following question: what are the odds that you cast the deciding vote that propels your preferred candidate to victory? Run through the election many times (e.g. 10,000), each time computing whether 
# the election has the characteristic described, and then let us know the proportion of 
# times where you would cast the deciding vote.

# In[72]:


import random 

def simulation():
    """ Returns percentage of times that user represents the deciding vote. 
    
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
        
election_result = simulation()
election_result


# #### 1.1 Running through the simulation, what is the proportion of times where you cast the deciding vote?

# 6.959...%

# #### 1.2 What conditions need to be true for you to be the deciding vote?

# There needs to be a tie between two of the three candidates

# #### 1.3 How does this number change as you run through it multiple times? What is the factor accounting for the change?

# The proportion can go up or down. The factor that is accounting for this change is simply the random integer that is being generated in the "election" function.

# ## 2. The Electoral College

# "The Electoral College consists of 538 electors. A majority of 270 electoral votes is required to elect the President. Electoral votes are allocated among the states based on the Census. Every state is allocated a number of votes equal to the number of senators and representatives in its U.S. Congressional delegation—two votes for its senators in the U.S. Senate plus a number of votes equal to the number of its members in the U. S. House of Representatives." 
# 
# -National Archives and Records Administration
# 
# One state constantly in electoral college news is Florida. Following the 2000 elections, Florida made headlines not only for its election processes, but also for the electoral college determining the presidency, diverging from the popular vote result. 
# 
# This next question follows a simulation using the data from the more recent 2016 presidential election and 2010 census, which can be found here (https://www.archives.gov/federal-register/electoral-college/allocation.html).

# In[73]:


# This code is creating two arrays and then joining them together as a table. Don't worry about tables for right now, we'll learn
# more about them in the next couple of weeks. Basically, two arrays have been joined together to create a table to better
# visualize the electoral college 

import random 

allocated_reps_states = make_array("Alabama", "Alaska", "Arizona", "Arkansas", "California", "Colorado", 
                            "Connecticut", "Delaware", "District of Columbia", "Florida", "Georgia", 
                            "Hawaii", "Idaho", "Illinois", "Indiana", "Iowa", "Kansas", "Kentucky", 
                            "Louisiana", "Maine", "Maryland", "Massachusetts", "Michigan", "Minnesota",
                            "Mississippi", "Missouri", "Montana", "Nebraska", "Nevada", "New Hampshire", 
                            "New Jersey", "New Mexico", "New York", "North Carolina", "North Dakota",
                            "Ohio", "Oklahoma", "Oregon", "Pennsylvania", "Rhode Island", "South Carolina",
                            "South Dakota", "Tennessee", "Texas", "Utah", "Vermont", "Virginia", "Washington", 
                            "West Virginia", "Wisconsin", "Wyoming")

allocated_state_numbers = make_array(9, 3, 11, 6, 55, 9, 
                                     7, 3, 3, 29, 16,
                                     4, 4, 20, 11, 6, 6, 8,
                                     8, 4, 10, 11, 16, 10, 
                                     6, 10, 3, 5, 6, 4,
                                     14, 5, 29, 15, 3,
                                     18, 7, 7, 20, 4, 9, 
                                     3, 11, 38, 6, 3, 13, 12, 
                                     5, 10, 3)

allocated_states_2016 = Table().with_columns("States", allocated_reps_states,
                                             "Numbers of Electoral College Representatives", allocated_state_numbers)
allocated_states_2016.show(51)


# Using two functions called max() and min(), we can generate the state with the highest and lowest electoral college representatives.

# #### 2.1 What is the highest number of electorates among all the states? Which state(s) is/are this?

# In[74]:


max(allocated_states_2016.column(1))


# In[75]:


max_amount = allocated_states_2016.where("Numbers of Electoral College Representatives", are.equal_to(55))
max_amount


# 55, CA

# #### 2.2 What is the lowest number of electorates among all the states? Which state(s) is/are this?

# In[76]:


min(allocated_states_2016.column(1))


# In[77]:


min_amount = allocated_states_2016.where("Numbers of Electoral College Representatives", are.equal_to(3))
min_amount


# 3, Alaska, Delaware, DC, Montana, North Dakota, South Dakota, Vermont, Wyoming

# In[78]:


import random 

results = make_array()

def election_simulation():
    """ Returns percentage of times that a state represents the deciding vote. 
    
    e - Electoral College number
    allocated_reps - state's allocated representatives for the Electoral college
    a- number of iterations
    
    """
    # If electoral college votes for candidate A, TRUE, else FALSE

    e = 538
    a, allocated_reps = 0, 51
    
    while a < allocated_reps:
        x = random.choice([True, False])
        changed_results = np.append(results, x)
        a += 1
    return results

election = election_simulation()
allocated_states_2016 = allocated_states_2016.with_column("Candidate 1 (T) or Candidate 2 (F)", results)
allocated_states_2016


# ## 3. The Presidential Hunger Games

# Assume that we are in an apocalyptic society where we can only "reap" from a pool of past presidents. We determine the two candidates from random integers from 1-10 and then flip a coin to determine the winner. We have created a function for you 

# In[103]:


#num_presidents = make_array(1,2,3,4,5,6,7,8,9,10)
list_of_presidents = make_array("George Washington", "Thomas Jefferson", "Abraham Lincoln", "Theodore Rooesevelt",
                                "Dwight D. Eisenhower", "John F. Kennedy", "Ronald Reagan", 
                                "Bill Clinton", "George W. Bush", "Barack Obama")


def candidates():
    x = random.randint(1,10)
    y = random.randint(1,10)
    z = (list_of_presidents.item(x), list_of_presidents.item(y))
    return(print("The candidates are " + list_of_presidents.item(x), "and " + list_of_presidents.item(y) + ". " + 
                 "The winner is " + random.choice(z)))

election_result = candidates()
election_result


# ## 4. Ranked Choice Voting (?)

# Is this a good idea? i'm not really sure what too much will be for questions

# In[ ]:




