# imports
import pygame
import random
import math as m
import sys


# constants
width = 800
height = 600
init_lives = 3
lives_increment = 40
nr_levels_max = 3
bannerX = (width) // 2
bannerY = (height) // 2
fire_rate = 4
poop_frequency = 30
kam_freqency = 30
white = (255, 255, 255)

#fonts
font = "fonts/Banana.ttf"

# in game messages
game_name = "Flying PIGS"
gameover_messages = ["mwahahahaha..you're vegan now", "oh no?! our barbecue...its broken", "oink oink oink oink oink oink oink"]
win_messages = ["yeeeeey!!!", "burgiiir", "bon appetite"]

# photos
background_img = "images/background.png"
pig_img = "images/pig.png"
barbeque_img = "images/barbeque.png"
bullet1_img = "images/coal.png"
bullet2_img = "images/fork.png"
bullet3_img = "images/burning.png"
reward1_img = "images/ham.png"
reward2_img = "images/sausage.png"
reward3_img = "images/ribs.png"
gameover_img = "images/gameover.png"
ribbon_img = "images/ribbon.png"
poop_img = "images/poop.png"

