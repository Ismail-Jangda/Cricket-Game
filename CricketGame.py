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

#This function should complete 1 delivery and make the necessary outcomes and update all statistics for that one ball.
def bowl_delivery(batsman, bowler):
    global BatsmanScore
    global score
    global wickets
    batsman_points = batsman.Batting()
    bowler_points = bowler.Bowling()
    point_differential = batsman_points - bowler_points
    if point_differential >= 80:
        score += 6
        BatsmanScore += 6
        print ("Batsman has scored 6 runs")
    elif point_differential >= 60:
        score += 4
        BatsmanScore += 4
        print("Batsman has scored 4 runs")
    elif point_differential >= 50:
        score +=3
        BatsmanScore +=3
        print("Batsman has scored 3 runs")
    elif point_differential >= 30:
        score +=2
        BatsmanScore +=2
        print("Batsman has scored 2 runs")
    elif point_differential >= 0:
        score +=1
        BatsmanScore +=1
        print("Batsman has scored 1 run")
    elif point_differential >= -30:
        print("Dot ball. No runs added.")
    elif point_differential <= -80: 
        print("Wicket! Taken! {} has bowled a wonderful delivery and has completely and utterly bamboozled {}".format(bowler.name, batsman.name))
        print("{} departs after scoring {} runs".format(batsman.name, BatsmanScore)) 
        wickets += 1
        BatsmanScore = 0
    elif point_differential <= -60:
        wicket_chance = random.randint(-40,60)
        if wicket_chance >= 0:
            print("Loud appeal for an LBW, looks plumb... AND ITS GIVEN! {} heads back to the pavilion".format(batsman.name))
            print("{} departs after scoring {} runs".format(batsman.name, BatsmanScore)) 
            wickets += 1
            BatsmanScore = 0
        else:
            print("The bowling side have all gone up to appeal this, but not given. Umpire indicating that the delivery was a bit high.") 
    elif point_differential <= -50:
        wicket_chance = random.randint(-50,50)
        if wicket_chance >= 0:
           print("Edged, and TAKEN! Excellent catch by the wicket keeper! {} shaking his head in disgust. What an unnecessary dismissal".format(batsman.name))
           print("{} departs after scoring {} runs".format(batsman.name, BatsmanScore)) 
           wickets += 1
           BatsmanScore = 0
        else:
            print("DROPPED! Regulation catch dropped by the keeper. {} looks distraught. That really should be taken at this level of game play.".format(bowler.name))             
    elif point_differential <= -31:
        wicket_chance = random.randint(-60,40)
        if wicket_chance >= 0:
            print("{} slashes at the ball, straight into the hands of the fielder. Lucky breakthrough by {}".format(batsman.name, bowler.name))
            print("{} departs after scoring {} runs".format(batsman.name, BatsmanScore)) 
            wickets += 1
            BatsmanScore = 0
        else:
            print("The fielder shelled the chance there. {} put alot of power in that shot, and the fielder was unable to grab onto it cleanly. Dot ball".format(batsman.name, bowler.name))     

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
        print("Over: {}.{}".format(over_number, x+1) )
        batsman = player(batting_team[wickets][0], batting_team[wickets][1],batting_team[wickets][2], batting_team[wickets][3], batting_team[wickets][4])
        bowler = player(bowling_team[9][0], bowling_team[9][1], bowling_team[9][2], bowling_team[9][3], bowling_team[9][4])
        bowl_delivery(batsman, bowler)
        if wickets == 10:
            print("This closes the innings. The batting team was able to score {}".format(score))
            return
    print("At the end of the over, the score is {} for {}".format(score, wickets))



def play_game(team1, team2):
    if random.randint(0,1) == 0:
        print("{} won the toss and has decided to bat first".format(team1))
        play_innings(team1, team2)
        play_innings(team2, team1)
    else:
        print("{} won the toss and has decided to bat first".format(team2))
        play_innings(team2, team1)
        play_innings(team1, team2)   

def main():
    play_game(Team_Pakistan, Team_India)
main()
