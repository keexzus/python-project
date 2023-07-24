import random

def roll(): 
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll 

while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <=4:
            break
        else:
             print("Must be between 2 and 4.")
    else: 
        print("Invalid input. Try again.")

max_score = 21
player_scores = [0 for _ in range(players)]

# print(player_scores)

while max(player_scores) < max_score:
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!")
        print("Your total score is: ", player_scores[player_idx],"\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                  break

            value = roll()
            if value == 1:
                print("You rolled a 1. Turn done.")
                current_score = 0
                break
            else:
                current_score += value

                if current_score > max_score:
                    print("You rolled a:", value)
                    print("You win! with a score of", current_score)
                    
                    break
                else:
                    print("You rolled a:", value)
                    print("Your score is:", current_score)
            
            # if player_scores[player_idx] >= max_score:
            #     print("You win!")
            #     break
    
        player_scores[player_idx] += current_score
        print("Congrats! Incredible performance! total score is: ", player_scores[player_idx])


max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner!\n"
      "with a score of:", max_score)