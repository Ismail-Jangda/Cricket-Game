#This is The Cricket Game

import random
import math
score = 0
wickets = 0 
class player:
    def __init__ (self, name = "Player_Name", Bat_Skill=0, Bowl_Skill=0, Field_Skill = 0):
        self.name = name
        self.Bat_Skill = Bat_Skill
        self.Bowl_Skill = Bowl_Skill
        self.Field_Skill = Field_Skill

    def Batting(self):
        Batting_Points = self.Bat_Skill + random.randint(-50,50)
        return Batting_Points

    def Bowling(self):
        Bowling_Points = self.Bowl_Skill + random.randint(-50,50)
        return Bowling_Points

def bowl_delivery(batsman, bowler):
    global score
    global wickets
    batsman_points = batsman.Batting()
    bowler_points = bowler.Bowling()
    point_differential = batsman_points - bowler_points
    if point_differential >= 80:
        score += 6
        print ("Batsman has scored 6 runs")
    elif point_differential >= 60:
        score += 4
        print("Batsman has scored 4 runs")
    elif point_differential >= 50:
        score +=3
        print("Batsman has scored 3 runs")
    elif point_differential >= 30:
        score +=2
        print("Batsman has scored 2 runs")
    elif point_differential >= 0:
        score +=1
        print("Batsman has scored 1 run")
    elif point_differential >= -30:
        print("Dot ball. No runs added.")
    elif point_differential <= -80: 
        print("Wicket! Taken! {} has bowled a wonderful delivery and has completely and utterly bamboozled {}".format(bowler.name, batsman.name)) 
        wickets += 1
    elif point_differential <= -60:
        wicket_chance = random.randint(-40,60)
        if wicket_chance >= 0:
            print("Loud appeal for an LBW, looks plumb... AND ITS GIVEN! {} heads back to the pavilion".format(batsman.name))
            wickets += 1
        else:
            print("The bowling side have all gone up to appeal this, but not given. Umpire indicating that the delivery was a bit high.") 
    elif point_differential <= -50:
        wicket_chance = random.randint(-50,50)
        if wicket_chance >= 0:
           print("Edged, and TAKEN! Excellent catch by the wicket keeper! {} shaking his head in disgust. What an unnecessary dismissal".format(batsman.name))
           wickets += 1
        else:
            print("DROPPED! Regulation catch dropped by the keeper. {} looks distraught. That really should be taken at this level of game play.".format(bowler.name))             
    elif point_differential <= -31:
        wicket_chance = random.randint(-60,40)
        if wicket_chance >= 0:
            print("{} slashes at the ball, straight into the hands of the fielder. Lucky breakthrough by {}".format(batsman.name, bowler.name))
            wickets += 1
        else:
            print("The fielder shelled the chance there. {} put alot of power in that shot, and the fielder was unable to grab onto it cleanly. Dot ball".format(batsman.name, bowler.name))     

def bowl_over(batsman, bowler):
    for x in range(6):
        if wickets == 10:
            print("This closes the innings. The batting team was able to score {}".format(score))
            return
        print("Over: 0.{}".format(x+1) )
        bowl_delivery(batsman, bowler)
    print("At the end of the over, the score is {} for {}".format(score, wickets))


def main():
    Wasim = player("Wasim Akram", 70, 95, 75)
    Sachin = player("Sachin Tendulkar", 95, 63, 70)
    bowl_over(Sachin, Wasim)

main()