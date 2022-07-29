#The Cricket Game

import random
import math
import sys
from Teams_and_Players import Team_Pakistan, Team_India, Team_ROW, Team_Asia



#This class defines the player. 
class player:
    def __init__ (self, name = "Player_Name", Bat_Skill=0, Bowl_Skill=0, Field_Skill = 0, Fitness_Skill = 0, Fitness_Reduction = 0):
        self.name = name
        self.Bat_Skill = Bat_Skill
        self.Bowl_Skill = Bowl_Skill
        self.Field_Skill = Field_Skill
        self.Fitness_Skill = Fitness_Skill
        self.Fitness_Reduction = Fitness_Reduction

    #This function randomizes the batting points for that one particular delivery. Should be normalized with the bat skill being the mean
    def Batting(self):
        Batting_Points = (self.Bat_Skill + (self.Fitness_Skill/2))/1.5 + random.randint(-30,30)
        return Batting_Points

    #This function randomizes the bowling points for that one particular delivery. Should be normalized with the bat skill being the mean
    def Bowling(self):
        Bowling_Points = (self.Bowl_Skill + (self.Fitness_Skill/2))/1.5  + random.randint(-30,30)
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
def bowl_delivery(batsman, bowler, bowling_team, batting_team):
    global BatsmanScore
    global RunnerScore
    global score
    global wickets
    global fielder
    global Over_runs
    global Over_wickets
    global On_Strike
    global Not_on_Strike
    batsman_points = batsman.Batting()
    bowler_points = bowler.Bowling()
    point_differential = batsman_points - bowler_points
    print(batsman.name, file = f)
    if point_differential >= 80:
        score += 6
        BatsmanScore += 6
        Over_runs += 6
        print ("SIX! MASSIVE HIT. {} just picks it up and deposits over the boundary".format(batsman.name), file=f)
    elif point_differential >= 60:
        score += 4
        BatsmanScore += 4
        Over_runs += 4
        print("FOUR! Slashes between point and the slip fielders.", file=f)
    elif point_differential >= 50:
        if field_check(bowling_team, "easy", "n") == "passed":
            score +=3
            BatsmanScore +=3
            Over_runs += 3
            Temp_Variable_to_switch_Strike = Not_on_Strike
            Not_on_Strike = On_Strike
            On_Strike = Temp_Variable_to_switch_Strike
            Temp_Variable_to_Switch_Score = RunnerScore
            RunnerScore = BatsmanScore
            BatsmanScore = Temp_Variable_to_Switch_Score
            print("Batsman has scored 3 runs. {} puts in a dive to stop the boundary". format(fielder), file=f)
        else:
            score +=4
            BatsmanScore +=4
            Over_runs +=4
            print("FOUR! {} has bungled an easy stop. Gives away an extra run.".format(fielder), file=f)           
    elif point_differential >= 30:
        if field_check(bowling_team, "easy", "n") == "passed":
            score +=2
            BatsmanScore +=2
            Over_runs += 2
            print("Stopped at long off. Good running by {} to get to the ball. 2 runs added to the score".format(fielder), file=f)
        else:
            score +=4
            BatsmanScore +=4
            Over_runs += 4
            print("{} isn't paying attention here. Ball slips through his fingers, and gives away a four instead of 2 runs.".format(fielder), file=f)
    elif point_differential >= 0:
        if field_check(bowling_team, "easy", "n") == "passed":
            score +=1
            BatsmanScore +=1
            Over_runs += 1
            Temp_Variable_to_switch_Strike = Not_on_Strike
            Not_on_Strike = On_Strike
            On_Strike = Temp_Variable_to_switch_Strike
            Temp_Variable_to_Switch_Score = RunnerScore
            RunnerScore = BatsmanScore
            BatsmanScore = Temp_Variable_to_Switch_Score
            print("Driven straight to the man at deep midwicket. Good throw by {} to keep the batsman at 1 run".format(fielder), file=f)
        else:
            score +=4
            BatsmanScore +=4
            Over_runs += 4
            print("{} drives it straight to {} who lets the ball go between his legs. A single at best is now a four.".format(batsman.name, fielder), file=f)
    elif point_differential >= -30:
        print("Dot ball. No runs added.", file=f)
    elif point_differential <= -85: 
        print("Wicket! Taken! {} has bowled a wonderful delivery and has completely and utterly bamboozled {}".format(bowler.name, batsman.name), file=f)
        print("{}       b       {}     {}".format(batsman.name, bowler.name, BatsmanScore), file=f)
        wickets += 1
        On_Strike = player(batting_team[wickets+2][0], batting_team[wickets+2][1], batting_team[wickets+2][2], batting_team[wickets+2][3], batting_team[wickets+2][4], batting_team[wickets+2][7])
        Over_wickets +=1
        BatsmanScore = 0
    elif point_differential <= -65:
        wicket_chance = random.randint(-50,60)
        if wicket_chance >= 0:
            print("Loud appeal for an LBW, looks plumb... AND ITS GIVEN! {} heads back to the pavilion".format(batsman.name), file=f)
            print("{}       lbw       {}     {}".format(batsman.name, bowler.name, BatsmanScore), file=f)
            wickets += 1
            On_Strike = player(batting_team[wickets+2][0], batting_team[wickets+2][1], batting_team[wickets+2][2], batting_team[wickets+2][3], batting_team[wickets+2][4], batting_team[wickets+2][7])
            Over_wickets +=1
            BatsmanScore = 0

        else:
            print("The bowling side have all gone up to appeal this, but not given. Umpire indicating that the delivery was a bit high.", file=f) 
    elif point_differential <= -50:
        wicket_chance = random.randint(-50,50)
        if wicket_chance >= 0:
            if field_check(bowling_team, 'medium', "y") == "passed":
                print("Edged, and TAKEN! Excellent catch by the wicket keeper! {} shaking his head in disgust. What an unnecessary dismissal".format(batsman.name), file=f)
                print("{}   c   {}   b   {}     {}".format(batsman.name, fielder, bowler.name, BatsmanScore), file=f)
                wickets += 1
                Over_wickets +=1
                On_Strike = player(batting_team[wickets+2][0], batting_team[wickets+2][1], batting_team[wickets+2][2], batting_team[wickets+2][3], batting_team[wickets+2][4], batting_team[wickets+2][7])
                Over_wickets +=1
                BatsmanScore = 0
            else:
                print("DROPPED! Regulation catch dropped by the keeper. {} looks distraught. That really should be taken at this level of game play.".format(bowler.name), file=f)             
        else:
            print("EDGED! and bounced before the keeper. Lucky reprieve. ", file=f)
    elif point_differential <= -31:
        wicket_chance = random.randint(-50,50)
        if wicket_chance >= 0:
            if field_check(bowling_team, 'hard', "n") == "passed":
                print("WHAT A CATCH!! {} slashed the ball through point, and {} leapt to pouch and incredible catch. Fortunate breakthrough by {}".format( batsman.name, fielder, bowler.name), file=f)
                print("{}   c   {}   b   {}     {}".format(batsman.name, fielder, bowler.name, BatsmanScore), file=f)
                wickets += 1
                On_Strike = player(batting_team[wickets+2][0], batting_team[wickets+2][1], batting_team[wickets+2][2], batting_team[wickets+2][3], batting_team[wickets+2][4], batting_team[wickets+2][7])
                Over_wickets +=1
                BatsmanScore = 0

            else:
                print("OOF! A chance there slips through the fingers of {}. Was a difficult chance, but {} isn't happy about it.".format(fielder, bowler.name), file=f)             
        else:
            print("{} put alot of power in that shot, and the fielder did well to just stop it. Would've been a chance if the fielder was brought in a couple of paces.".format(batsman.name, bowler.name), file=f)     

def play_innings(batting_team, bowling_team):
    global over_number
    global wickets
    global score
    global BatsmanScore
    global RunnerScore
    global Over_runs
    global current_bowler
    global Over_wickets
    global On_Strike
    global Not_on_Strike

    On_Strike = player(batting_team[1][0], batting_team[1][1], batting_team[1][2], batting_team[1][3], batting_team[1][4], batting_team[1][7])
    Not_on_Strike = player(batting_team[2][0], batting_team[2][1], batting_team[2][2], batting_team[2][3], batting_team[2][4], batting_team[2][7])

    for y in range(20):
        bowl_over(batting_team, bowling_team)
        update_bowling_scorecard(current_bowler, Over_runs, Over_wickets, bowling_team)
        Over_runs = 0
        Over_wickets = 0
        over_number += 1
        if y == 19:
            innings_end(BowlingScoreCard_i1)
        if wickets == 10:
            innings_end(BowlingScoreCard_i1)
            return


def update_bowling_scorecard(bowler, over_runs, over_wickets, bowling_team):
    global max_overs
    for x in range(len(BowlingScoreCard_i1)):
        if BowlingScoreCard_i1[x][0] == bowler:
            BowlingScoreCard_i1[x][3] += over_runs
            BowlingScoreCard_i1[x][4] += over_wickets
            if over_runs == 0:
                BowlingScoreCard_i1[x][2] += 1
            if BowlingScoreCard_i1[x][1] == max_overs:
                for x in range(len(bowling_team)):
                    if bowling_team[x][0] == current_bowler:
                        bowling_team[x][2] = -50

def innings_end(bowlingScoreCard):
    print("\n\nBowling Scorecard", file=f)
    for x in range(len(bowlingScoreCard)):
        print(bowlingScoreCard[x], file=f)
    emptyScoreCard()

def emptyScoreCard():
    BowlingScoreCard_i1.clear()

        

def bowl_over(batting_team, bowling_team):
    global over_number
    global current_bowler
    global On_Strike
    global Not_on_Strike
    global BatsmanScore
    global RunnerScore
    bowler = pick_bowler(bowling_team)
    print("\n{} is the new bowler".format(current_bowler), file=f)
    for x in range(6):
        print("Over: {}.{}".format(over_number, x+1), file=f ) 
        batsman = On_Strike
        bowl_delivery(batsman, bowler, bowling_team, batting_team)
        if wickets == 10:
            return
    print("At the end of the over, the score is {} for {}".format(score, wickets), file=f)
    Temp_Variable_to_switch_Strike = Not_on_Strike
    Not_on_Strike = On_Strike
    On_Strike = Temp_Variable_to_switch_Strike
    Temp_Variable_to_Switch_Score = RunnerScore
    RunnerScore = BatsmanScore
    BatsmanScore = Temp_Variable_to_Switch_Score

    for x in range(1,12):
        if current_bowler == bowling_team[x][0]:
            bowling_team[x][7] += 5
        if bowling_team[x][7] != 0:
           bowling_team[x][7] - 1 


#Bowling skill is done twice. Once above - and once now. 
def pick_bowler(bowling_team):
    Bowl_Skill = 0
    bowler_found = False
    global current_bowler
    for x in range(1,12):
        if ((bowling_team[x][2] + ((bowling_team[x][4]-bowling_team[x][7])/2))/1.5) > Bowl_Skill:
            if current_bowler != bowling_team[x][0]:
                Bowl_Skill = ((bowling_team[x][2] + ((bowling_team[x][4]-bowling_team[x][7])/2))/1.5) 
                bowler = player(bowling_team[x][0], bowling_team[x][1], bowling_team[x][2], bowling_team[x][3], bowling_team[x][4], bowling_team[x][7])
                best_bowler = bowling_team[x][0]
    current_bowler = best_bowler
    #check over of current bowler
    for x in range(len(BowlingScoreCard_i1)):
        if BowlingScoreCard_i1[x][0] == current_bowler:
            BowlingScoreCard_i1[x][1] += 1
            bowler_found = True
    if bowler_found == False:
        BowlingScoreCard_i1.append([current_bowler, 1, 0, 0, 0])
    bowler_found = False
    return bowler

def play_game(team1, team2):
    global avg_fielding
    global over_number
    global wickets
    global score
    global BatsmanScore
    global RunnerScore
    for items in range(1, 12):
        avg_fielding = avg_fielding + team1[items][3] + team2[items][3]
    avg_fielding = avg_fielding/22
    over_number = 0
    wickets = 0
    score = 0
    BatsmanScore = 0
    RunnerScore = 0
    if random.randint(0,1) == 0:
        print("{} won the toss and has decided to bat first".format(team1[0][1]), file=f)
        play_innings(team1, team2)
        print("This closes the innings. {} have to make {} at a run rate of {} to win the game.".format( team2[0][0], score+1, (score+1)/20), file=f)
        over_number = 0
        wickets = 0
        score = 0
        BatsmanScore = 0
        play_innings(team2, team1)
    else:
        print("{} won the toss and has decided to bat first".format(team2[0][1]), file=f)
        play_innings(team2, team1)
        print("This closes the innings. {} have to make {} at a run rate of {} to win the game.".format( team1[0][0], score+1, (score+1)/20), file=f)
        over_number = 0
        wickets = 0
        score = 0
        BatsmanScore = 0
        play_innings(team1, team2)   


if __name__ == "__main__":
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
    #This list keeps track of bowling figures:
    #["Bowler Name", "Overs Bowled", Runs Given Away, Wickets Taken, Current Fitness ]
    BowlingScoreCard_i1 = []
    #This list keeps track of the scorecard:
    BattingScoreCard_i1 = []
    #This is Current Bowler name
    current_bowler = ""
    #Runs in the over
    Over_runs = 0
    #Wickets in the over
    Over_wickets = 0
    #Max overs per bowler
    max_overs = 4
    #Batsman on Strike
    On_Strike = []
    #Batsman not on strike
    Not_on_Strike = []
    #I might need to delete the variable batsman score

    f = open(r"C:\Users\Standard User\Google Drive\02 Personal Items\Python\Cricket-Game\Commentary", "a")


    play_game(Team_Pakistan, Team_ROW)

    f.close