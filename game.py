# Rock-paper-scissors-lizard-Spock
import random
# The key idea of this program is to equate the strings
# "rock", "paper", "scissors", "lizard", "Spock" to numbers
# as follows:
#
# 0 - rock
# 1 - Spock
# 2 - paper
# 3 - lizard
# 4 - scissors

# helper functions

def number_to_name(number):
    # fill in your code below
    if(number==0):
        return "rock";
    elif (number==1):
        return "Spock";
    elif (number==2):
        return "paper";
    elif (number==3):
        return "lizard";
    else:
        return "scissors";
    
def name_to_number(name):
    # fill in your code below
    if(name=="rock"):
        return 0;
    elif (name=="Spock"):
        return 1;
    elif (name=="paper"):
        return 2;
    elif (name=="lizard"):
        return 3;
    else:
        return 4;
    
def rpsls(name): 
    # convert name to player_number using name_to_number
    player_number=name_to_number(name);

    # compute random guess for comp_number using random.randrange()
    comp_number=random.randrange(0,5);
    # convert comp_number to name using number_to_name
    comp_name=number_to_name(comp_number);
    
    #print choices
    print "Player chooses ",name;
    print "Computer chooses ",comp_name;
    
    # compute difference of player_number and comp_number modulo five
    
    difference=player_number-comp_number;
        
    if(difference < 0):
        difference %= 5;
    
    # use if/elif/else to determine winner
    # print results
    if(difference == 1 or difference == 2):
        print "Player Wins!";
    elif(difference == 3 or difference == 4):
        print "Computer Wins!";
    else:
        print "Player and Computer Ties!";
    print ;
    
# test your code
rpsls("rock")
rpsls("Spock")
rpsls("paper")
rpsls("lizard")
rpsls("scissors")
