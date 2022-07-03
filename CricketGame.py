#The Cricket Game

import random
import math
from Teams_and_Players import Team_Pakistan, Team_India

#This variable keeps the overall score
score = 0
#This variable keeps the wickets that have fallen
wickets = 0 
#This variable keeps the current batsman score
BatsmanScore = 0
#This variable keeps the current over number
over_number = 0
#This variable is the average fielding level of the players in game. Used for fielding checks
avg_fielding = 0
#This variable defines the fielder selected
fielder = ""

#This class defines the player. I need to add fitness to this. 
class player:
    def __init__ (self, name = "Player_Name", Bat_Skill=0, Bowl_Skill=0, Field_Skill = 0, Fitness_Skill = 0):
        self.name = name
        self.Bat_Skill = Bat_Skill
        self.Bowl_Skill = Bowl_Skill
        self.Field_Skill = Field_Skill
        self.Fitness_Skill = Fitness_Skill

    #This function randomizes the batting points for that one particular delivery. Should be normalized with the bat skill being the mean
    def Batting(self):
        Batting_Points = self.Bat_Skill + random.randint(-50,50)
        return Batting_Points

    #This function randomizes the bowling points for that one particular delivery. Should be normalized with the bat skill being the mean
    def Bowling(self):
        Bowling_Points = self.Bowl_Skill + random.randint(-50,50)
        return Bowling_Points

def field_check(bowling_team, difficulty, keeper):
    global fielder

    if keeper == "y":
        fielder = bowling_team[(bowling_team[0][2])][0]
        fielding_points = bowling_team[(bowling_team[0][2])][3] + random.randint(-30,30)
    else:
        fielder_select = random.randint(1,11)
        while fielder_select == bowling_team[0][2]:
            fielder_select = random.randint(1,11)
        fielder = bowling_team[fielder_select][0] 
        fielding_points = bowling_team[fielder_select][3] + random.randint(-30,30)
    if difficulty == "easy":
        pass_points = avg_fielding + random.randint(-30,0)
    if difficulty == "medium":
        pass_points = avg_fielding + random.randint(-30,30)
    if difficulty == "hard":
        pass_points = avg_fielding + random.randint(-30,50)
    
    if fielding_points > pass_points:
        return "passed"
    else:
        return "failed"
    






#This function should complete 1 delivery and make the necessary outcomes and update all statistics for that one ball.
def bowl_delivery(batsman, bowler, bowling_team):
    global BatsmanScore
    global score
    global wickets
    global fielder
    batsman_points = batsman.Batting()
    bowler_points = bowler.Bowling()
    point_differential = batsman_points - bowler_points
    if point_differential >= 80:
        score += 6
        BatsmanScore += 6
        print ("SIX! MASSIVE HIT. {} just picks it up and deposits over the boundary".format(batsman.name))
    elif point_differential >= 60:
        score += 4
        BatsmanScore += 4
        print("FOUR! Slashes between point and the slip fielders.")
    elif point_differential >= 50:
        if field_check(bowling_team, "easy", "n") == "passed":
            score +=3
            BatsmanScore +=3
            print("Batsman has scored 3 runs. {} puts in a dive to stop the boundary". format(fielder))
        else:
            score +=4
            BatsmanScore +=4
            print("FOUR! {} has bungled an easy stop. Gives away an extra run.".format(fielder))           
    elif point_differential >= 30:
        if field_check(bowling_team, "easy", "n") == "passed":
            score +=2
            BatsmanScore +=2
            print("Stopped at long off. Good running by {} to get to the ball. 2 runs added to the score".format(fielder))
        else:
            score +=4
            BatsmanScore +=4
            print("{} isn't paying attention here. Ball slips through his fingers, and gives away a four instead of 2 runs.".format(fielder))
    elif point_differential >= 0:
        if field_check(bowling_team, "easy", "n") == "passed":
            score +=1
            BatsmanScore +=1
            print("Driven straight to the man at deep midwicket. Good throw by {} to keep the batsman at 1 run".format(fielder))
        else:
            score +=4
            BatsmanScore +=4
            print("{} drives it straight to {} who lets the ball go between his legs. A single at best is now a four.".format(batsman.name, fielder))
    elif point_differential >= -30:
        print("Dot ball. No runs added.")
    elif point_differential <= -85: 
        print("Wicket! Taken! {} has bowled a wonderful delivery and has completely and utterly bamboozled {}".format(bowler.name, batsman.name))
        print("{}       b       {}     {}".format(batsman.name, bowler.name, BatsmanScore))
        wickets += 1
        BatsmanScore = 0
    elif point_differential <= -65:
        wicket_chance = random.randint(-50,60)
        if wicket_chance >= 0:
            print("Loud appeal for an LBW, looks plumb... AND ITS GIVEN! {} heads back to the pavilion".format(batsman.name))
            print("{}       lbw       {}     {}".format(batsman.name, bowler.name, BatsmanScore))
            wickets += 1
            BatsmanScore = 0
        else:
            print("The bowling side have all gone up to appeal this, but not given. Umpire indicating that the delivery was a bit high.") 
    elif point_differential <= -50:
        wicket_chance = random.randint(-50,50)
        if wicket_chance >= 0:
            if field_check(bowling_team, 'medium', "y") == "passed":
                print("Edged, and TAKEN! Excellent catch by the wicket keeper! {} shaking his head in disgust. What an unnecessary dismissal".format(batsman.name))
                print("{}   c   {}   b   {}     {}".format(batsman.name, fielder, bowler.name, BatsmanScore))
                wickets += 1
                BatsmanScore = 0
            else:
                print("DROPPED! Regulation catch dropped by the keeper. {} looks distraught. That really should be taken at this level of game play.".format(bowler.name))             
        else:
            print("EDGED! and bounced before the keeper. Lucky reprieve. ")
    elif point_differential <= -31:
        wicket_chance = random.randint(-50,50)
        if wicket_chance >= 0:
            if field_check(bowling_team, 'hard', "n") == "passed":
                print("WHAT A CATCH!! {} slashed the ball through point, and {} leapt to pouch and incredible catch. Fortunate breakthrough by {}".format( batsman.name, fielder, bowler.name))
                print("{}   c   {}   b   {}     {}".format(batsman.name, fielder, bowler.name, BatsmanScore))
                wickets += 1
                BatsmanScore = 0
            else:
                print("OOF! A chance there slips through the fingers of {}. Was a difficult chance, but {} isn't happy about it.".format(fielder, bowler.name))             
        else:
            print("{} put alot of power in that shot, and the fielder did well to just stop it. Would've been a chance if the fielder was brought in a couple of paces.".format(batsman.name, bowler.name))     

def play_innings(batting_team, bowling_team):
    global over_number
    global wickets
    global score
    for y in range(20):
        bowl_over(batting_team, bowling_team)
        over_number += 1
        if wickets == 10:
            over_number = 0
            wickets = 0
            score = 0
            return

def bowl_over(batting_team, bowling_team):
    global over_number
    for x in range(6):
        print("\n Over: {}.{}".format(over_number, x+1) )
        batsman = player(batting_team[wickets+1][0], batting_team[wickets+1][1],batting_team[wickets+1][2], batting_team[wickets+1][3], batting_team[wickets+1][4])
        bowler = player(bowling_team[9][0], bowling_team[9][1], bowling_team[9][2], bowling_team[9][3], bowling_team[9][4])
        bowl_delivery(batsman, bowler, bowling_team)
        if wickets == 10:
            print("This closes the innings. The batting team was able to score {}".format(score))
            return
    print("At the end of the over, the score is {} for {}".format(score, wickets))



def play_game(team1, team2):
    global avg_fielding
    for items in range(1, 12):
        avg_fielding = avg_fielding + team1[items][3] + team2[items][3]
    avg_fielding = avg_fielding/22
    if random.randint(0,1) == 0:
        print("{} won the toss and has decided to bat first".format(team1[0][1]))
        play_innings(team1, team2)
        play_innings(team2, team1)
    else:
        print("{} won the toss and has decided to bat first".format(team2[0][1]))
        play_innings(team2, team1)
        play_innings(team1, team2)   

def main():
    play_game(Team_Pakistan, Team_India)
main()
