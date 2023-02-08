import csv
import os
import random
import time
from Tresure_hunt_art import *


"""the shortcuts based on + (including the implied use in sum) are, of necessity,
O(L**2) when there are L sublists -- as the intermediate result list keeps getting longer,
at each step a new intermediate result list object gets allocated,
and all the items in the previous intermediate result must be copied over
(as well as a few new ones added at the end). So, for simplicity and without actual loss of generality, 
say you have L sublists of I items each: the first I items are copied back and forth L-1 times, 
the second I items L-2 times, and so on; total number of copies is I times the sum of x for x from 1 to L excluded,
i.e., I * (L**2)/2.

The list comprehension just generates one list, once, and copies each item over (from its original place of residence to the result list) also exactly once.
"""

def flatten(l):
    return [item for sublist in l for item in sublist]
# fucntion to take two lists of riddles and Rounds and return a dictionary

def read_csv_file(file_name):
    # store data in a list
    data = []
    # open csv file
    with open(file_name, 'r') as file:
        # read csv file
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    
    return flatten(data)

def create_dictionary( key_list,riddle_list):
 
    riddle_dictionary = {}
    # loop through the lists
    
    for i in range(len(key_list)):
        # add the key and value to the dictionary
        riddle_dictionary[key_list[i]] = riddle_list[i]
    
    return riddle_dictionary

def create_shortList(riddle_dictionary):
    # create a dictionary of random 10 items
    shortList = {}
    
    # loop through the dictionary
    for i in range(10):
        # get a random key
        key = random.choice(list(riddle_dictionary.keys()))
        # add the key and value to the dictionary
        shortList[key] = riddle_dictionary[key]
        # remove the key from the dictionary
        riddle_dictionary.pop(key)
    
    return shortList
    
    
def play_Treasure_Hunt(round_number):
    
    round_file = 'Round_' + str(round_number) + '.csv'
    
    riddles_list = read_csv_file('riddles.csv')
    keys_list = read_csv_file(round_file)

    # create a dictionary
    riddles = create_dictionary(keys_list, riddles_list)
    riddles = create_shortList(riddles)
    
    keys_list = list(riddles.keys())

    counter = 0
    
    os.system('cls')
    
    print(logo)
    time.sleep(5)
    os.system("cls")
    
    # for debugging
    # for key in keys_list:
    #     print(key)
    
    print("Find the first Key !! \n")
    
    print(riddle_art[counter])
    # print the first riddle from the dictionary
    print(riddles[keys_list[counter]])
    
        
    while(True):
        user_key = input("Enter the key: ").upper()
        
        if(user_key == 'QUIT' or user_key == 'Q'):
            exit()    
            
        time.sleep(1)
        if(user_key == keys_list[counter] and counter < len(keys_list)):
            os.system('cls')
            print("\nCongratulation !! You found the key !!\n")
            print("Next Riddle Unlocked !!\n")
            time.sleep(3)
            os.system('cls')
            counter += 1
            print(riddle_art[counter])
            print(riddles[keys_list[counter]])
        else:
            os.system('cls')
            print("\nOops thats the wrong Key !!\n")
            print(Gameover)
            time.sleep(5)
            break
        
        




keep_playing = True
while(keep_playing):
    os.system('cls')
    print(logo)
    
    round_number = 1
    
    play_Treasure_Hunt(round_number)
    
    os.system('cls')
    if(input(play_again) != 'y'):
        keep_playing= False    