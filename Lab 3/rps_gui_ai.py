import pygame
import random
import sys
import os
import time 

pygame.init()

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rock, Paper, Scissors")

font = pygame.font.Font(None, 36)

rock = pygame.image.load(os.path.join(os.getcwd(), r"rock.jpeg"))
paper = pygame.image.load(os.path.join(os.getcwd(), r"paper.jpeg"))
scissors = pygame.image.load(os.path.join(os.getcwd(), r"scissors.jpeg"))
   
rock = pygame.transform.scale(rock, (120, 120))
paper = pygame.transform.scale(paper, (120, 120))
scissors = pygame.transform.scale(scissors, (120, 120))

def write_text(text, colour, x, y):
    text_surface = font.render(text, True, colour)
    screen.blit(text_surface, (x, y))

def draw_button(text, button_colour, text_colour, x, y, width, height):
    button = pygame.Rect(x, y, width, height)
    pygame.draw.rect(screen, button_colour, button)
    write_text(text, text_colour, x, y)

def get_user_choice():
    screen.fill(WHITE)
    write_text("Choose rock, paper, or scissors", RED, 220, 50)
    screen.blit(rock, (140, 240))
    screen.blit(paper, (340, 240))
    screen.blit(scissors, (540, 240))
    pygame.display.flip()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 140 <= x <= 260 and 240 <= y <= 360:
                    print("rock")
                    return "rock"
                elif 340 <= x <= 460 and 240 <= y <= 360:
                    print("paper")
                    return "paper"
                elif 540 <= x <= 660 and 240 <= y <= 360:
                    print("scissors")
                    return "scissors"
                
def get_opponent_choice():
    return random.choice(["rock", "paper", "scissors"])

def determine_winner(user_choice, opponent_choice):
    if user_choice == opponent_choice:
        return "It's a tie!"
    elif (
        (user_choice == "rock" and opponent_choice == "scissors") or
        (user_choice == "paper" and opponent_choice == "rock") or
        (user_choice == "scissors" and opponent_choice == "paper")
    ):
        return "You win!"
    else:
        return "You lose!"

def main():
    while True:
        user_choice = get_user_choice()
        opponent_choice = get_opponent_choice()
        print(opponent_choice)
        pygame.display.flip()

        screen.fill(WHITE)
        write_text(f"You chose {user_choice}.", BLACK, 100, 100)
        write_text(f"Opponent chose {opponent_choice}.", BLACK, 100, 200)
        result = determine_winner(user_choice, opponent_choice)
        write_text(result, BLACK, 100, 300)
        print(result)

        draw_button("Quit", BLACK, WHITE, 100, 400, 100, 50)
        draw_button("Play Again", BLACK, WHITE, 500, 400, 200, 50)
        pygame.display.flip()  

        while True:
            again = 0
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x, y = event.pos
                    if 100 <= x <= 200 and 400 <= y <= 450:
                        pygame.quit()
                        sys.exit()
                    elif 500 <= x <= 700 and 400 <= y <= 450:
                        again = 1
                        break
            if again == 1:
                break

if __name__ == "__main__":
    main()
