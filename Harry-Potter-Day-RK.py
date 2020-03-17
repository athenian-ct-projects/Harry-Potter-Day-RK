def fansCheer(team):
  print("Go " + team + "!")

fansCheer("Gryffindor")
fansCheer("Slytherin")
fansCheer("Hufflepuff")
fansCheer("Ravenclaw")

#Making quiditch!!!!!
#Dedicated for Nathan and his amazing teaching skills


# importing random numbers:
#import random
#print(random.randint(1,5))

#Deciding Teams:

#Team one picking

print("Here are the following rules to play quiditch!:")
team_name1 = input("To start, team one first pick your team, type in either Gryffindor, Slytherin, Hufflepuff, or Ravenclaw ") 
while team_name1 != "Gryffindor" and team_name1 != "Slytherin" and team_name1 !="Hufflepuff" and team_name1!= "Ravenclaw":
  team_name1 = input("You do not have a valid Harry Potter name for this quiditch cup try again!")
print("team one has decided to pick the glorious team "+team_name1)

#Team two picking

print("now that team one has picked thier team, now team 2 will pick") 
team_name2 =input("Pick any other wonderful team besides the one team one picked ") 
while team_name2!="Gryffindor" and team_name2 != "Slytherin" and team_name2 !="Hufflepuff" and team_name2!= "Ravenclaw" or team_name1 == team_name2:
  team_name2 =input("You do not have a valid Harry Potter name for this quiditch cup try agian!")

print("team two has decided to pick the glorious team " +team_name2) 

print("team one is " +team_name1 +" and team two is " +team_name2)

team_names = [team_name1, team_name2]

#coin toss time!

possesion=0

print("Follow the instructions and we will see who wins the game ") 
coin_toss=input((team_name1) + " it is time to start the game pick heads or tails ")
while coin_toss!= "heads" and coin_toss!= "tails":
  print("PICK HEADS OR TAILS!")
  coin_toss=input((team_name1) + " it is time to start the game pick heads or tails ")
if coin_toss=="heads":
  coin_toss=1 
elif coin_toss=="tails":
  coin_toss=2
import random
real_number=(random.randint(1,2))

#Saying who has won the toss 

if coin_toss==real_number:
  print((team_name1) +" has won the toss ")
  possesion=1
elif coin_toss!=real_number: 
  print((team_name2)+ " has won the toss ")
  possesion=2


#Staring the match

#Keeping track of score and possesion

score_team1=0
score_team2=0

possesion=0


def one_turn():
  global possesion
  global score_team1
  global score_team2

  print("Because team " + team_names[possesion] + " won the toss, they have started with the quaffle and bludgers. They will make the first move")
  choose_to_pass_or_shoot = input("You are at midfield, do you want to pass to a teamate ahead or do you want to shoot?")
  if choose_to_pass_or_shoot == "pass":
    
    #if choosing to pass 
    #clearing space
    #if pass is complete
    import random
    probability_of_completion=(random.randint(1,2))
    if probability_of_completion==2:
      print("pass complete")
      two_choice=input("now that the pass is complete, you are 25 yards away from the pole thing goal do you want to pass agian or shoot?")
      if two_choice=="pass":
        chance_two=(random.randint(1,3))
        if chance_two==3:
          print("pass is complete")
        elif chance_two!=3:
          print("pass is incomplete")
          
      elif two_choice=="shoot":
        two_score=(random.randint(1,3))
        if two_score==2:
          print("GOALLLL!!!!")
          if possesion==0: 
            score_team1+=50
            print(str(score_team1)+" is how many points you have")
          else:
            score_team2+=50
            print(str(score_team2) + " is how many points you have")
        elif two_score!=2:
          print("missed goal")
    else: 
      print("pass is incomplete")
  

  

  elif choose_to_pass_or_shoot=="shoot":

    import random
    probability_of_score=(random.randint(1,3))
    if probability_of_score==3:
      print("YOU SCORDED!!!")
      print("GOALLLL!!!!")
      if possesion==0: 
          score_team1+=50
          print(str(score_team1)+ " is how many points you have")
      else:
          score_team2+=50
          print(str(score_team2)+" is how many points you have")
    else:
       print("It is a missed")


  if possesion==0:
    possesion=1
  else:
    possesion=0


# elif coin_toss!=real_number:
#   print("Because team two has won the toss, they have started with the quaffle and bludgers. They will make the first move")
#   #input("You are at midfield, do you want to pass to a teamate ahead or do you want to shoot?")
#   choose_to_pass_or_shoot =input("You are at midfield, do you want to pass to a teamate ahead or do you want to shoot?")
#   if choose_to_pass_or_shoot=="pass":
  
#     import random
#     probability_of_completion = (random.randint(1,2))
#     if probability_of_completion==2:
#       print("pass complete")
#     elif choose_to_pass_or_shoot!=probability_of_completion:
#       print("pass is incomplete")

# #Picking if they decide to shoot not pass
# #*clearing space*
# #*clearing space*

#   elif choose_to_pass_or_shoot=="shoot":

#     import random
#     probability_of_score=(random.randint(1,5))
#     if probability_of_score==3:
#       print("YOU SCORDED!!!")
#     elif choose_to_pass_or_shoot!=probability_of_completion:
#       print("It is a missed")

for x in range (10):
  one_turn()
