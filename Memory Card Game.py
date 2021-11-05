# Library
from tkinter import *

import os, os.path, sys, random, time

from os import path
from PIL import Image, ImageTk

# Turn off console

# hide = win32gui.GetForegroundWindow()
# win32gui.ShowWindow(hide, win32con.SW_HIDE)

# Screen
screen = Tk() 

screen.config(bg = "light blue")
screen.title("Memory Card Game")
screen.geometry("{0}x{1}+0+0".format(screen.winfo_screenwidth(), screen.winfo_screenheight()))

# Making paths & settings
pathname = os.path.dirname(sys.argv[0])

if path.exists(pathname) == False:
    os.mkdir(pathname)

if path.exists(pathname+"\settings.txt") == False:
    settings = open(pathname+"\settings.txt", "w")
    settings.write("difficulty = 2\ndisplaytime = 2")
    settings.close()

if path.exists(pathname+"\savegame.txt") == False:
    savegame = open(pathname+"\savegame.txt", "w")
    savegame.write("lvl01 = 1\nlvl02 = 0\nlvl03 = 0\nlvl04 = 0\nlvl05 = 0\nlvl06 = 0\nlvl07 = 0\nlvl08 = 0")
    savegame.close()

# Change game icon
icon = PhotoImage(file=pathname+r"\img\content\inverted_tiles.png")
screen.call("wm", "iconphoto", screen._w, icon)
#screen.iconbitmap(pathname+r"\img\content\inverted_tiles.png")

# Global variabels
correct = 0
attempts = 0
count = 0
answer_list = []
answer_dict = {}
difficultyload = []
displaytimeload = []

# 2v2 global variabels
turn = ""

count1 = 0
count2 = 0

correct1 = 0
correct2 = 0

# Level countdown
sec = 0

timer01 = [0,0]
timer02 = [0,0]
timer03 = [0,0]
timer04 = [0,0]
timer05 = [0,0]
timer06 = [0,0]
timer07 = [0,0]
timer08 = [0,0]

# Main
def main():

    # Path saver
    settingsload = open(pathname+"\settings.txt", "r")
    settings = settingsload.read()
    i = 0
    pathload = ""
    for x in settings:
        i = 1 + i
        if i > 23:
            pathload = pathload + str(x)
    settingsload.close()

    # After clicking Start
    def start():

        # Setting all global variabels to default
        global correct, attempts, count, count1, count2, turn, correct1, correct2, answer_list, answer_dict, sec, timer01, timer02, timer03, timer04, timer05, timer06, timer07, timer08

        correct = 0
        attempts = 0
        count = 0
        answer_list = []
        answer_dict = {}

        count1 = 0
        count2 = 0
        correct1 = 0
        correct2 = 0

        # Level countdown
        sec = 0

        timer01 = [0,10]
        timer02 = [0,20]
        timer03 = [0,20]
        timer04 = [0,25]
        timer05 = [1,0]
        timer06 = [2,0]
        timer07 = [2,20]
        timer08 = [5,0]

        settingsload = open(pathname+"\settings.txt", "r")
        settings = settingsload.read()
        i = 0
        for x in settings:
            i = 1 + i
            if i > 13:
                difficultyload.append(x)
        settingsload.close()

        diffcons = [1]

        if difficultyload[0] == "1":
            diffcons[0] = 2
        elif difficultyload[0] == "2":
            diffcons[0] = 1.5
        elif difficultyload[0] == "3":
            diffcons[0] = 1

        def diff(timer, diffcons):
            if timer[0] == 0:
                if (timer[1] * int(diffcons[0])) < 60:
                    timer[1] = int(timer[1] * float(diffcons[0])) + 1
                else:
                    timer[0] += 1
                    timer[1] = int(timer[1] * float(diffcons[0]) - 60) + 1
            else:
                timer[0] = int(timer[0] * float(diffcons[0]))

        diff(timer01, diffcons)
        diff(timer02, diffcons)
        diff(timer03, diffcons)
        diff(timer04, diffcons)
        diff(timer05, diffcons)
        diff(timer06, diffcons)
        diff(timer07, diffcons)
        diff(timer08, diffcons)

        # Levels
        
        #
        #
        #
        #
        # Level 01
        def lvl01():
            top1.destroy()
            top2.destroy()
            twovtwo_btn.destroy()
            back_btn.destroy()

            global displaytimeload

            # Images
            inverted_tiles_img = Image.open(pathname+r"\img\content\inverted_tiles.png")
            inverted_tiles_img = inverted_tiles_img.resize((128, 128), Image.ANTIALIAS)
            inverted_tiles_img = ImageTk.PhotoImage(inverted_tiles_img)
            inverted_tiles = Label(image=inverted_tiles_img)
            inverted_tiles.image = inverted_tiles_img

            c01_img = Image.open(pathname+r"\img\content\01.png")
            c01_img = c01_img.resize((128, 128), Image.ANTIALIAS)
            c01_img = ImageTk.PhotoImage(c01_img)
            c01 = Label(image=c01_img)
            c01.image = c01_img

            c02_img = Image.open(pathname+r"\img\content\02.png")
            c02_img = c02_img.resize((128, 128), Image.ANTIALIAS)
            c02_img = ImageTk.PhotoImage(c02_img)
            c02 = Label(image=c02_img)
            c02.image = c02_img

            c03_img = Image.open(pathname+r"\img\content\03.png")
            c03_img = c03_img.resize((128, 128), Image.ANTIALIAS)
            c03_img = ImageTk.PhotoImage(c03_img)
            c03 = Label(image=c03_img)
            c03.image = c03_img

            # Random cards
            random_cards = [1,1,2,2,3,3]
            random.shuffle(random_cards)

            # Frames
            level_top = Frame(screen)
            level_top.pack(pady = 20, side=TOP)

            lvl01_top = Frame(screen)
            lvl01_top.pack(pady = 20, side=TOP)

            lvl01 = Frame(screen)
            lvl01.pack(pady = 20, side = TOP)

            lvl01_bottom = Frame(screen)
            lvl01_bottom.pack(pady = 100, side=BOTTOM)

            # Show cards
            def show_cards(c, card, number):
                if c["text"] == "":
                    def waithere():
                        var = IntVar()
                        screen.after(100, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    # Show images
                    if card == 1:
                        c["image"] = c01_img
                    elif card == 2:
                        c["image"] = c02_img
                    elif card == 3:
                        c["image"] = c03_img
                

            #Functions for clicking buttons
            def button_click(c, card, number):
                global count, answer_list, answer_dict, attempts, correct
                if c["text"] == "" and count < 2:
                    if card == 1:
                        # Change image
                        c["text"] = "1"
                        c["image"] = c01_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "1"
                    elif card == 2:
                        # Change image
                        c["text"] = "2"
                        c["image"] = c02_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "2"
                    elif card == 3:
                        # Change image
                        c["text"] = "3"
                        c["image"] = c03_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "3"

                    # Counter for steps
                    count += 1
                
                # Start to determine correct answers
                if len(answer_list) == 2:
                    if random_cards[answer_list[0]] == random_cards[answer_list[1]]:
                        # Attempt counter
                        attempts += 1
                        attempts_label.config(text="Attempts: " + str(attempts) + "     |")
                        # Status label
                        status_label.config(text="  Match!")
                        # Disabling button if correct answer
                        for key in answer_dict:
                            key["state"] = "disabled"
                        # Reseting temp
                        count = 0
                        answer_list = []
                        answer_dict = {}
                        # Counting correct answers
                        correct += 1
                    else:
                        # Attempt counter
                        attempts += 1
                        attempts_label.config(text="Attempts: " + str(attempts) + "     |")
                        # Status label
                        status_label.config(text="  Incorrect!")
                        # Reseting temp
                        count = 0
                        answer_list = []

                        # Waittime after incorrect answer
                        def waithere():
                            var = IntVar()
                            screen.after(10, var.set, 1)
                            screen.wait_variable(var)
                        waithere()
                        time.sleep(1)

                        # Reset the buttons
                        for key in answer_dict:
                            key["text"] = ""
                            key["image"] = inverted_tiles_img

                        # Reseting temp
                        answer_dict = {}
                
                # Game win
                if correct == 3:
                    # Status win
                    status_label.config(text="Win!", font=("Helvetica", 48))

                    # Pause after winning the game
                    def waithere():
                        var = IntVar()
                        screen.after(500, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    time.sleep(2.5)

                    # Auto save game
                    with open(pathname+"\savegame.txt", "r") as file:
                        savegame = file.read()
                        savegame = savegame.replace("lvl02 = 0", "lvl02 = 1")

                    with open(pathname+"\savegame.txt", "w") as file:
                        file.write(savegame)

                    # Returing back to level menu
                    level_top.destroy()
                    lvl01_top.destroy()
                    lvl01.destroy()
                    lvl01_bottom.destroy()
                    
                    start()

            # Level logo
            level_label = Label(level_top, image = level01_img, width= 130, height=130)
            level_label.pack(pady = 10)

            # Playcards
            card0 = Button(lvl01_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card0, random_cards[0], 0))
            card1 = Button(lvl01_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card1, random_cards[1], 1))
            card2 = Button(lvl01_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card2, random_cards[2], 2))
            card3 = Button(lvl01_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card3, random_cards[3], 3))
            card4 = Button(lvl01_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card4, random_cards[4], 4))
            card5 = Button(lvl01_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card5, random_cards[5], 5))

            # Griding playcards
            card0.grid(row = 0, column = 0)
            card1.grid(row = 0, column = 1)
            card2.grid(row = 0, column = 2)
            card3.grid(row = 1, column = 0)
            card4.grid(row = 1, column = 1)
            card5.grid(row = 1, column = 2)

            cards = [card0, card1, card2, card3, card4, card5]

            # Show cards
            i = 0
            for item in cards:
                show_cards(item, random_cards[i], i)
                i += 1
            
            # Wait for few seconds
            def waithere():
                var = IntVar()
                screen.after(500, var.set, 1)
                screen.wait_variable(var)
            waithere()

            settingsload = open(pathname+"\settings.txt", "r")
            settings = settingsload.read()
            i = 0
            for x in settings:
                i = 1 + i
                if i > 29:
                    displaytimeload.append(x)
            settingsload.close()

            if displaytimeload[0] == "1":
                time.sleep(2.5)
            elif displaytimeload[0] == "2":
                time.sleep(1)
            elif displaytimeload[0] == "2":
                time.sleep(0.5)
            
            # Hide cards
            card0.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card1.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card2.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card3.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card4.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card5.config(image = inverted_tiles_img)

            # Status & attempts label
            status_label = Label(lvl01, text="Game Started!")
            attempts_label = Label(lvl01, text="Attempts: " + str(attempts) + "     |")

            attempts_label.grid(row = 0, column = 0)
            status_label.grid(row = 0, column = 1)

            # Countdown timer
            def clock():
                global timer01, sec
                timer01[1] -= 1

                # Losing game after countdown is finished
                if timer01[1] == -1 and timer01[0] != 0:
                    timer01[0] -= 1
                    timer01[1] += 60

                timer_label.config(text = str(timer01[0]) + ":" + str(timer01[1]))

                if timer01[0] == 0 and timer01[1] == 0:
                    # Status label
                    status_label.config(text="Lose! Try Again!", font=("Helvetica", 48))

                    # Pause after losing game
                    def waithere():
                        var = IntVar()
                        screen.after(500, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    time.sleep(2.5)

                    # Returning back to level menu
                    level_top.destroy()
                    lvl01_top.destroy()
                    lvl01.destroy()
                    lvl01_bottom.destroy()

                    start() 

                timer_label.after(1000, clock)


            timer_label = Label(lvl01_bottom, text = str(timer01[0]) + ":" + str(timer01[1]), font=("Helvetica", 32))
            timer_label.pack(pady=20)

            clock()

        # Lvl 01 end

        #
        #
        #
        #
        # Level 02
        def lvl02():
            top1.destroy()
            top2.destroy()
            twovtwo_btn.destroy()
            back_btn.destroy()

            global displaytimeload

            # Images
            inverted_tiles_img = Image.open(pathname+r"\img\content\inverted_tiles.png")
            inverted_tiles_img = inverted_tiles_img.resize((128, 128), Image.ANTIALIAS)
            inverted_tiles_img = ImageTk.PhotoImage(inverted_tiles_img)
            inverted_tiles = Label(image=inverted_tiles_img)
            inverted_tiles.image = inverted_tiles_img

            c01_img = Image.open(pathname+r"\img\content\04.png")
            c01_img = c01_img.resize((128, 128), Image.ANTIALIAS)
            c01_img = ImageTk.PhotoImage(c01_img)
            c01 = Label(image=c01_img)
            c01.image = c01_img

            c02_img = Image.open(pathname+r"\img\content\05.png")
            c02_img = c02_img.resize((128, 128), Image.ANTIALIAS)
            c02_img = ImageTk.PhotoImage(c02_img)
            c02 = Label(image=c02_img)
            c02.image = c02_img

            c03_img = Image.open(pathname+r"\img\content\06.png")
            c03_img = c03_img.resize((128, 128), Image.ANTIALIAS)
            c03_img = ImageTk.PhotoImage(c03_img)
            c03 = Label(image=c03_img)
            c03.image = c03_img

            c04_img = Image.open(pathname+r"\img\content\07.png")
            c04_img = c04_img.resize((128, 128), Image.ANTIALIAS)
            c04_img = ImageTk.PhotoImage(c04_img)
            c04 = Label(image=c04_img)
            c04.image = c04_img

            c05_img = Image.open(pathname+r"\img\content\08.png")
            c05_img = c05_img.resize((128, 128), Image.ANTIALIAS)
            c05_img = ImageTk.PhotoImage(c05_img)
            c05 = Label(image=c05_img)
            c05.image = c05_img

            # Random cards
            num = 3
            random_cards = [1,1,2,2,3,3,4,4,5,5]
            random.shuffle(random_cards)

            # Frames
            level_top = Frame(screen)
            level_top.pack(pady = 20, side=TOP)

            lvl02_top = Frame(screen)
            lvl02_top.pack(pady = 20, side=TOP)

            lvl02 = Frame(screen)
            lvl02.pack(pady = 20, side = TOP)

            lvl02_bottom = Frame(screen)
            lvl02_bottom.pack(pady = 100, side=BOTTOM)

            # Show cards
            def show_cards(c, card, number):
                if c["text"] == "":
                    def waithere():
                        var = IntVar()
                        screen.after(100, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    # Show images
                    if card == 1:
                        c["image"] = c01_img
                    elif card == 2:
                        c["image"] = c02_img
                    elif card == 3:
                        c["image"] = c03_img
                    elif card == 4:
                        c["image"] = c04_img
                    elif card == 5:
                        c["image"] = c05_img
                

            #Functions for clicking buttons
            def button_click(c, card, number):
                global count, answer_list, answer_dict, attempts, correct
                if c["text"] == "" and count < 2:
                    if card == 1:
                        # Change image
                        c["text"] = "1"
                        c["image"] = c01_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "1"
                    elif card == 2:
                        # Change image
                        c["text"] = "2"
                        c["image"] = c02_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "2"
                    elif card == 3:
                        # Change image
                        c["text"] = "3"
                        c["image"] = c03_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "3"
                    elif card == 4:
                        # Change image
                        c["text"] = "4"
                        c["image"] = c04_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "4"
                    elif card == 5:
                        # Change image
                        c["text"] = "5"
                        c["image"] = c05_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "5"

                    # Counter for steps
                    count += 1
                
                # Start to determine correct answers
                if len(answer_list) == 2:
                    if random_cards[answer_list[0]] == random_cards[answer_list[1]]:
                        # Attempt counter
                        attempts += 1
                        attempts_label.config(text="Attempts: " + str(attempts) + "     |")
                        # Status label
                        status_label.config(text="  Match!")
                        # Disabling button if correct answer
                        for key in answer_dict:
                            key["state"] = "disabled"
                        # Reseting temp
                        count = 0
                        answer_list = []
                        answer_dict = {}
                        # Counting correct answers
                        correct += 1
                    else:
                        # Attempt counter
                        attempts += 1
                        attempts_label.config(text="Attempts: " + str(attempts) + "     |")
                        # Status label
                        status_label.config(text="  Incorrect!")
                        # Reseting temp
                        count = 0
                        answer_list = []

                        # Waittime after incorrect answer
                        def waithere():
                            var = IntVar()
                            screen.after(10, var.set, 1)
                            screen.wait_variable(var)
                        waithere()
                        time.sleep(1)

                        # Reset the buttons
                        for key in answer_dict:
                            key["text"] = ""
                            key["image"] = inverted_tiles_img

                        # Reseting temp
                        answer_dict = {}
                if correct == 5:
                    # Status win
                    status_label.config(text="Win!", font=("Helvetica", 48))

                    # Pause after winning the game
                    def waithere():
                        var = IntVar()
                        screen.after(500, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    time.sleep(2.5)

                    # Auto save game
                    with open(pathname+"\savegame.txt", "r") as file:
                        savegame = file.read()
                        savegame = savegame.replace("lvl03 = 0", "lvl03 = 1")

                    with open(pathname+"\savegame.txt", "w") as file:
                        file.write(savegame)

                    # Returing back to level menu
                    level_top.destroy()
                    lvl02_top.destroy()
                    lvl02.destroy()
                    lvl02_bottom.destroy()
                    
                    start()

            # Level logo
            level_label = Label(level_top, image = level02_img, width= 130, height=130)
            level_label.pack(pady = 10)

            # Playcards
            card0 = Button(lvl02_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card0, random_cards[0], 0))
            card1 = Button(lvl02_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card1, random_cards[1], 1))
            card2 = Button(lvl02_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card2, random_cards[2], 2))
            card3 = Button(lvl02_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card3, random_cards[3], 3))
            card4 = Button(lvl02_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card4, random_cards[4], 4))
            card5 = Button(lvl02_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card5, random_cards[5], 5))
            card6 = Button(lvl02_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card6, random_cards[6], 6))
            card7 = Button(lvl02_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card7, random_cards[7], 7))
            card8 = Button(lvl02_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card8, random_cards[8], 8))
            card9 = Button(lvl02_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card9, random_cards[9], 9))

            # Griding playcards
            card0.grid(row = 0, column = 0)
            card1.grid(row = 0, column = 1)
            card2.grid(row = 0, column = 2)
            card3.grid(row = 0, column = 3)
            card4.grid(row = 0, column = 4)
            card5.grid(row = 1, column = 0)
            card6.grid(row = 1, column = 1)
            card7.grid(row = 1, column = 2)
            card8.grid(row = 1, column = 3)
            card9.grid(row = 1, column = 4)

            cards = [card0, card1, card2, card3, card4, card5, card6, card7, card8, card9]

            # Show cards
            i = 0
            for item in cards:
                show_cards(item, random_cards[i], i)
                i += 1
                
            # Wait for few seconds
            def waithere():
                var = IntVar()
                screen.after(500, var.set, 1)
                screen.wait_variable(var)
            waithere()

            settingsload = open(pathname+"\settings.txt", "r")
            settings = settingsload.read()
            i = 0
            for x in settings:
                i = 1 + i
                if i > 29:
                    displaytimeload.append(x)
            settingsload.close()

            if displaytimeload[0] == "1":
                time.sleep(2.5)
            elif displaytimeload[0] == "2":
                time.sleep(1)
            elif displaytimeload[0] == "2":
                time.sleep(0.5)

            # Hide cards
            card0.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card1.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card2.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card3.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card4.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card5.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
                waithere()
            card6.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card7.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card8.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card9.config(image = inverted_tiles_img)
                
            # Status & attempts label
            status_label = Label(lvl02, text="Game Started!")
            attempts_label = Label(lvl02, text="Attempts: " + str(attempts) + "     |")

            attempts_label.grid(row = 0, column = 0)
            status_label.grid(row = 0, column = 1)

            # Countdown timer
            def clock():
                global timer02, sec
                timer02[1] -= 1

                # Losing game after countdown is finished
                if timer02[1] == -1 and timer02[0] != 0:
                    timer02[0] -= 1
                    timer02[1] += 60

                timer02_label.config(text = str(timer02[0]) + ":" + str(timer02[1]))

                if timer02[0] == 0 and timer02[1] == 0:
                    # Status label
                    status_label.config(text="Lose! Try Again!", font=("Helvetica", 48))

                    # Pause after losing game
                    def waithere():
                        var = IntVar()
                        screen.after(500, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    time.sleep(2.5)

                    # Returning back to level menu
                    level_top.destroy()
                    lvl02_top.destroy()
                    lvl02.destroy()
                    lvl02_bottom.destroy()

                    start() 

                timer02_label.after(1000, clock)


            timer02_label = Label(lvl02_bottom, text = str(timer02[0]) + ":" + str(timer02[1]), font=("Helvetica", 32))
            timer02_label.pack(pady=20)

            clock()

        # Lvl 02 end

        #
        #
        #
        #
        # Level 03
        def lvl03():
            top1.destroy()
            top2.destroy()
            twovtwo_btn.destroy()
            back_btn.destroy()

            global displaytimeload

            # Images
            inverted_tiles_img = Image.open(pathname+r"\img\content\inverted_tiles.png")
            inverted_tiles_img = inverted_tiles_img.resize((128, 128), Image.ANTIALIAS)
            inverted_tiles_img = ImageTk.PhotoImage(inverted_tiles_img)
            inverted_tiles = Label(image=inverted_tiles_img)
            inverted_tiles.image = inverted_tiles_img

            c01_img = Image.open(pathname+r"\img\content\01.png")
            c01_img = c01_img.resize((128, 128), Image.ANTIALIAS)
            c01_img = ImageTk.PhotoImage(c01_img)
            c01 = Label(image=c01_img)
            c01.image = c01_img

            c02_img = Image.open(pathname+r"\img\content\02.png")
            c02_img = c02_img.resize((128, 128), Image.ANTIALIAS)
            c02_img = ImageTk.PhotoImage(c02_img)
            c02 = Label(image=c02_img)
            c02.image = c02_img

            c03_img = Image.open(pathname+r"\img\content\03.png")
            c03_img = c03_img.resize((128, 128), Image.ANTIALIAS)
            c03_img = ImageTk.PhotoImage(c03_img)
            c03 = Label(image=c03_img)
            c03.image = c03_img

            # Random cards
            random_cards = [1,1,1,2,2,2,3,3,3]
            random.shuffle(random_cards)

            # Frames
            level_top = Frame(screen)
            level_top.pack(pady = 20, side=TOP)

            lvl03_top = Frame(screen)
            lvl03_top.pack(pady = 20, side=TOP)

            lvl03 = Frame(screen)
            lvl03.pack(pady = 20, side = TOP)

            lvl03_bottom = Frame(screen)
            lvl03_bottom.pack(pady = 100, side=BOTTOM)

            # Show cards
            def show_cards(c, card, number):
                if c["text"] == "":
                    def waithere():
                        var = IntVar()
                        screen.after(100, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    # Show images
                    if card == 1:
                        c["image"] = c01_img
                    elif card == 2:
                        c["image"] = c02_img
                    elif card == 3:
                        c["image"] = c03_img
                

            #Functions for clicking buttons
            def button_click(c, card, number):
                global count, answer_list, answer_dict, attempts, correct
                if c["text"] == "" and count < 3:
                    if card == 1:
                        # Change image
                        c["text"] = "1"
                        c["image"] = c01_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "1"
                    elif card == 2:
                        # Change image
                        c["text"] = "2"
                        c["image"] = c02_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "2"
                    elif card == 3:
                        # Change image
                        c["text"] = "3"
                        c["image"] = c03_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "3"

                    # Counter for steps
                    count += 1
                
                # Start to determine correct answers
                if len(answer_list) == 3:
                    if random_cards[answer_list[0]] == random_cards[answer_list[1]] and random_cards[answer_list[0]] == random_cards[answer_list[2]] and random_cards[answer_list[1]] == random_cards[answer_list[2]]:
                        # Attempt counter
                        attempts += 1
                        attempts_label.config(text="Attempts: " + str(attempts) + "     |")
                        # Status label
                        status_label.config(text="  Match!")
                        # Disabling button if correct answer
                        for key in answer_dict:
                            key["state"] = "disabled"
                        # Reseting temp
                        count = 0
                        answer_list = []
                        answer_dict = {}
                        # Counting correct answers
                        correct += 1
                    else:
                        # Attempt counter
                        attempts += 1
                        attempts_label.config(text="Attempts: " + str(attempts) + "     |")
                        # Status label
                        status_label.config(text="  Incorrect!")
                        # Reseting temp
                        count = 0
                        answer_list = []

                        # Waittime after incorrect answer
                        def waithere():
                            var = IntVar()
                            screen.after(10, var.set, 1)
                            screen.wait_variable(var)
                        waithere()
                        time.sleep(1)

                        # Reset the buttons
                        for key in answer_dict:
                            key["text"] = ""
                            key["image"] = inverted_tiles_img

                        # Reseting temp
                        answer_dict = {}
                if correct == 3:
                    # Status win
                    status_label.config(text="Win!", font=("Helvetica", 48))

                    # Pause after winning the game
                    def waithere():
                        var = IntVar()
                        screen.after(500, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    time.sleep(2.5)

                    # Auto save game
                    with open(pathname+"\savegame.txt", "r") as file:
                        savegame = file.read()
                        savegame = savegame.replace("lvl04 = 0", "lvl04 = 1")

                    with open(pathname+"\savegame.txt", "w") as file:
                        file.write(savegame)

                    # Returing back to level menu
                    level_top.destroy()
                    lvl03_top.destroy()
                    lvl03.destroy()
                    lvl03_bottom.destroy()
                    
                    start()

            # Level logo
            level_label = Label(level_top, image = level03_img, width= 130, height=130)
            level_label.pack(pady = 10)

            # Playcards
            card0 = Button(lvl03_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card0, random_cards[0], 0))
            card1 = Button(lvl03_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card1, random_cards[1], 1))
            card2 = Button(lvl03_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card2, random_cards[2], 2))
            card3 = Button(lvl03_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card3, random_cards[3], 3))
            card4 = Button(lvl03_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card4, random_cards[4], 4))
            card5 = Button(lvl03_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card5, random_cards[5], 5))
            card6 = Button(lvl03_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card6, random_cards[6], 6))
            card7 = Button(lvl03_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card7, random_cards[7], 7))
            card8 = Button(lvl03_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card8, random_cards[8], 8))

            # Griding playcards
            card0.grid(row = 0, column = 0)
            card1.grid(row = 0, column = 1)
            card2.grid(row = 0, column = 2)
            card3.grid(row = 1, column = 0)
            card4.grid(row = 1, column = 1)
            card5.grid(row = 1, column = 2)
            card6.grid(row = 2, column = 0)
            card7.grid(row = 2, column = 1)
            card8.grid(row = 2, column = 2)

            cards = [card0, card1, card2, card3, card4, card5, card6, card7, card8]
        
            # Show cards
            i = 0
            for item in cards:
                show_cards(item, random_cards[i], i)
                i += 1
            
            # Wait for few seconds
            def waithere():
                var = IntVar()
                screen.after(500, var.set, 1)
                screen.wait_variable(var)
            waithere()

            # Hide cards
            settingsload = open(pathname+"\settings.txt", "r")
            settings = settingsload.read()
            i = 0
            for x in settings:
                i = 1 + i
                if i > 29:
                    displaytimeload.append(x)
            settingsload.close()

            if displaytimeload[0] == "1":
                time.sleep(2.5)
            elif displaytimeload[0] == "2":
                time.sleep(1)
            elif displaytimeload[0] == "2":
                time.sleep(0.5)

            card0.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card1.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card2.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card3.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card4.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card5.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card6.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card7.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card8.config(image = inverted_tiles_img)

            # Status & attempts label
            status_label = Label(lvl03, text="Game Started!")
            attempts_label = Label(lvl03, text="Attempts: " + str(attempts) + "     |")

            attempts_label.grid(row = 0, column = 0)
            status_label.grid(row = 0, column = 1)

            # Countdown timer
            def clock():
                global timer03, sec
                timer03[1] -= 1

                # Losing game after countdown is finished
                if timer03[1] == -1 and timer03[0] != 0:
                    timer03[0] -= 1
                    timer03[1] += 60

                timer_label.config(text = str(timer03[0]) + ":" + str(timer03[1]))

                if timer03[0] == 0 and timer03[1] == 0:
                    # Status label
                    status_label.config(text="Lose! Try Again!", font=("Helvetica", 48))

                    # Pause after losing game
                    def waithere():
                        var = IntVar()
                        screen.after(500, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    time.sleep(2.5)

                    # Returning back to level menu
                    level_top.destroy()
                    lvl03_top.destroy()
                    lvl03.destroy()
                    lvl03_bottom.destroy()

                    start() 

                timer_label.after(1000, clock)


            timer_label = Label(lvl03_bottom, text = str(timer03[0]) + ":" + str(timer03[1]), font=("Helvetica", 32))
            timer_label.pack(pady=20)

            clock()

        # Lvl 03 end

        #
        #
        #
        #
        # Level 04
        def lvl04():
            top1.destroy()
            top2.destroy()
            twovtwo_btn.destroy()
            back_btn.destroy()

            global displaytimeload

            # Images
            inverted_tiles_img = Image.open(pathname+r"\img\content\inverted_tiles.png")
            inverted_tiles_img = inverted_tiles_img.resize((128, 128), Image.ANTIALIAS)
            inverted_tiles_img = ImageTk.PhotoImage(inverted_tiles_img)
            inverted_tiles = Label(image=inverted_tiles_img)
            inverted_tiles.image = inverted_tiles_img

            c01_img = Image.open(pathname+r"\img\content\04.png")
            c01_img = c01_img.resize((128, 128), Image.ANTIALIAS)
            c01_img = ImageTk.PhotoImage(c01_img)
            c01 = Label(image=c01_img)
            c01.image = c01_img

            c02_img = Image.open(pathname+r"\img\content\05.png")
            c02_img = c02_img.resize((128, 128), Image.ANTIALIAS)
            c02_img = ImageTk.PhotoImage(c02_img)
            c02 = Label(image=c02_img)
            c02.image = c02_img

            c03_img = Image.open(pathname+r"\img\content\06.png")
            c03_img = c03_img.resize((128, 128), Image.ANTIALIAS)
            c03_img = ImageTk.PhotoImage(c03_img)
            c03 = Label(image=c03_img)
            c03.image = c03_img

            c04_img = Image.open(pathname+r"\img\content\07.png")
            c04_img = c04_img.resize((128, 128), Image.ANTIALIAS)
            c04_img = ImageTk.PhotoImage(c04_img)
            c04 = Label(image=c04_img)
            c04.image = c04_img

            c05_img = Image.open(pathname+r"\img\content\08.png")
            c05_img = c05_img.resize((128, 128), Image.ANTIALIAS)
            c05_img = ImageTk.PhotoImage(c05_img)
            c05 = Label(image=c05_img)
            c05.image = c05_img

            # Random cards
            random_cards = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5]
            random.shuffle(random_cards)

            # Frames
            level_top = Frame(screen)
            level_top.pack(pady = 20, side=TOP)

            lvl_top = Frame(screen)
            lvl_top.pack(pady = 20, side=TOP)

            lvl = Frame(screen)
            lvl.pack(pady = 20, side = TOP)

            lvl_bottom = Frame(screen)
            lvl_bottom.pack(pady = 100, side=BOTTOM)

            # Show cards
            def show_cards(c, card, number):
                if c["text"] == "":
                    def waithere():
                        var = IntVar()
                        screen.after(100, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    # Show images
                    if card == 1:
                        c["image"] = c01_img
                    elif card == 2:
                        c["image"] = c02_img
                    elif card == 3:
                        c["image"] = c03_img
                    elif card == 4:
                        c["image"] = c04_img
                    elif card == 5:
                        c["image"] = c05_img
                

            #Functions for clicking buttons
            def button_click(c, card, number):
                global count, answer_list, answer_dict, attempts, correct
                if c["text"] == "" and count < 3:
                    if card == 1:
                        # Change image
                        c["text"] = "1"
                        c["image"] = c01_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "1"
                    elif card == 2:
                        # Change image
                        c["text"] = "2"
                        c["image"] = c02_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "2"
                    elif card == 3:
                        # Change image
                        c["text"] = "3"
                        c["image"] = c03_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "3"
                    elif card == 4:
                        # Change image
                        c["text"] = "4"
                        c["image"] = c04_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "4"
                    elif card == 5:
                        # Change image
                        c["text"] = "5"
                        c["image"] = c05_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "5"

                    # Counter for steps
                    count += 1
                
                # Start to determine correct answers
                if len(answer_list) == 3:
                    if random_cards[answer_list[0]] == random_cards[answer_list[1]] and random_cards[answer_list[0]] == random_cards[answer_list[2]] and random_cards[answer_list[1]] == random_cards[answer_list[2]]:
                        # Attempt counter
                        attempts += 1
                        attempts_label.config(text="Attempts: " + str(attempts) + "     |")
                        # Status label
                        status_label.config(text="  Match!")
                        # Disabling button if correct answer
                        for key in answer_dict:
                            key["state"] = "disabled"
                        # Reseting temp
                        count = 0
                        answer_list = []
                        answer_dict = {}
                        # Counting correct answers
                        correct += 1
                    else:
                        # Attempt counter
                        attempts += 1
                        attempts_label.config(text="Attempts: " + str(attempts) + "     |")
                        # Status label
                        status_label.config(text="  Incorrect!")
                        # Reseting temp
                        count = 0
                        answer_list = []

                        # Waittime after incorrect answer
                        def waithere():
                            var = IntVar()
                            screen.after(10, var.set, 1)
                            screen.wait_variable(var)
                        waithere()
                        time.sleep(1)

                        # Reset the buttons
                        for key in answer_dict:
                            key["text"] = ""
                            key["image"] = inverted_tiles_img

                        # Reseting temp
                        answer_dict = {}
                if correct == 5:
                    # Status win
                    status_label.config(text="Win!", font=("Helvetica", 48))

                    # Pause after winning the game
                    def waithere():
                        var = IntVar()
                        screen.after(500, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    time.sleep(2.5)

                    # Auto save game
                    with open(pathname+"\savegame.txt", "r") as file:
                        savegame = file.read()
                        savegame = savegame.replace("lvl05 = 0", "lvl05 = 1")

                    with open(pathname+"\savegame.txt", "w") as file:
                        file.write(savegame)

                    # Returing back to level menu
                    level_top.destroy()
                    lvl_top.destroy()
                    lvl.destroy()
                    lvl_bottom.destroy()
                    
                    start()

            # Level logo
            level_label = Label(level_top, image = level04_img, width= 130, height=130)
            level_label.pack(pady = 10)

            # Playcards
            card0 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card0, random_cards[0], 0))
            card1 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card1, random_cards[1], 1))
            card2 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card2, random_cards[2], 2))
            card3 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card3, random_cards[3], 3))
            card4 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card4, random_cards[4], 4))
            card5 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card5, random_cards[5], 5))
            card6 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card6, random_cards[6], 6))
            card7 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card7, random_cards[7], 7))
            card8 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card8, random_cards[8], 8))
            card9 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card9, random_cards[9], 9))
            card10 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card10, random_cards[10], 10))
            card11 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card11, random_cards[11], 11))
            card12 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card12, random_cards[12], 12))
            card13 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card13, random_cards[13], 13))
            card14 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card14, random_cards[14], 14))

            # Griding playcards
            card0.grid(row = 0, column = 0)
            card1.grid(row = 0, column = 1)
            card2.grid(row = 0, column = 2)
            card3.grid(row = 0, column = 3)
            card4.grid(row = 0, column = 4)
            card5.grid(row = 1, column = 0)
            card6.grid(row = 1, column = 1)
            card7.grid(row = 1, column = 2)
            card8.grid(row = 1, column = 3)
            card9.grid(row = 1, column = 4)
            card10.grid(row = 2, column = 0)
            card11.grid(row = 2, column = 1)
            card12.grid(row = 2, column = 2)
            card13.grid(row = 2, column = 3)
            card14.grid(row = 2, column = 4)

            cards = [card0, card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14]

            # Show cards
            i = 0
            for item in cards:
                show_cards(item, random_cards[i], i)
                i += 1
            
            # Wait for few seconds
            def waithere():
                var = IntVar()
                screen.after(500, var.set, 1)
                screen.wait_variable(var)
            waithere()

            # Hide cards
            settingsload = open(pathname+"\settings.txt", "r")
            settings = settingsload.read()
            i = 0
            for x in settings:
                i = 1 + i
                if i > 29:
                    displaytimeload.append(x)
            settingsload.close()

            if displaytimeload[0] == "1":
                time.sleep(2.5)
            elif displaytimeload[0] == "2":
                time.sleep(1)
            elif displaytimeload[0] == "2":
                time.sleep(0.5)

            card0.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card1.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card2.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card3.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card4.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card5.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card6.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card7.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card8.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card9.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card10.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card11.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card12.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card13.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card14.config(image = inverted_tiles_img)

            # Status label
            status_label = Label(lvl, text="Game Started!")
            attempts_label = Label(lvl, text="Attempts: " + str(attempts) + "     |")

            attempts_label.grid(row = 0, column = 0)
            status_label.grid(row = 0, column = 1)

            # Countdown timer
            def clock():
                global timer04, sec
                timer04[1] -= 1

                # Losing game after countdown is finished
                if timer04[1] == -1 and timer04[0] != 0:
                    timer04[0] -= 1
                    timer04[1] += 60

                timer_label.config(text = str(timer04[0]) + ":" + str(timer04[1]))

                if timer04[0] == 0 and timer04[1] == 0:
                    # Status label
                    status_label.config(text="Lose! Try Again!", font=("Helvetica", 48))

                    # Pause after losing game
                    def waithere():
                        var = IntVar()
                        screen.after(500, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    time.sleep(2.5)

                    # Returning back to level menu
                    level_top.destroy()
                    lvl_top.destroy()
                    lvl.destroy()
                    lvl_bottom.destroy()

                    start() 

                timer_label.after(1000, clock)


            timer_label = Label(lvl_bottom, text = str(timer04[0]) + ":" + str(timer04[1]), font=("Helvetica", 32))
            timer_label.pack(pady=20)

            clock()

        # Lvl 04 end

        #
        #
        #
        #
        # Level 05
        def lvl05():
            top1.destroy()
            top2.destroy()
            twovtwo_btn.destroy()
            back_btn.destroy()

            global displaytimeload

            # Images
            inverted_tiles_img = Image.open(pathname+r"\img\content\inverted_tiles.png")
            inverted_tiles_img = inverted_tiles_img.resize((128, 128), Image.ANTIALIAS)
            inverted_tiles_img = ImageTk.PhotoImage(inverted_tiles_img)
            inverted_tiles = Label(image=inverted_tiles_img)
            inverted_tiles.image = inverted_tiles_img

            c01_img = Image.open(pathname+r"\img\content\09.png")
            c01_img = c01_img.resize((128, 128), Image.ANTIALIAS)
            c01_img = ImageTk.PhotoImage(c01_img)
            c01 = Label(image=c01_img)
            c01.image = c01_img

            c02_img = Image.open(pathname+r"\img\content\10.png")
            c02_img = c02_img.resize((128, 128), Image.ANTIALIAS)
            c02_img = ImageTk.PhotoImage(c02_img)
            c02 = Label(image=c02_img)
            c02.image = c02_img

            c03_img = Image.open(pathname+r"\img\content\11.png")
            c03_img = c03_img.resize((128, 128), Image.ANTIALIAS)
            c03_img = ImageTk.PhotoImage(c03_img)
            c03 = Label(image=c03_img)
            c03.image = c03_img

            c04_img = Image.open(pathname+r"\img\content\12.png")
            c04_img = c04_img.resize((128, 128), Image.ANTIALIAS)
            c04_img = ImageTk.PhotoImage(c04_img)
            c04 = Label(image=c04_img)
            c04.image = c04_img

            c05_img = Image.open(pathname+r"\img\content\13.png")
            c05_img = c05_img.resize((128, 128), Image.ANTIALIAS)
            c05_img = ImageTk.PhotoImage(c05_img)
            c05 = Label(image=c05_img)
            c05.image = c05_img

            c06_img = Image.open(pathname+r"\img\content\14.png")
            c06_img = c06_img.resize((128, 128), Image.ANTIALIAS)
            c06_img = ImageTk.PhotoImage(c06_img)
            c06 = Label(image=c06_img)
            c06.image = c06_img

            c07_img = Image.open(pathname+r"\img\content\15.png")
            c07_img = c07_img.resize((128, 128), Image.ANTIALIAS)
            c07_img = ImageTk.PhotoImage(c07_img)
            c07 = Label(image=c07_img)
            c07.image = c07_img

            c08_img = Image.open(pathname+r"\img\content\16.png")
            c08_img = c08_img.resize((128, 128), Image.ANTIALIAS)
            c08_img = ImageTk.PhotoImage(c08_img)
            c08 = Label(image=c08_img)
            c08.image = c08_img

            c09_img = Image.open(pathname+r"\img\content\17.png")
            c09_img = c09_img.resize((128, 128), Image.ANTIALIAS)
            c09_img = ImageTk.PhotoImage(c09_img)
            c09 = Label(image=c09_img)
            c09.image = c09_img

            c10_img = Image.open(pathname+r"\img\content\18.png")
            c10_img = c10_img.resize((128, 128), Image.ANTIALIAS)
            c10_img = ImageTk.PhotoImage(c10_img)
            c10 = Label(image=c10_img)
            c10.image = c10_img

            # Random cards
            random_cards = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10]
            random.shuffle(random_cards)

            # Frames
            level_top = Frame(screen)
            level_top.pack(pady = 20, side=TOP)

            lvl_top = Frame(screen)
            lvl_top.pack(pady = 20, side=TOP)

            lvl = Frame(screen)
            lvl.pack(pady = 20, side = TOP)

            lvl_bottom = Frame(screen)
            lvl_bottom.pack(side=BOTTOM)

            # Show cards
            def show_cards(c, card, number):
                if c["text"] == "":
                    def waithere():
                        var = IntVar()
                        screen.after(100, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    # Show images
                    if card == 1:
                        c["image"] = c01_img
                    elif card == 2:
                        c["image"] = c02_img
                    elif card == 3:
                        c["image"] = c03_img
                    elif card == 4:
                        c["image"] = c04_img
                    elif card == 5:
                        c["image"] = c05_img
                    elif card == 6:
                        c["image"] = c06_img
                    elif card == 7:
                        c["image"] = c07_img
                    elif card == 8:
                        c["image"] = c08_img
                    elif card == 9:
                        c["image"] = c09_img
                    elif card == 10:
                        c["image"] = c10_img
                

            #Functions for clicking buttons
            def button_click(c, card, number):
                global count, answer_list, answer_dict, attempts, correct
                if c["text"] == "" and count < 2:
                    if card == 1:
                        # Change image
                        c["text"] = "1"
                        c["image"] = c01_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "1"
                    elif card == 2:
                        # Change image
                        c["text"] = "2"
                        c["image"] = c02_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "2"
                    elif card == 3:
                        # Change image
                        c["text"] = "3"
                        c["image"] = c03_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "3"
                    elif card == 4:
                        # Change image
                        c["text"] = "4"
                        c["image"] = c04_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "4"
                    elif card == 5:
                        # Change image
                        c["text"] = "5"
                        c["image"] = c05_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "5"
                    elif card == 6:
                        # Change image
                        c["text"] = "6"
                        c["image"] = c06_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "6"
                    elif card == 7:
                        # Change image
                        c["text"] = "7"
                        c["image"] = c07_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "7"
                    elif card == 8:
                        # Change image
                        c["text"] = "8"
                        c["image"] = c08_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "8"
                    elif card == 9:
                        # Change image
                        c["text"] = "9"
                        c["image"] = c09_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "9"
                    elif card == 10:
                        # Change image
                        c["text"] = "10"
                        c["image"] = c10_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "10"

                    # Counter for steps
                    count += 1
                
                # Start to determine correct answers
                if len(answer_list) == 2:
                    if random_cards[answer_list[0]] == random_cards[answer_list[1]]:
                        # Attempt counter
                        attempts += 1
                        attempts_label.config(text="Attempts: " + str(attempts) + "     |")
                        # Status label
                        status_label.config(text="  Match!")
                        # Disabling button if correct answer
                        for key in answer_dict:
                            key["state"] = "disabled"
                        # Reseting temp
                        count = 0
                        answer_list = []
                        answer_dict = {}
                        # Counting correct answers
                        correct += 1
                    else:
                        # Attempt counter
                        attempts += 1
                        attempts_label.config(text="Attempts: " + str(attempts) + "     |")
                        # Status label
                        status_label.config(text="  Incorrect!")
                        # Reseting temp
                        count = 0
                        answer_list = []

                        # Waittime after incorrect answer
                        def waithere():
                            var = IntVar()
                            screen.after(10, var.set, 1)
                            screen.wait_variable(var)
                        waithere()
                        time.sleep(1)

                        # Reset the buttons
                        for key in answer_dict:
                            key["text"] = ""
                            key["image"] = inverted_tiles_img

                        # Reseting temp
                        answer_dict = {}
                if correct == 10:
                    # Status win
                    status_label.config(text="Win!", font=("Helvetica", 48))

                    # Pause after winning the game
                    def waithere():
                        var = IntVar()
                        screen.after(500, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    time.sleep(2.5)

                    # Auto save game
                    with open(pathname+"\savegame.txt", "r") as file:
                        savegame = file.read()
                        savegame = savegame.replace("lvl06 = 0", "lvl06 = 1")

                    with open(pathname+"\savegame.txt", "w") as file:
                        file.write(savegame)

                    # Returing back to level menu
                    level_top.destroy()
                    lvl_top.destroy()
                    lvl.destroy()
                    lvl_bottom.destroy()
                    
                    start()

            # Level logo
            level_label = Label(level_top, image = level05_img, width= 130, height=130)
            timer_label = Label(level_top, text = str(timer05[0]) + ":" + str(timer05[1]), font=("Helvetica", 32))

            level_label.grid(row = 0, column = 0)
            timer_label.grid(row = 0, column = 1)

            # Playcards
            card0 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card0, random_cards[0], 0))
            card1 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card1, random_cards[1], 1))
            card2 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card2, random_cards[2], 2))
            card3 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card3, random_cards[3], 3))
            card4 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card4, random_cards[4], 4))
            card5 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card5, random_cards[5], 5))
            card6 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card6, random_cards[6], 6))
            card7 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card7, random_cards[7], 7))
            card8 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card8, random_cards[8], 8))
            card9 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card9, random_cards[9], 9))
            card10 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card10, random_cards[10], 10))
            card11 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card11, random_cards[11], 11))
            card12 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card12, random_cards[12], 12))
            card13 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card13, random_cards[13], 13))
            card14 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card14, random_cards[14], 14))
            card15 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card15, random_cards[15], 15))
            card16 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card16, random_cards[16], 16))
            card17 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card17, random_cards[17], 17))
            card18 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card18, random_cards[18], 18))
            card19 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card19, random_cards[19], 19))

            # Griding playcards
            card0.grid(row = 0, column = 0)
            card1.grid(row = 0, column = 1)
            card2.grid(row = 0, column = 2)
            card3.grid(row = 0, column = 3)
            card4.grid(row = 0, column = 4)
            card5.grid(row = 1, column = 0)
            card6.grid(row = 1, column = 1)
            card7.grid(row = 1, column = 2)
            card8.grid(row = 1, column = 3)
            card9.grid(row = 1, column = 4)
            card10.grid(row = 2, column = 0)
            card11.grid(row = 2, column = 1)
            card12.grid(row = 2, column = 2)
            card13.grid(row = 2, column = 3)
            card14.grid(row = 2, column = 4)
            card15.grid(row = 3, column = 0)
            card16.grid(row = 3, column = 1)
            card17.grid(row = 3, column = 2)
            card18.grid(row = 3, column = 3)
            card19.grid(row = 3, column = 4)

            cards = [card0, card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17, card18, card19]

            # Show cards
            i = 0
            for item in cards:
                show_cards(item, random_cards[i], i)
                i += 1
                
            # Wait for few seconds
            def waithere():
                var = IntVar()
                screen.after(500, var.set, 1)
                screen.wait_variable(var)
            waithere()

            settingsload = open(pathname+"\settings.txt", "r")
            settings = settingsload.read()
            i = 0
            for x in settings:
                i = 1 + i
                if i > 29:
                    displaytimeload.append(x)
            settingsload.close()

            if displaytimeload[0] == "1":
                time.sleep(2.5)
            elif displaytimeload[0] == "2":
                time.sleep(1)
            elif displaytimeload[0] == "2":
                time.sleep(0.5)

            # Hide cards
            card0.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card1.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card2.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card3.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card4.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card5.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
                waithere()
            card6.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card7.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card8.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card9.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card10.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card11.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card12.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card13.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card14.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card15.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
                waithere()
            card16.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card17.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card18.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card19.config(image = inverted_tiles_img)
                
            # Status label
            status_label = Label(lvl, text="Game Started!")
            attempts_label = Label(lvl, text="Attempts: " + str(attempts) + "     |")

            attempts_label.grid(row = 0, column = 0)
            status_label.grid(row = 0, column = 1)

            # Countdown timer
            def clock():
                global timer05, sec
                timer05[1] -= 1
                print(timer05)

                # Losing game after countdown is finished
                if timer05[1] == -1 and timer05[0] != 0:
                    timer05[0] -= 1
                    timer05[1] += 60

                timer_label.config(text = str(timer05[0]) + ":" + str(timer05[1]))

                if timer05[0] == 0 and timer05[1] == 0:
                    # Status label
                    status_label.config(text="Lose! Try Again!", font=("Helvetica", 48))

                    # Pause after losing game
                    def waithere():
                        var = IntVar()
                        screen.after(500, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    time.sleep(2.5)

                    # Returning back to level menu
                    level_top.destroy()
                    lvl_top.destroy()
                    lvl.destroy()
                    lvl_bottom.destroy()

                    start() 

                timer_label.after(1000, clock)

            clock()

        # Lvl 05 end

        #
        #
        #
        #
        # Level 06
        def lvl06():
            top1.destroy()
            top2.destroy()
            twovtwo_btn.destroy()
            back_btn.destroy()

            global displaytimeload

            # Images
            inverted_tiles_img = Image.open(pathname+r"\img\content\inverted_tiles.png")
            inverted_tiles_img = inverted_tiles_img.resize((128, 128), Image.ANTIALIAS)
            inverted_tiles_img = ImageTk.PhotoImage(inverted_tiles_img)
            inverted_tiles = Label(image=inverted_tiles_img)
            inverted_tiles.image = inverted_tiles_img

            c01_img = Image.open(pathname+r"\img\content\09.png")
            c01_img = c01_img.resize((128, 128), Image.ANTIALIAS)
            c01_img = ImageTk.PhotoImage(c01_img)
            c01 = Label(image=c01_img)
            c01.image = c01_img

            c02_img = Image.open(pathname+r"\img\content\10.png")
            c02_img = c02_img.resize((128, 128), Image.ANTIALIAS)
            c02_img = ImageTk.PhotoImage(c02_img)
            c02 = Label(image=c02_img)
            c02.image = c02_img

            c03_img = Image.open(pathname+r"\img\content\11.png")
            c03_img = c03_img.resize((128, 128), Image.ANTIALIAS)
            c03_img = ImageTk.PhotoImage(c03_img)
            c03 = Label(image=c03_img)
            c03.image = c03_img

            c04_img = Image.open(pathname+r"\img\content\12.png")
            c04_img = c04_img.resize((128, 128), Image.ANTIALIAS)
            c04_img = ImageTk.PhotoImage(c04_img)
            c04 = Label(image=c04_img)
            c04.image = c04_img

            c05_img = Image.open(pathname+r"\img\content\13.png")
            c05_img = c05_img.resize((128, 128), Image.ANTIALIAS)
            c05_img = ImageTk.PhotoImage(c05_img)
            c05 = Label(image=c05_img)
            c05.image = c05_img

            c06_img = Image.open(pathname+r"\img\content\14.png")
            c06_img = c06_img.resize((128, 128), Image.ANTIALIAS)
            c06_img = ImageTk.PhotoImage(c06_img)
            c06 = Label(image=c06_img)
            c06.image = c06_img

            c07_img = Image.open(pathname+r"\img\content\15.png")
            c07_img = c07_img.resize((128, 128), Image.ANTIALIAS)
            c07_img = ImageTk.PhotoImage(c07_img)
            c07 = Label(image=c07_img)
            c07.image = c07_img

            c08_img = Image.open(pathname+r"\img\content\16.png")
            c08_img = c08_img.resize((128, 128), Image.ANTIALIAS)
            c08_img = ImageTk.PhotoImage(c08_img)
            c08 = Label(image=c08_img)
            c08.image = c08_img

            c09_img = Image.open(pathname+r"\img\content\17.png")
            c09_img = c09_img.resize((128, 128), Image.ANTIALIAS)
            c09_img = ImageTk.PhotoImage(c09_img)
            c09 = Label(image=c09_img)
            c09.image = c09_img

            c10_img = Image.open(pathname+r"\img\content\18.png")
            c10_img = c10_img.resize((128, 128), Image.ANTIALIAS)
            c10_img = ImageTk.PhotoImage(c10_img)
            c10 = Label(image=c10_img)
            c10.image = c10_img

            # Random cards
            random_cards = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10]
            random.shuffle(random_cards)

            # Frames
            level_top = Frame(screen)
            level_top.pack(pady = 20, side=TOP)

            lvl_top = Frame(screen)
            lvl_top.pack(pady = 20, side=TOP)

            lvl = Frame(screen)
            lvl.pack(pady = 20, side = TOP)

            lvl_bottom = Frame(screen)
            lvl_bottom.pack(pady = 100, side=BOTTOM)

            # Show cards
            def show_cards(c, card, number):
                if c["text"] == "":
                    def waithere():
                        var = IntVar()
                        screen.after(100, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    # Show images
                    if card == 1:
                        c["image"] = c01_img
                    elif card == 2:
                        c["image"] = c02_img
                    elif card == 3:
                        c["image"] = c03_img
                    elif card == 4:
                        c["image"] = c04_img
                    elif card == 5:
                        c["image"] = c05_img
                    elif card == 6:
                        c["image"] = c06_img
                    elif card == 7:
                        c["image"] = c07_img
                    elif card == 8:
                        c["image"] = c08_img
                    elif card == 9:
                        c["image"] = c09_img
                    elif card == 10:
                        c["image"] = c10_img
                

            #Functions for clicking buttons
            def button_click(c, card, number):
                global count, answer_list, answer_dict, attempts, correct
                if c["text"] == "" and count < 3:
                    if card == 1:
                        # Change image
                        c["text"] = "1"
                        c["image"] = c01_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "1"
                    elif card == 2:
                        # Change image
                        c["text"] = "2"
                        c["image"] = c02_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "2"
                    elif card == 3:
                        # Change image
                        c["text"] = "3"
                        c["image"] = c03_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "3"
                    elif card == 4:
                        # Change image
                        c["text"] = "4"
                        c["image"] = c04_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "4"
                    elif card == 5:
                        # Change image
                        c["text"] = "5"
                        c["image"] = c05_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "5"
                    elif card == 6:
                        # Change image
                        c["text"] = "6"
                        c["image"] = c06_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "6"
                    elif card == 7:
                        # Change image
                        c["text"] = "7"
                        c["image"] = c07_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "7"
                    elif card == 8:
                        # Change image
                        c["text"] = "8"
                        c["image"] = c08_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "8"
                    elif card == 9:
                        # Change image
                        c["text"] = "9"
                        c["image"] = c09_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "9"
                    elif card == 10:
                        # Change image
                        c["text"] = "10"
                        c["image"] = c10_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "10"

                    # Counter for steps
                    count += 1
                
                # Start to determine correct answers
                if len(answer_list) == 3:
                    if random_cards[answer_list[0]] == random_cards[answer_list[1]] and random_cards[answer_list[0]] == random_cards[answer_list[2]] and random_cards[answer_list[1]] == random_cards[answer_list[2]]:
                        # Attempt counter
                        attempts += 1
                        attempts_label.config(text="Attempts: " + str(attempts) + "     |")
                        # Status label
                        status_label.config(text="  Match!")
                        # Disabling button if correct answer
                        for key in answer_dict:
                            key["state"] = "disabled"
                        # Reseting temp
                        count = 0
                        answer_list = []
                        answer_dict = {}
                        # Counting correct answers
                        correct += 1
                    else:
                        # Attempt counter
                        attempts += 1
                        attempts_label.config(text="Attempts: " + str(attempts) + "     |")
                        # Status label
                        status_label.config(text="  Incorrect!")
                        # Reseting temp
                        count = 0
                        answer_list = []

                        # Waittime after incorrect answer
                        def waithere():
                            var = IntVar()
                            screen.after(10, var.set, 1)
                            screen.wait_variable(var)
                        waithere()
                        time.sleep(1)

                        # Reset the buttons
                        for key in answer_dict:
                            key["text"] = ""
                            key["image"] = inverted_tiles_img

                        # Reseting temp
                        answer_dict = {}
                if correct == 10:
                    # Status win
                    status_label.config(text="Win!", font=("Helvetica", 48))

                    # Pause after winning the game
                    def waithere():
                        var = IntVar()
                        screen.after(500, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    time.sleep(2.5)

                    # Auto save game
                    with open(pathname+"\savegame.txt", "r") as file:
                        savegame = file.read()
                        savegame = savegame.replace("lvl07 = 0", "lvl07 = 1")

                    with open(pathname+"\savegame.txt", "w") as file:
                        file.write(savegame)

                    # Returing back to level menu
                    level_top.destroy()
                    lvl_top.destroy()
                    lvl.destroy()
                    lvl_bottom.destroy()
                    
                    start()

            # Level logo
            level_label = Label(level_top, image = level06_img, width= 130, height=130)
            timer_label = Label(level_top, text = str(timer06[0]) + ":" + str(timer06[1]), font=("Helvetica", 32))

            level_label.grid(row = 0, column = 0)
            timer_label.grid(row = 0, column = 1)

            # Playcards
            card0 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card0, random_cards[0], 0))
            card1 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card1, random_cards[1], 1))
            card2 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card2, random_cards[2], 2))
            card3 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card3, random_cards[3], 3))
            card4 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card4, random_cards[4], 4))
            card5 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card5, random_cards[5], 5))
            card6 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card6, random_cards[6], 6))
            card7 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card7, random_cards[7], 7))
            card8 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card8, random_cards[8], 8))
            card9 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card9, random_cards[9], 9))
            card10 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card10, random_cards[10], 10))
            card11 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card11, random_cards[11], 11))
            card12 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card12, random_cards[12], 12))
            card13 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card13, random_cards[13], 13))
            card14 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card14, random_cards[14], 14))
            card15 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card15, random_cards[15], 15))
            card16 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card16, random_cards[16], 16))
            card17 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card17, random_cards[17], 17))
            card18 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card18, random_cards[18], 18))
            card19 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card19, random_cards[19], 19))
            card20 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card20, random_cards[20], 20))
            card21 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card21, random_cards[21], 21))
            card22 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card22, random_cards[22], 22))
            card23 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card23, random_cards[23], 23))
            card24 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card24, random_cards[24], 24))
            card25 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card25, random_cards[25], 25))
            card26 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card26, random_cards[26], 26))
            card27 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card27, random_cards[27], 27))
            card28 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card28, random_cards[28], 28))
            card29 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card29, random_cards[29], 29))

            # Griding playcards
            card0.grid(row = 0, column = 0)
            card1.grid(row = 0, column = 1)
            card2.grid(row = 0, column = 2)
            card3.grid(row = 0, column = 3)
            card4.grid(row = 0, column = 4)
            card5.grid(row = 0, column = 5)
            card6.grid(row = 0, column = 6)
            card7.grid(row = 0, column = 7)
            card8.grid(row = 0, column = 8)
            card9.grid(row = 0, column = 9)
            card10.grid(row = 1, column = 0)
            card11.grid(row = 1, column = 1)
            card12.grid(row = 1, column = 2)
            card13.grid(row = 1, column = 3)
            card14.grid(row = 1, column = 4)
            card15.grid(row = 1, column = 5)
            card16.grid(row = 1, column = 6)
            card17.grid(row = 1, column = 7)
            card18.grid(row = 1, column = 8)
            card19.grid(row = 1, column = 9)
            card20.grid(row = 2, column = 0)
            card21.grid(row = 2, column = 1)
            card22.grid(row = 2, column = 2)
            card23.grid(row = 2, column = 3)
            card24.grid(row = 2, column = 4)
            card25.grid(row = 2, column = 5)
            card26.grid(row = 2, column = 6)
            card27.grid(row = 2, column = 7)
            card28.grid(row = 2, column = 8)
            card29.grid(row = 2, column = 9)

            cards = [card0, card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15,
                    card16, card17, card18, card19, card20, card21, card22, card23, card24, card25, card26, card27, card28, card29]

            # Show cards
            i = 0
            for item in cards:
                show_cards(item, random_cards[i], i)
                i += 1
            
            # Wait for few seconds
            def waithere():
                var = IntVar()
                screen.after(500, var.set, 1)
                screen.wait_variable(var)
            waithere()

            settingsload = open(pathname+"\settings.txt", "r")
            settings = settingsload.read()
            i = 0
            for x in settings:
                i = 1 + i
                if i > 29:
                    displaytimeload.append(x)
            settingsload.close()

            if displaytimeload[0] == "1":
                time.sleep(2.5)
            elif displaytimeload[0] == "2":
                time.sleep(1)
            elif displaytimeload[0] == "2":
                time.sleep(0.5)

            # Hide cards
            card0.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card1.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card2.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card3.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card4.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card5.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card6.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card7.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card8.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card9.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card10.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card11.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card12.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card13.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card14.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card15.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card16.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card17.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card18.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card19.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card20.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card21.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card22.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card23.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card24.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card25.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card26.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card27.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card28.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card29.config(image = inverted_tiles_img)

            # Status label
            status_label = Label(lvl, text="Game Started!")
            attempts_label = Label(lvl, text="Attempts: " + str(attempts) + "     |")

            attempts_label.grid(row = 0, column = 0)
            status_label.grid(row = 0, column = 1)

            # Countdown timer
            def clock():
                global timer06, sec
                timer06[1] -= 1

                # Losing game after countdown is finished
                if timer06[1] == -1 and timer06[0] != 0:
                    timer06[0] -= 1
                    timer06[1] += 60

                timer_label.config(text = str(timer06[0]) + ":" + str(timer06[1]))

                if timer06[0] == 0 and timer06[1] == 0:
                    # Status label
                    status_label.config(text="Lose! Try Again!", font=("Helvetica", 48))

                    # Pause after losing game
                    def waithere():
                        var = IntVar()
                        screen.after(500, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    time.sleep(2.5)

                    # Returning back to level menu
                    level_top.destroy()
                    lvl_top.destroy()
                    lvl.destroy()
                    lvl_bottom.destroy()

                    start() 

                timer_label.after(1000, clock)

            clock()

        # Lvl 06 end

        #
        #
        #
        #
        # Level 07
        def lvl07():
            top1.destroy()
            top2.destroy()
            twovtwo_btn.destroy()
            back_btn.destroy()

            global displaytimeload

            # Images
            inverted_tiles_img = Image.open(pathname+r"\img\content\inverted_tiles.png")
            inverted_tiles_img = inverted_tiles_img.resize((128, 128), Image.ANTIALIAS)
            inverted_tiles_img = ImageTk.PhotoImage(inverted_tiles_img)
            inverted_tiles = Label(image=inverted_tiles_img)
            inverted_tiles.image = inverted_tiles_img

            c01_img = Image.open(pathname+r"\img\content\19.png")
            c01_img = c01_img.resize((128, 128), Image.ANTIALIAS)
            c01_img = ImageTk.PhotoImage(c01_img)
            c01 = Label(image=c01_img)
            c01.image = c01_img

            c02_img = Image.open(pathname+r"\img\content\20.png")
            c02_img = c02_img.resize((128, 128), Image.ANTIALIAS)
            c02_img = ImageTk.PhotoImage(c02_img)
            c02 = Label(image=c02_img)
            c02.image = c02_img

            c03_img = Image.open(pathname+r"\img\content\21.png")
            c03_img = c03_img.resize((128, 128), Image.ANTIALIAS)
            c03_img = ImageTk.PhotoImage(c03_img)
            c03 = Label(image=c03_img)
            c03.image = c03_img

            c04_img = Image.open(pathname+r"\img\content\22.png")
            c04_img = c04_img.resize((128, 128), Image.ANTIALIAS)
            c04_img = ImageTk.PhotoImage(c04_img)
            c04 = Label(image=c04_img)
            c04.image = c04_img

            c05_img = Image.open(pathname+r"\img\content\23.png")
            c05_img = c05_img.resize((128, 128), Image.ANTIALIAS)
            c05_img = ImageTk.PhotoImage(c05_img)
            c05 = Label(image=c05_img)
            c05.image = c05_img

            c06_img = Image.open(pathname+r"\img\content\24.png")
            c06_img = c06_img.resize((128, 128), Image.ANTIALIAS)
            c06_img = ImageTk.PhotoImage(c06_img)
            c06 = Label(image=c06_img)
            c06.image = c06_img

            c07_img = Image.open(pathname+r"\img\content\25.png")
            c07_img = c07_img.resize((128, 128), Image.ANTIALIAS)
            c07_img = ImageTk.PhotoImage(c07_img)
            c07 = Label(image=c07_img)
            c07.image = c07_img

            c08_img = Image.open(pathname+r"\img\content\26.png")
            c08_img = c08_img.resize((128, 128), Image.ANTIALIAS)
            c08_img = ImageTk.PhotoImage(c08_img)
            c08 = Label(image=c08_img)
            c08.image = c08_img

            c09_img = Image.open(pathname+r"\img\content\27.png")
            c09_img = c09_img.resize((128, 128), Image.ANTIALIAS)
            c09_img = ImageTk.PhotoImage(c09_img)
            c09 = Label(image=c09_img)
            c09.image = c09_img

            c10_img = Image.open(pathname+r"\img\content\28.png")
            c10_img = c10_img.resize((128, 128), Image.ANTIALIAS)
            c10_img = ImageTk.PhotoImage(c10_img)
            c10 = Label(image=c10_img)
            c10.image = c10_img

            c11_img = Image.open(pathname+r"\img\content\29.png")
            c11_img = c11_img.resize((128, 128), Image.ANTIALIAS)
            c11_img = ImageTk.PhotoImage(c11_img)
            c11 = Label(image=c11_img)
            c11.image = c11_img

            c12_img = Image.open(pathname+r"\img\content\30.png")
            c12_img = c12_img.resize((128, 128), Image.ANTIALIAS)
            c12_img = ImageTk.PhotoImage(c12_img)
            c12 = Label(image=c12_img)
            c12.image = c12_img

            c13_img = Image.open(pathname+r"\img\content\31.png")
            c13_img = c13_img.resize((128, 128), Image.ANTIALIAS)
            c13_img = ImageTk.PhotoImage(c13_img)
            c13 = Label(image=c13_img)
            c13.image = c13_img

            c14_img = Image.open(pathname+r"\img\content\32.png")
            c14_img = c14_img.resize((128, 128), Image.ANTIALIAS)
            c14_img = ImageTk.PhotoImage(c14_img)
            c14 = Label(image=c14_img)
            c14.image = c14_img

            c15_img = Image.open(pathname+r"\img\content\33.png")
            c15_img = c15_img.resize((128, 128), Image.ANTIALIAS)
            c15_img = ImageTk.PhotoImage(c15_img)
            c15 = Label(image=c15_img)
            c15.image = c15_img

            c16_img = Image.open(pathname+r"\img\content\34.png")
            c16_img = c16_img.resize((128, 128), Image.ANTIALIAS)
            c16_img = ImageTk.PhotoImage(c16_img)
            c16 = Label(image=c16_img)
            c16.image = c16_img

            c17_img = Image.open(pathname+r"\img\content\35.png")
            c17_img = c17_img.resize((128, 128), Image.ANTIALIAS)
            c17_img = ImageTk.PhotoImage(c17_img)
            c17 = Label(image=c17_img)
            c17.image = c17_img

            c18_img = Image.open(pathname+r"\img\content\36.png")
            c18_img = c18_img.resize((128, 128), Image.ANTIALIAS)
            c18_img = ImageTk.PhotoImage(c18_img)
            c18 = Label(image=c18_img)
            c18.image = c18_img

            c19_img = Image.open(pathname+r"\img\content\37.png")
            c19_img = c19_img.resize((128, 128), Image.ANTIALIAS)
            c19_img = ImageTk.PhotoImage(c19_img)
            c19 = Label(image=c19_img)
            c19.image = c19_img

            c20_img = Image.open(pathname+r"\img\content\38.png")
            c20_img = c20_img.resize((128, 128), Image.ANTIALIAS)
            c20_img = ImageTk.PhotoImage(c20_img)
            c20 = Label(image=c20_img)
            c20.image = c20_img

            # Random cards
            random_cards = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20]
            random.shuffle(random_cards)

            # Frames
            level_top = Frame(screen)
            level_top.pack(pady = 20, side=TOP)

            lvl_top = Frame(screen)
            lvl_top.pack(pady = 20, side=TOP)

            lvl = Frame(screen)
            lvl.pack(pady = 20, side = TOP)

            lvl_bottom = Frame(screen)
            lvl_bottom.pack(side=BOTTOM)

            # Show cards
            def show_cards(c, card, number):
                if c["text"] == "":
                    def waithere():
                        var = IntVar()
                        screen.after(100, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    # Show images
                    if card == 1:
                        c["image"] = c01_img
                    elif card == 2:
                        c["image"] = c02_img
                    elif card == 3:
                        c["image"] = c03_img
                    elif card == 4:
                        c["image"] = c04_img
                    elif card == 5:
                        c["image"] = c05_img
                    elif card == 6:
                        c["image"] = c06_img
                    elif card == 7:
                        c["image"] = c07_img
                    elif card == 8:
                        c["image"] = c08_img
                    elif card == 9:
                        c["image"] = c09_img
                    elif card == 10:
                        c["image"] = c10_img
                    elif card == 11:
                        c["image"] = c11_img
                    elif card == 12:
                        c["image"] = c12_img
                    elif card == 13:
                        c["image"] = c13_img
                    elif card == 14:
                        c["image"] = c14_img
                    elif card == 15:
                        c["image"] = c15_img
                    elif card == 16:
                        c["image"] = c16_img
                    elif card == 17:
                        c["image"] = c17_img
                    elif card == 18:
                        c["image"] = c18_img
                    elif card == 19:
                        c["image"] = c19_img
                    elif card == 20:
                        c["image"] = c20_img
                

            #Functions for clicking buttons
            def button_click(c, card, number):
                global count, answer_list, answer_dict, attempts, correct
                if c["text"] == "" and count < 2:
                    if card == 1:
                        # Change image
                        c["text"] = "1"
                        c["image"] = c01_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "1"
                    elif card == 2:
                        # Change image
                        c["text"] = "2"
                        c["image"] = c02_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "2"
                    elif card == 3:
                        # Change image
                        c["text"] = "3"
                        c["image"] = c03_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "3"
                    elif card == 4:
                        # Change image
                        c["text"] = "4"
                        c["image"] = c04_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "4"
                    elif card == 5:
                        # Change image
                        c["text"] = "5"
                        c["image"] = c05_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "5"
                    elif card == 6:
                        # Change image
                        c["text"] = "6"
                        c["image"] = c06_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "6"
                    elif card == 7:
                        # Change image
                        c["text"] = "7"
                        c["image"] = c07_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "7"
                    elif card == 8:
                        # Change image
                        c["text"] = "8"
                        c["image"] = c08_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "8"
                    elif card == 9:
                        # Change image
                        c["text"] = "9"
                        c["image"] = c09_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "9"
                    elif card == 10:
                        # Change image
                        c["text"] = "10"
                        c["image"] = c10_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "10"
                    elif card == 11:
                        # Change image
                        c["text"] = "11"
                        c["image"] = c11_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "11"
                    elif card == 12:
                        # Change image
                        c["text"] = "12"
                        c["image"] = c12_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "12"
                    elif card == 13:
                        # Change image
                        c["text"] = "13"
                        c["image"] = c13_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "13"
                    elif card == 14:
                        # Change image
                        c["text"] = "14"
                        c["image"] = c14_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "14"
                    elif card == 15:
                        # Change image
                        c["text"] = "15"
                        c["image"] = c15_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "15"
                    elif card == 16:
                        # Change image
                        c["text"] = "16"
                        c["image"] = c16_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "16"
                    elif card == 17:
                        # Change image
                        c["text"] = "17"
                        c["image"] = c17_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "17"
                    elif card == 18:
                        # Change image
                        c["text"] = "18"
                        c["image"] = c18_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "18"
                    elif card == 19:
                        # Change image
                        c["text"] = "19"
                        c["image"] = c19_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "19"
                    elif card == 20:
                        # Change image
                        c["text"] = "20"
                        c["image"] = c20_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "20"

                    # Counter for steps
                    count += 1
                
                # Start to determine correct answers
                if len(answer_list) == 2:
                    if random_cards[answer_list[0]] == random_cards[answer_list[1]]:
                        # Attempt counter
                        attempts += 1
                        attempts_label.config(text="Attempts: " + str(attempts) + "     |")
                        # Status label
                        status_label.config(text="  Match!")
                        # Disabling button if correct answer
                        for key in answer_dict:
                            key["state"] = "disabled"
                        # Reseting temp
                        count = 0
                        answer_list = []
                        answer_dict = {}
                        # Counting correct answers
                        correct += 1
                    else:
                        # Attempt counter
                        attempts += 1
                        attempts_label.config(text="Attempts: " + str(attempts) + "     |")
                        # Status label
                        status_label.config(text="  Incorrect!")
                        # Reseting temp
                        count = 0
                        answer_list = []

                        # Waittime after incorrect answer
                        def waithere():
                            var = IntVar()
                            screen.after(10, var.set, 1)
                            screen.wait_variable(var)
                        waithere()
                        time.sleep(1)

                        # Reset the buttons
                        for key in answer_dict:
                            key["text"] = ""
                            key["image"] = inverted_tiles_img

                        # Reseting temp
                        answer_dict = {}
                if correct == 20:
                    # Status win
                    status_label.config(text="Win!", font=("Helvetica", 48))

                    # Pause after winning the game
                    def waithere():
                        var = IntVar()
                        screen.after(500, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    time.sleep(2.5)

                    # Auto save game
                    with open(pathname+"\savegame.txt", "r") as file:
                        savegame = file.read()
                        savegame = savegame.replace("lvl08 = 0", "lvl08 = 1")

                    with open(pathname+"\savegame.txt", "w") as file:
                        file.write(savegame)

                    # Returing back to level menu
                    level_top.destroy()
                    lvl_top.destroy()
                    lvl.destroy()
                    lvl_bottom.destroy()
                    
                    start()

            # Level logo
            level_label = Label(level_top, image = level07_img, width= 130, height=130)
            timer_label = Label(level_top, text = str(timer07[0]) + ":" + str(timer07[1]), font=("Helvetica", 32))

            level_label.grid(row = 0, column = 0)
            timer_label.grid(row = 0, column = 1)

            # Playcards
            card0 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card0, random_cards[0], 0))
            card1 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card1, random_cards[1], 1))
            card2 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card2, random_cards[2], 2))
            card3 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card3, random_cards[3], 3))
            card4 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card4, random_cards[4], 4))
            card5 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card5, random_cards[5], 5))
            card6 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card6, random_cards[6], 6))
            card7 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card7, random_cards[7], 7))
            card8 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card8, random_cards[8], 8))
            card9 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card9, random_cards[9], 9))
            card10 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card10, random_cards[10], 10))
            card11 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card11, random_cards[11], 11))
            card12 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card12, random_cards[12], 12))
            card13 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card13, random_cards[13], 13))
            card14 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card14, random_cards[14], 14))
            card15 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card15, random_cards[15], 15))
            card16 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card16, random_cards[16], 16))
            card17 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card17, random_cards[17], 17))
            card18 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card18, random_cards[18], 18))
            card19 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card19, random_cards[19], 19))
            card20 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card20, random_cards[20], 20))
            card21 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card21, random_cards[21], 21))
            card22 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card22, random_cards[22], 22))
            card23 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card23, random_cards[23], 23))
            card24 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card24, random_cards[24], 24))
            card25 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card25, random_cards[25], 25))
            card26 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card26, random_cards[26], 26))
            card27 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card27, random_cards[27], 27))
            card28 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card28, random_cards[28], 28))
            card29 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card29, random_cards[29], 29))
            card30 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card30, random_cards[30], 30))
            card31 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card31, random_cards[31], 31))
            card32 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card32, random_cards[32], 32))
            card33 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card33, random_cards[33], 33))
            card34 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card34, random_cards[34], 34))
            card35 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card35, random_cards[35], 35))
            card36 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card36, random_cards[36], 36))
            card37 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card37, random_cards[37], 37))
            card38 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card38, random_cards[38], 38))
            card39 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card39, random_cards[39], 39))

            # Griding playcards
            card0.grid(row = 0, column = 0)
            card1.grid(row = 0, column = 1)
            card2.grid(row = 0, column = 2)
            card3.grid(row = 0, column = 3)
            card4.grid(row = 0, column = 4)
            card5.grid(row = 0, column = 5)
            card6.grid(row = 0, column = 6)
            card7.grid(row = 0, column = 7)
            card8.grid(row = 0, column = 8)
            card9.grid(row = 0, column = 9)
            card10.grid(row = 1, column = 0)
            card11.grid(row = 1, column = 1)
            card12.grid(row = 1, column = 2)
            card13.grid(row = 1, column = 3)
            card14.grid(row = 1, column = 4)
            card15.grid(row = 1, column = 5)
            card16.grid(row = 1, column = 6)
            card17.grid(row = 1, column = 7)
            card18.grid(row = 1, column = 8)
            card19.grid(row = 1, column = 9)
            card20.grid(row = 2, column = 0)
            card21.grid(row = 2, column = 1)
            card22.grid(row = 2, column = 2)
            card23.grid(row = 2, column = 3)
            card24.grid(row = 2, column = 4)
            card25.grid(row = 2, column = 5)
            card26.grid(row = 2, column = 6)
            card27.grid(row = 2, column = 7)
            card28.grid(row = 2, column = 8)
            card29.grid(row = 2, column = 9)
            card30.grid(row = 3, column = 0)
            card31.grid(row = 3, column = 1)
            card32.grid(row = 3, column = 2)
            card33.grid(row = 3, column = 3)
            card34.grid(row = 3, column = 4)
            card35.grid(row = 3, column = 5)
            card36.grid(row = 3, column = 6)
            card37.grid(row = 3, column = 7)
            card38.grid(row = 3, column = 8)
            card39.grid(row = 3, column = 9)

            cards = [card0, card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17, card18, card19, 
                    card20, card21, card22, card23, card24, card25, card26, card27, card28, card29, card30, card31, card32, card33, card34, card35, card36, card37, card38, card39]

            # Show cards
            i = 0
            for item in cards:
                show_cards(item, random_cards[i], i)
                i += 1
                
            # Wait for few seconds
            def waithere():
                var = IntVar()
                screen.after(500, var.set, 1)
                screen.wait_variable(var)
            waithere()
            
            settingsload = open(pathname+"\settings.txt", "r")
            settings = settingsload.read()
            i = 0
            for x in settings:
                i = 1 + i
                if i > 29:
                    displaytimeload.append(x)
            settingsload.close()

            if displaytimeload[0] == "1":
                time.sleep(2.5)
            elif displaytimeload[0] == "2":
                time.sleep(1)
            elif displaytimeload[0] == "2":
                time.sleep(0.5)

            # Hide cards
            card0.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card1.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card2.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card3.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card4.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card5.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
                waithere()
            card6.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card7.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card8.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card9.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card10.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card11.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card12.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card13.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card14.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card15.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
                waithere()
            card16.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card17.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card18.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card19.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card20.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card21.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card22.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card23.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card24.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card25.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
                waithere()
            card26.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card27.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card28.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card29.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card30.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card31.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card32.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card33.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card34.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card35.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
                waithere()
            card36.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card37.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card38.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card39.config(image = inverted_tiles_img)
                
            # Status label
            status_label = Label(lvl, text="Game Started!")
            attempts_label = Label(lvl, text="Attempts: " + str(attempts) + "     |")

            attempts_label.grid(row = 0, column = 0)
            status_label.grid(row = 0, column = 1)

            # Countdown timer
            def clock():
                global timer07, sec
                timer07[1] -= 1
                print(timer07)

                # Losing game after countdown is finished
                if timer07[1] == -1 and timer07[0] != 0:
                    timer07[0] -= 1
                    timer07[1] += 60

                timer_label.config(text = str(timer07[0]) + ":" + str(timer07[1]))

                if timer07[0] == 0 and timer07[1] == 0:
                    # Status label
                    status_label.config(text="Lose! Try Again!", font=("Helvetica", 48))

                    # Pause after losing game
                    def waithere():
                        var = IntVar()
                        screen.after(500, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    time.sleep(2.5)

                    # Returning back to level menu
                    level_top.destroy()
                    lvl_top.destroy()
                    lvl.destroy()
                    lvl_bottom.destroy()

                    start() 

                timer_label.after(1000, clock)

            clock()

        # Lvl 07 end

        #
        #
        #
        #
        # Level 08
        def lvl08():
            top1.destroy()
            top2.destroy()
            twovtwo_btn.destroy()
            back_btn.destroy()

            global displaytimeload

            # Images
            inverted_tiles_img = Image.open(pathname+r"\img\content\inverted_tiles.png")
            inverted_tiles_img = inverted_tiles_img.resize((128, 128), Image.ANTIALIAS)
            inverted_tiles_img = ImageTk.PhotoImage(inverted_tiles_img)
            inverted_tiles = Label(image=inverted_tiles_img)
            inverted_tiles.image = inverted_tiles_img

            c01_img = Image.open(pathname+r"\img\content\19.png")
            c01_img = c01_img.resize((128, 128), Image.ANTIALIAS)
            c01_img = ImageTk.PhotoImage(c01_img)
            c01 = Label(image=c01_img)
            c01.image = c01_img

            c02_img = Image.open(pathname+r"\img\content\20.png")
            c02_img = c02_img.resize((128, 128), Image.ANTIALIAS)
            c02_img = ImageTk.PhotoImage(c02_img)
            c02 = Label(image=c02_img)
            c02.image = c02_img

            c03_img = Image.open(pathname+r"\img\content\21.png")
            c03_img = c03_img.resize((128, 128), Image.ANTIALIAS)
            c03_img = ImageTk.PhotoImage(c03_img)
            c03 = Label(image=c03_img)
            c03.image = c03_img

            c04_img = Image.open(pathname+r"\img\content\22.png")
            c04_img = c04_img.resize((128, 128), Image.ANTIALIAS)
            c04_img = ImageTk.PhotoImage(c04_img)
            c04 = Label(image=c04_img)
            c04.image = c04_img

            c05_img = Image.open(pathname+r"\img\content\23.png")
            c05_img = c05_img.resize((128, 128), Image.ANTIALIAS)
            c05_img = ImageTk.PhotoImage(c05_img)
            c05 = Label(image=c05_img)
            c05.image = c05_img

            c06_img = Image.open(pathname+r"\img\content\24.png")
            c06_img = c06_img.resize((128, 128), Image.ANTIALIAS)
            c06_img = ImageTk.PhotoImage(c06_img)
            c06 = Label(image=c06_img)
            c06.image = c06_img

            c07_img = Image.open(pathname+r"\img\content\25.png")
            c07_img = c07_img.resize((128, 128), Image.ANTIALIAS)
            c07_img = ImageTk.PhotoImage(c07_img)
            c07 = Label(image=c07_img)
            c07.image = c07_img

            c08_img = Image.open(pathname+r"\img\content\26.png")
            c08_img = c08_img.resize((128, 128), Image.ANTIALIAS)
            c08_img = ImageTk.PhotoImage(c08_img)
            c08 = Label(image=c08_img)
            c08.image = c08_img

            c09_img = Image.open(pathname+r"\img\content\27.png")
            c09_img = c09_img.resize((128, 128), Image.ANTIALIAS)
            c09_img = ImageTk.PhotoImage(c09_img)
            c09 = Label(image=c09_img)
            c09.image = c09_img

            c10_img = Image.open(pathname+r"\img\content\28.png")
            c10_img = c10_img.resize((128, 128), Image.ANTIALIAS)
            c10_img = ImageTk.PhotoImage(c10_img)
            c10 = Label(image=c10_img)
            c10.image = c10_img

            c11_img = Image.open(pathname+r"\img\content\29.png")
            c11_img = c11_img.resize((128, 128), Image.ANTIALIAS)
            c11_img = ImageTk.PhotoImage(c11_img)
            c11 = Label(image=c11_img)
            c11.image = c11_img

            c12_img = Image.open(pathname+r"\img\content\30.png")
            c12_img = c12_img.resize((128, 128), Image.ANTIALIAS)
            c12_img = ImageTk.PhotoImage(c12_img)
            c12 = Label(image=c12_img)
            c12.image = c12_img

            c13_img = Image.open(pathname+r"\img\content\31.png")
            c13_img = c13_img.resize((128, 128), Image.ANTIALIAS)
            c13_img = ImageTk.PhotoImage(c13_img)
            c13 = Label(image=c13_img)
            c13.image = c13_img

            c14_img = Image.open(pathname+r"\img\content\32.png")
            c14_img = c14_img.resize((128, 128), Image.ANTIALIAS)
            c14_img = ImageTk.PhotoImage(c14_img)
            c14 = Label(image=c14_img)
            c14.image = c14_img

            c15_img = Image.open(pathname+r"\img\content\33.png")
            c15_img = c15_img.resize((128, 128), Image.ANTIALIAS)
            c15_img = ImageTk.PhotoImage(c15_img)
            c15 = Label(image=c15_img)
            c15.image = c15_img

            c16_img = Image.open(pathname+r"\img\content\34.png")
            c16_img = c16_img.resize((128, 128), Image.ANTIALIAS)
            c16_img = ImageTk.PhotoImage(c16_img)
            c16 = Label(image=c16_img)
            c16.image = c16_img

            c17_img = Image.open(pathname+r"\img\content\35.png")
            c17_img = c17_img.resize((128, 128), Image.ANTIALIAS)
            c17_img = ImageTk.PhotoImage(c17_img)
            c17 = Label(image=c17_img)
            c17.image = c17_img

            c18_img = Image.open(pathname+r"\img\content\36.png")
            c18_img = c18_img.resize((128, 128), Image.ANTIALIAS)
            c18_img = ImageTk.PhotoImage(c18_img)
            c18 = Label(image=c18_img)
            c18.image = c18_img

            c19_img = Image.open(pathname+r"\img\content\37.png")
            c19_img = c19_img.resize((128, 128), Image.ANTIALIAS)
            c19_img = ImageTk.PhotoImage(c19_img)
            c19 = Label(image=c19_img)
            c19.image = c19_img

            c20_img = Image.open(pathname+r"\img\content\38.png")
            c20_img = c20_img.resize((128, 128), Image.ANTIALIAS)
            c20_img = ImageTk.PhotoImage(c20_img)
            c20 = Label(image=c20_img)
            c20.image = c20_img

            # Random cards
            random_cards = [1,1,1,2,2,2,3,3,3,4,4,4,5,5,5,6,6,6,7,7,7,8,8,8,9,9,9,10,10,10,11,11,11,12,12,12,13,13,13,14,14,14,15,15,15,16,16,16,17,17,17,18,18,18,19,19,19,20,20,20]
            random.shuffle(random_cards)

            # Frames
            level_top = Frame(screen)
            level_top.pack(pady = 20, side=TOP)

            lvl_top = Frame(screen)
            lvl_top.pack(pady = 20, side=TOP)

            lvl = Frame(screen)
            lvl.pack(pady = 20, side = TOP)

            lvl_bottom = Frame(screen)
            lvl_bottom.pack(pady = 100, side=BOTTOM)

            # Show cards
            def show_cards(c, card, number):
                if c["text"] == "":
                    def waithere():
                        var = IntVar()
                        screen.after(100, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    # Show images
                    if card == 1:
                        c["image"] = c01_img
                    elif card == 2:
                        c["image"] = c02_img
                    elif card == 3:
                        c["image"] = c03_img
                    elif card == 4:
                        c["image"] = c04_img
                    elif card == 5:
                        c["image"] = c05_img
                    elif card == 6:
                        c["image"] = c06_img
                    elif card == 7:
                        c["image"] = c07_img
                    elif card == 8:
                        c["image"] = c08_img
                    elif card == 9:
                        c["image"] = c09_img
                    elif card == 10:
                        c["image"] = c10_img
                    elif card == 11:
                        c["image"] = c11_img
                    elif card == 12:
                        c["image"] = c12_img
                    elif card == 13:
                        c["image"] = c13_img
                    elif card == 14:
                        c["image"] = c14_img
                    elif card == 15:
                        c["image"] = c15_img
                    elif card == 16:
                        c["image"] = c16_img
                    elif card == 17:
                        c["image"] = c17_img
                    elif card == 18:
                        c["image"] = c18_img
                    elif card == 19:
                        c["image"] = c19_img
                    elif card == 20:
                        c["image"] = c20_img
                

            #Functions for clicking buttons
            def button_click(c, card, number):
                global count, answer_list, answer_dict, attempts, correct
                if c["text"] == "" and count < 3:
                    if card == 1:
                        # Change image
                        c["text"] = "1"
                        c["image"] = c01_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "1"
                    elif card == 2:
                        # Change image
                        c["text"] = "2"
                        c["image"] = c02_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "2"
                    elif card == 3:
                        # Change image
                        c["text"] = "3"
                        c["image"] = c03_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "3"
                    elif card == 4:
                        # Change image
                        c["text"] = "4"
                        c["image"] = c04_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "4"
                    elif card == 5:
                        # Change image
                        c["text"] = "5"
                        c["image"] = c05_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "5"
                    elif card == 6:
                        # Change image
                        c["text"] = "6"
                        c["image"] = c06_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "6"
                    elif card == 7:
                        # Change image
                        c["text"] = "7"
                        c["image"] = c07_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "7"
                    elif card == 8:
                        # Change image
                        c["text"] = "8"
                        c["image"] = c08_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "8"
                    elif card == 9:
                        # Change image
                        c["text"] = "9"
                        c["image"] = c09_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "9"
                    elif card == 10:
                        # Change image
                        c["text"] = "10"
                        c["image"] = c10_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "10"
                    elif card == 11:
                        # Change image
                        c["text"] = "11"
                        c["image"] = c11_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "11"
                    elif card == 12:
                        # Change image
                        c["text"] = "12"
                        c["image"] = c12_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "12"
                    elif card == 13:
                        # Change image
                        c["text"] = "13"
                        c["image"] = c13_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "13"
                    elif card == 14:
                        # Change image
                        c["text"] = "14"
                        c["image"] = c14_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "14"
                    elif card == 15:
                        # Change image
                        c["text"] = "15"
                        c["image"] = c15_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "15"
                    elif card == 16:
                        # Change image
                        c["text"] = "16"
                        c["image"] = c16_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "16"
                    elif card == 17:
                        # Change image
                        c["text"] = "17"
                        c["image"] = c17_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "17"
                    elif card == 18:
                        # Change image
                        c["text"] = "18"
                        c["image"] = c18_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "18"
                    elif card == 19:
                        # Change image
                        c["text"] = "19"
                        c["image"] = c19_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "19"
                    elif card == 20:
                        # Change image
                        c["text"] = "20"
                        c["image"] = c20_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "20"

                    # Counter for steps
                    count += 1
                
                # Start to determine correct answers
                if len(answer_list) == 3:
                    if random_cards[answer_list[0]] == random_cards[answer_list[1]] and random_cards[answer_list[0]] == random_cards[answer_list[2]] and random_cards[answer_list[1]] == random_cards[answer_list[2]]:
                        # Attempt counter
                        attempts += 1
                        attempts_label.config(text="Attempts: " + str(attempts) + "     |")
                        # Status label
                        status_label.config(text="  Match!")
                        # Disabling button if correct answer
                        for key in answer_dict:
                            key["state"] = "disabled"
                        # Reseting temp
                        count = 0
                        answer_list = []
                        answer_dict = {}
                        # Counting correct answers
                        correct += 1
                    else:
                        # Attempt counter
                        attempts += 1
                        attempts_label.config(text="Attempts: " + str(attempts) + "     |")
                        # Status label
                        status_label.config(text="  Incorrect!")
                        # Reseting temp
                        count = 0
                        answer_list = []

                        # Waittime after incorrect answer
                        def waithere():
                            var = IntVar()
                            screen.after(10, var.set, 1)
                            screen.wait_variable(var)
                        waithere()
                        time.sleep(1)

                        # Reset the buttons
                        for key in answer_dict:
                            key["text"] = ""
                            key["image"] = inverted_tiles_img

                        # Reseting temp
                        answer_dict = {}
                if correct == 20:
                    # Status win
                    status_label.config(text="Win!", font=("Helvetica", 48))

                    # Pause after winning the game
                    def waithere():
                        var = IntVar()
                        screen.after(500, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    time.sleep(2.5)

                    # Returing back to level menu
                    level_top.destroy()
                    lvl_top.destroy()
                    lvl.destroy()
                    lvl_bottom.destroy()
                    
                    start()

            # Level logo
            level_label = Label(level_top, image = level08_img, width= 130, height=130)
            timer_label = Label(level_top, text = str(timer08[0]) + ":" + str(timer08[1]), font=("Helvetica", 32))

            level_label.grid(row = 0, column = 0)
            timer_label.grid(row = 0, column = 1)

            # Playcards
            card0 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card0, random_cards[0], 0))
            card1 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card1, random_cards[1], 1))
            card2 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card2, random_cards[2], 2))
            card3 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card3, random_cards[3], 3))
            card4 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card4, random_cards[4], 4))
            card5 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card5, random_cards[5], 5))
            card6 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card6, random_cards[6], 6))
            card7 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card7, random_cards[7], 7))
            card8 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card8, random_cards[8], 8))
            card9 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card9, random_cards[9], 9))
            card10 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card10, random_cards[10], 10))
            card11 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card11, random_cards[11], 11))
            card12 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card12, random_cards[12], 12))
            card13 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card13, random_cards[13], 13))
            card14 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card14, random_cards[14], 14))
            card15 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card15, random_cards[15], 15))
            card16 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card16, random_cards[16], 16))
            card17 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card17, random_cards[17], 17))
            card18 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card18, random_cards[18], 18))
            card19 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card19, random_cards[19], 19))
            card20 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card20, random_cards[20], 20))
            card21 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card21, random_cards[21], 21))
            card22 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card22, random_cards[22], 22))
            card23 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card23, random_cards[23], 23))
            card24 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card24, random_cards[24], 24))
            card25 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card25, random_cards[25], 25))
            card26 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card26, random_cards[26], 26))
            card27 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card27, random_cards[27], 27))
            card28 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card28, random_cards[28], 28))
            card29 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card29, random_cards[29], 29))
            card30 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card30, random_cards[30], 30))
            card31 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card31, random_cards[31], 31))
            card32 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card32, random_cards[32], 32))
            card33 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card33, random_cards[33], 33))
            card34 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card34, random_cards[34], 34))
            card35 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card35, random_cards[35], 35))
            card36 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card36, random_cards[36], 36))
            card37 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card37, random_cards[37], 37))
            card38 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card38, random_cards[38], 38))
            card39 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card39, random_cards[39], 39))
            card40 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card40, random_cards[40], 40))
            card41 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card41, random_cards[41], 41))
            card42 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card42, random_cards[42], 42))
            card43 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card43, random_cards[43], 43))
            card44 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card44, random_cards[44], 44))
            card45 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card45, random_cards[45], 45))
            card46 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card46, random_cards[46], 46))
            card47 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card47, random_cards[47], 47))
            card48 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card48, random_cards[48], 48))
            card49 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card49, random_cards[49], 49))
            card50 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card50, random_cards[50], 50))
            card51 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card51, random_cards[51], 51))
            card52 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card52, random_cards[52], 52))
            card53 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card53, random_cards[53], 53))
            card54 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card54, random_cards[54], 54))
            card55 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card55, random_cards[55], 55))
            card56 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card56, random_cards[56], 56))
            card57 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card57, random_cards[57], 57))
            card58 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card58, random_cards[58], 58))
            card59 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card59, random_cards[59], 59))

            # Griding playcards
            card0.grid(row = 0, column = 0)
            card1.grid(row = 0, column = 1)
            card2.grid(row = 0, column = 2)
            card3.grid(row = 0, column = 3)
            card4.grid(row = 0, column = 4)
            card5.grid(row = 0, column = 5)
            card6.grid(row = 0, column = 6)
            card7.grid(row = 0, column = 7)
            card8.grid(row = 0, column = 8)
            card9.grid(row = 0, column = 9)
            card10.grid(row = 1, column = 0)
            card11.grid(row = 1, column = 1)
            card12.grid(row = 1, column = 2)
            card13.grid(row = 1, column = 3)
            card14.grid(row = 1, column = 4)
            card15.grid(row = 1, column = 5)
            card16.grid(row = 1, column = 6)
            card17.grid(row = 1, column = 7)
            card18.grid(row = 1, column = 8)
            card19.grid(row = 1, column = 9)
            card20.grid(row = 2, column = 0)
            card21.grid(row = 2, column = 1)
            card22.grid(row = 2, column = 2)
            card23.grid(row = 2, column = 3)
            card24.grid(row = 2, column = 4)
            card25.grid(row = 2, column = 5)
            card26.grid(row = 2, column = 6)
            card27.grid(row = 2, column = 7)
            card28.grid(row = 2, column = 8)
            card29.grid(row = 2, column = 9)
            card30.grid(row = 3, column = 0)
            card31.grid(row = 3, column = 1)
            card32.grid(row = 3, column = 2)
            card33.grid(row = 3, column = 3)
            card34.grid(row = 3, column = 4)
            card35.grid(row = 3, column = 5)
            card36.grid(row = 3, column = 6)
            card37.grid(row = 3, column = 7)
            card38.grid(row = 3, column = 8)
            card39.grid(row = 3, column = 9)
            card40.grid(row = 4, column = 0)
            card41.grid(row = 4, column = 1)
            card42.grid(row = 4, column = 2)
            card43.grid(row = 4, column = 3)
            card44.grid(row = 4, column = 4)
            card45.grid(row = 4, column = 5)
            card46.grid(row = 4, column = 6)
            card47.grid(row = 4, column = 7)
            card48.grid(row = 4, column = 8)
            card49.grid(row = 4, column = 9)
            card50.grid(row = 5, column = 0)
            card51.grid(row = 5, column = 1)
            card52.grid(row = 5, column = 2)
            card53.grid(row = 5, column = 3)
            card54.grid(row = 5, column = 4)
            card55.grid(row = 5, column = 5)
            card56.grid(row = 5, column = 6)
            card57.grid(row = 5, column = 7)
            card58.grid(row = 5, column = 8)
            card59.grid(row = 5, column = 9)

            cards = [card0, card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15,
                    card16, card17, card18, card19, card20, card21, card22, card23, card24, card25, card26, card27, card28, card29,
                    card30, card31, card32, card33, card34, card35, card36, card37, card38, card39,
                    card40, card41, card42, card43, card44, card45, card46, card47, card48, card49,
                    card50, card51, card52, card53, card54, card55, card56, card57, card58, card59]

            # Show cards
            i = 0
            for item in cards:
                show_cards(item, random_cards[i], i)
                i += 1
            
            # Wait for few seconds
            def waithere():
                var = IntVar()
                screen.after(500, var.set, 1)
                screen.wait_variable(var)
            waithere()

            settingsload = open(pathname+"\settings.txt", "r")
            settings = settingsload.read()
            i = 0
            for x in settings:
                i = 1 + i
                if i > 29:
                    displaytimeload.append(x)
            settingsload.close()

            if displaytimeload[0] == "1":
                time.sleep(2.5)
            elif displaytimeload[0] == "2":
                time.sleep(1)
            elif displaytimeload[0] == "2":
                time.sleep(0.5)

            # Hide cards
            card0.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card1.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card2.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card3.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card4.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card5.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card6.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card7.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card8.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card9.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card10.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card11.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card12.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card13.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card14.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card15.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card16.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card17.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card18.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card19.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card20.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card21.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card22.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card23.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card24.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card25.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card26.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card27.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card28.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card29.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            card30.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card31.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card32.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card33.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card34.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card35.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card36.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card37.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card38.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card39.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            card40.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card41.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card42.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card43.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card44.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card45.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card46.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card47.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card48.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card49.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            card50.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card51.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card52.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card53.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card54.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card55.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card56.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card57.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card58.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card59.config(image = inverted_tiles_img)  

            # Status label
            status_label = Label(level_top, text="Game Started!")
            attempts_label = Label(level_top, text="Attempts: " + str(attempts) + "     |")

            attempts_label.grid(row = 1, column = 0)
            status_label.grid(row = 1, column = 1)

            # Countdown timer
            def clock():
                global timer08, sec
                timer08[1] -= 1

                # Losing game after countdown is finished
                if timer08[1] == -1 and timer08[0] != 0:
                    timer08[0] -= 1
                    timer08[1] += 60

                timer_label.config(text = str(timer08[0]) + ":" + str(timer08[1]))

                if timer08[0] == 0 and timer08[1] == 0:
                    # Status label
                    status_label.config(text="Lose! Try Again!", font=("Helvetica", 48))

                    # Pause after losing game
                    def waithere():
                        var = IntVar()
                        screen.after(500, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    time.sleep(2.5)

                    # Returning back to level menu
                    level_top.destroy()
                    lvl_top.destroy()
                    lvl.destroy()
                    lvl_bottom.destroy()

                    start() 

                timer_label.after(1000, clock)

            clock()

        # Lvl 08 end

        #
        #
        #
        #
        # 2v2
        def twoVtwo():
            top1.destroy()
            top2.destroy()
            twovtwo_btn.destroy()
            back_btn.destroy()

            # Images
            inverted_tiles_img = Image.open(pathname+r"\img\content\inverted_tiles.png")
            inverted_tiles_img = inverted_tiles_img.resize((128, 128), Image.ANTIALIAS)
            inverted_tiles_img = ImageTk.PhotoImage(inverted_tiles_img)
            inverted_tiles = Label(image=inverted_tiles_img)
            inverted_tiles.image = inverted_tiles_img

            c01_img = Image.open(pathname+r"\img\content\19.png")
            c01_img = c01_img.resize((128, 128), Image.ANTIALIAS)
            c01_img = ImageTk.PhotoImage(c01_img)
            c01 = Label(image=c01_img)
            c01.image = c01_img

            c02_img = Image.open(pathname+r"\img\content\20.png")
            c02_img = c02_img.resize((128, 128), Image.ANTIALIAS)
            c02_img = ImageTk.PhotoImage(c02_img)
            c02 = Label(image=c02_img)
            c02.image = c02_img

            c03_img = Image.open(pathname+r"\img\content\21.png")
            c03_img = c03_img.resize((128, 128), Image.ANTIALIAS)
            c03_img = ImageTk.PhotoImage(c03_img)
            c03 = Label(image=c03_img)
            c03.image = c03_img

            c04_img = Image.open(pathname+r"\img\content\22.png")
            c04_img = c04_img.resize((128, 128), Image.ANTIALIAS)
            c04_img = ImageTk.PhotoImage(c04_img)
            c04 = Label(image=c04_img)
            c04.image = c04_img

            c05_img = Image.open(pathname+r"\img\content\23.png")
            c05_img = c05_img.resize((128, 128), Image.ANTIALIAS)
            c05_img = ImageTk.PhotoImage(c05_img)
            c05 = Label(image=c05_img)
            c05.image = c05_img

            c06_img = Image.open(pathname+r"\img\content\24.png")
            c06_img = c06_img.resize((128, 128), Image.ANTIALIAS)
            c06_img = ImageTk.PhotoImage(c06_img)
            c06 = Label(image=c06_img)
            c06.image = c06_img

            c07_img = Image.open(pathname+r"\img\content\25.png")
            c07_img = c07_img.resize((128, 128), Image.ANTIALIAS)
            c07_img = ImageTk.PhotoImage(c07_img)
            c07 = Label(image=c07_img)
            c07.image = c07_img

            c08_img = Image.open(pathname+r"\img\content\26.png")
            c08_img = c08_img.resize((128, 128), Image.ANTIALIAS)
            c08_img = ImageTk.PhotoImage(c08_img)
            c08 = Label(image=c08_img)
            c08.image = c08_img

            c09_img = Image.open(pathname+r"\img\content\27.png")
            c09_img = c09_img.resize((128, 128), Image.ANTIALIAS)
            c09_img = ImageTk.PhotoImage(c09_img)
            c09 = Label(image=c09_img)
            c09.image = c09_img

            c10_img = Image.open(pathname+r"\img\content\28.png")
            c10_img = c10_img.resize((128, 128), Image.ANTIALIAS)
            c10_img = ImageTk.PhotoImage(c10_img)
            c10 = Label(image=c10_img)
            c10.image = c10_img

            c11_img = Image.open(pathname+r"\img\content\29.png")
            c11_img = c11_img.resize((128, 128), Image.ANTIALIAS)
            c11_img = ImageTk.PhotoImage(c11_img)
            c11 = Label(image=c11_img)
            c11.image = c11_img

            c12_img = Image.open(pathname+r"\img\content\30.png")
            c12_img = c12_img.resize((128, 128), Image.ANTIALIAS)
            c12_img = ImageTk.PhotoImage(c12_img)
            c12 = Label(image=c12_img)
            c12.image = c12_img

            c13_img = Image.open(pathname+r"\img\content\31.png")
            c13_img = c13_img.resize((128, 128), Image.ANTIALIAS)
            c13_img = ImageTk.PhotoImage(c13_img)
            c13 = Label(image=c13_img)
            c13.image = c13_img

            c14_img = Image.open(pathname+r"\img\content\32.png")
            c14_img = c14_img.resize((128, 128), Image.ANTIALIAS)
            c14_img = ImageTk.PhotoImage(c14_img)
            c14 = Label(image=c14_img)
            c14.image = c14_img

            c15_img = Image.open(pathname+r"\img\content\33.png")
            c15_img = c15_img.resize((128, 128), Image.ANTIALIAS)
            c15_img = ImageTk.PhotoImage(c15_img)
            c15 = Label(image=c15_img)
            c15.image = c15_img

            c16_img = Image.open(pathname+r"\img\content\34.png")
            c16_img = c16_img.resize((128, 128), Image.ANTIALIAS)
            c16_img = ImageTk.PhotoImage(c16_img)
            c16 = Label(image=c16_img)
            c16.image = c16_img

            c17_img = Image.open(pathname+r"\img\content\35.png")
            c17_img = c17_img.resize((128, 128), Image.ANTIALIAS)
            c17_img = ImageTk.PhotoImage(c17_img)
            c17 = Label(image=c17_img)
            c17.image = c17_img

            c18_img = Image.open(pathname+r"\img\content\36.png")
            c18_img = c18_img.resize((128, 128), Image.ANTIALIAS)
            c18_img = ImageTk.PhotoImage(c18_img)
            c18 = Label(image=c18_img)
            c18.image = c18_img

            c19_img = Image.open(pathname+r"\img\content\37.png")
            c19_img = c19_img.resize((128, 128), Image.ANTIALIAS)
            c19_img = ImageTk.PhotoImage(c19_img)
            c19 = Label(image=c19_img)
            c19.image = c19_img

            c20_img = Image.open(pathname+r"\img\content\38.png")
            c20_img = c20_img.resize((128, 128), Image.ANTIALIAS)
            c20_img = ImageTk.PhotoImage(c20_img)
            c20 = Label(image=c20_img)
            c20.image = c20_img

            # Random cards
            random_cards = [1,1,2,2,3,3,4,4,5,5,6,6,7,7,8,8,9,9,10,10,11,11,12,12,13,13,14,14,15,15,16,16,17,17,18,18,19,19,20,20]
            random.shuffle(random_cards)

            # Frames
            level_top = Frame(screen)
            level_top.pack(pady = 20, side=TOP)

            lvl_top = Frame(screen)
            lvl_top.pack(pady = 20, side=TOP)

            lvl = Frame(screen)
            lvl.pack(pady = 20, side = TOP)

            lvl_bottom = Frame(screen)
            lvl_bottom.pack(side=BOTTOM)

            # Show cards
            def show_cards(c, card, number):
                if c["text"] == "":
                    def waithere():
                        var = IntVar()
                        screen.after(100, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    # Show images
                    if card == 1:
                        c["image"] = c01_img
                    elif card == 2:
                        c["image"] = c02_img
                    elif card == 3:
                        c["image"] = c03_img
                    elif card == 4:
                        c["image"] = c04_img
                    elif card == 5:
                        c["image"] = c05_img
                    elif card == 6:
                        c["image"] = c06_img
                    elif card == 7:
                        c["image"] = c07_img
                    elif card == 8:
                        c["image"] = c08_img
                    elif card == 9:
                        c["image"] = c09_img
                    elif card == 10:
                        c["image"] = c10_img
                    elif card == 11:
                        c["image"] = c11_img
                    elif card == 12:
                        c["image"] = c12_img
                    elif card == 13:
                        c["image"] = c13_img
                    elif card == 14:
                        c["image"] = c14_img
                    elif card == 15:
                        c["image"] = c15_img
                    elif card == 16:
                        c["image"] = c16_img
                    elif card == 17:
                        c["image"] = c17_img
                    elif card == 18:
                        c["image"] = c18_img
                    elif card == 19:
                        c["image"] = c19_img
                    elif card == 20:
                        c["image"] = c20_img
                

            #Functions for clicking buttons
            def button_click(c, card, number):
                global count1, count2, turn, correct1, correct2, answer_list, answer_dict, attempts, correct
                # Player 1
                if c["text"] == "" and count1 < 2 and turn == "player1":
                    if card == 1:
                        # Change image
                        c["text"] = "1"
                        c["image"] = c01_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "1"
                    elif card == 2:
                        # Change image
                        c["text"] = "2"
                        c["image"] = c02_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "2"
                    elif card == 3:
                        # Change image
                        c["text"] = "3"
                        c["image"] = c03_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "3"
                    elif card == 4:
                        # Change image
                        c["text"] = "4"
                        c["image"] = c04_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "4"
                    elif card == 5:
                        # Change image
                        c["text"] = "5"
                        c["image"] = c05_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "5"
                    elif card == 6:
                        # Change image
                        c["text"] = "6"
                        c["image"] = c06_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "6"
                    elif card == 7:
                        # Change image
                        c["text"] = "7"
                        c["image"] = c07_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "7"
                    elif card == 8:
                        # Change image
                        c["text"] = "8"
                        c["image"] = c08_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "8"
                    elif card == 9:
                        # Change image
                        c["text"] = "9"
                        c["image"] = c09_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "9"
                    elif card == 10:
                        # Change image
                        c["text"] = "10"
                        c["image"] = c10_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "10"
                    elif card == 11:
                        # Change image
                        c["text"] = "11"
                        c["image"] = c11_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "11"
                    elif card == 12:
                        # Change image
                        c["text"] = "12"
                        c["image"] = c12_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "12"
                    elif card == 13:
                        # Change image
                        c["text"] = "13"
                        c["image"] = c13_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "13"
                    elif card == 14:
                        # Change image
                        c["text"] = "14"
                        c["image"] = c14_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "14"
                    elif card == 15:
                        # Change image
                        c["text"] = "15"
                        c["image"] = c15_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "15"
                    elif card == 16:
                        # Change image
                        c["text"] = "16"
                        c["image"] = c16_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "16"
                    elif card == 17:
                        # Change image
                        c["text"] = "17"
                        c["image"] = c17_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "17"
                    elif card == 18:
                        # Change image
                        c["text"] = "18"
                        c["image"] = c18_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "18"
                    elif card == 19:
                        # Change image
                        c["text"] = "19"
                        c["image"] = c19_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "19"
                    elif card == 20:
                        # Change image
                        c["text"] = "20"
                        c["image"] = c20_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "20"

                    # Counter for steps
                    count1 += 1

                # Player 2
                elif c["text"] == "" and count2 < 2 and turn == "player2":
                    if card == 1:
                        # Change image
                        c["text"] = "1"
                        c["image"] = c01_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "1"
                    elif card == 2:
                        # Change image
                        c["text"] = "2"
                        c["image"] = c02_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "2"
                    elif card == 3:
                        # Change image
                        c["text"] = "3"
                        c["image"] = c03_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "3"
                    elif card == 4:
                        # Change image
                        c["text"] = "4"
                        c["image"] = c04_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "4"
                    elif card == 5:
                        # Change image
                        c["text"] = "5"
                        c["image"] = c05_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "5"
                    elif card == 6:
                        # Change image
                        c["text"] = "6"
                        c["image"] = c06_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "6"
                    elif card == 7:
                        # Change image
                        c["text"] = "7"
                        c["image"] = c07_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "7"
                    elif card == 8:
                        # Change image
                        c["text"] = "8"
                        c["image"] = c08_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "8"
                    elif card == 9:
                        # Change image
                        c["text"] = "9"
                        c["image"] = c09_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "9"
                    elif card == 10:
                        # Change image
                        c["text"] = "10"
                        c["image"] = c10_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "10"
                    elif card == 11:
                        # Change image
                        c["text"] = "11"
                        c["image"] = c11_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "11"
                    elif card == 12:
                        # Change image
                        c["text"] = "12"
                        c["image"] = c12_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "12"
                    elif card == 13:
                        # Change image
                        c["text"] = "13"
                        c["image"] = c13_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "13"
                    elif card == 14:
                        # Change image
                        c["text"] = "14"
                        c["image"] = c14_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "14"
                    elif card == 15:
                        # Change image
                        c["text"] = "15"
                        c["image"] = c15_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "15"
                    elif card == 16:
                        # Change image
                        c["text"] = "16"
                        c["image"] = c16_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "16"
                    elif card == 17:
                        # Change image
                        c["text"] = "17"
                        c["image"] = c17_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "17"
                    elif card == 18:
                        # Change image
                        c["text"] = "18"
                        c["image"] = c18_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "18"
                    elif card == 19:
                        # Change image
                        c["text"] = "19"
                        c["image"] = c19_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "19"
                    elif card == 20:
                        # Change image
                        c["text"] = "20"
                        c["image"] = c20_img
                        # Add number to answer list
                        answer_list.append(number)
                        # Add button and number to answer dictionary
                        answer_dict[c] = "20"

                    # Counter for steps
                    count2 += 1
                
                # Start to determine correct answers

                # Player 1
                if len(answer_list) == 2 and turn == "player1":
                    if random_cards[answer_list[0]] == random_cards[answer_list[1]]:
                        # Attempt counter
                        attempts += 1
                        attempts1_label.config(text="Player 1 attempts: " + str(attempts))
                        
                        correct1 += 1
                        correct1_label.config(text="Player 1 correct: " + str(correct1))
                        # Status label
                        status_label.config(text="  Player 1: match!")
                        # Disabling button if correct answer
                        for key in answer_dict:
                            key["state"] = "disabled"
                        # Reseting temp
                        count1 = 0
                        answer_list = []
                        answer_dict = {}
                        # Counting correct answers
                        correct += 1
                    else:
                        # Attempt counter
                        attempts += 1
                        attempts1_label.config(text="Player 1 attempts: " + str(attempts))
                        # Status label
                        status_label.config(text="  Player 2 turn")
                        # Reseting temp
                        count1 = 0
                        answer_list = []

                        turn = "player2"

                        # Waittime after incorrect answer
                        def waithere():
                            var = IntVar()
                            screen.after(10, var.set, 1)
                            screen.wait_variable(var)
                        waithere()
                        time.sleep(1)

                        # Reset the buttons
                        for key in answer_dict:
                            key["text"] = ""
                            key["image"] = inverted_tiles_img

                        # Reseting temp
                        answer_dict = {}

                # Player 2
                elif len(answer_list) == 2 and turn == "player2":
                    if random_cards[answer_list[0]] == random_cards[answer_list[1]]:
                        # Attempt counter
                        attempts += 1
                        attempts2_label.config(text="Player 2 attempts: " + str(attempts))

                        correct2 += 1
                        correct2_label.config(text="Player 2 correct: " + str(correct2))
                        # Status label
                        status_label.config(text="  Player 2: match!")
                        # Disabling button if correct answer
                        for key in answer_dict:
                            key["state"] = "disabled"
                        # Reseting temp
                        count2 = 0
                        answer_list = []
                        answer_dict = {}
                        # Counting correct answers
                        correct += 1
                    else:
                        # Attempt counter
                        attempts += 1
                        attempts2_label.config(text="Player 2 attempts: " + str(attempts))
                        # Status label
                        status_label.config(text="  Player 1 turn")
                        # Reseting temp
                        count2 = 0
                        answer_list = []

                        turn = "player1"

                        # Waittime after incorrect answer
                        def waithere():
                            var = IntVar()
                            screen.after(10, var.set, 1)
                            screen.wait_variable(var)
                        waithere()
                        time.sleep(1)

                        # Reset the buttons
                        for key in answer_dict:
                            key["text"] = ""
                            key["image"] = inverted_tiles_img

                        # Reseting temp
                        answer_dict = {}

                if correct == 20:
                    # Status win
                    if correct1 > correct2:
                        status_label.config(text="Player 1 Win!", font=("Helvetica", 48))
                    elif correct1 < correct2:
                        status_label.config(text="Player 2 Win!", font=("Helvetica", 48))
                    elif correct1 == correct2:
                        status_label.config(text="Equally! Congratulations!", font=("Helvetica", 48))

                    # Pause after winning the game
                    def waithere():
                        var = IntVar()
                        screen.after(500, var.set, 1)
                        screen.wait_variable(var)
                    waithere()
                    time.sleep(2.5)

                    # Returing back to level menu
                    level_top.destroy()
                    lvl_top.destroy()
                    lvl.destroy()
                    lvl_bottom.destroy()
                    
                    start()

            # Level logo
            level_label = Label(level_top, image = twovtwo_img, width= 130, height=130)

            level_label.grid(row = 0, column = 0)

            global turn

            turn = "player1"

            # Playcards
            card0 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card0, random_cards[0], 0))
            card1 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card1, random_cards[1], 1))
            card2 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card2, random_cards[2], 2))
            card3 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card3, random_cards[3], 3))
            card4 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card4, random_cards[4], 4))
            card5 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card5, random_cards[5], 5))
            card6 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card6, random_cards[6], 6))
            card7 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card7, random_cards[7], 7))
            card8 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card8, random_cards[8], 8))
            card9 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card9, random_cards[9], 9))
            card10 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card10, random_cards[10], 10))
            card11 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card11, random_cards[11], 11))
            card12 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card12, random_cards[12], 12))
            card13 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card13, random_cards[13], 13))
            card14 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card14, random_cards[14], 14))
            card15 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card15, random_cards[15], 15))
            card16 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card16, random_cards[16], 16))
            card17 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card17, random_cards[17], 17))
            card18 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card18, random_cards[18], 18))
            card19 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card19, random_cards[19], 19))
            card20 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card20, random_cards[20], 20))
            card21 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card21, random_cards[21], 21))
            card22 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card22, random_cards[22], 22))
            card23 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card23, random_cards[23], 23))
            card24 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card24, random_cards[24], 24))
            card25 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card25, random_cards[25], 25))
            card26 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card26, random_cards[26], 26))
            card27 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card27, random_cards[27], 27))
            card28 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card28, random_cards[28], 28))
            card29 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card29, random_cards[29], 29))
            card30 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card30, random_cards[30], 30))
            card31 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card31, random_cards[31], 31))
            card32 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card32, random_cards[32], 32))
            card33 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card33, random_cards[33], 33))
            card34 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card34, random_cards[34], 34))
            card35 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card35, random_cards[35], 35))
            card36 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card36, random_cards[36], 36))
            card37 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card37, random_cards[37], 37))
            card38 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card38, random_cards[38], 38))
            card39 = Button(lvl_top, text = "", image = inverted_tiles_img, width = 130, heigh = 130, command = lambda: button_click(card39, random_cards[39], 39))

            # Griding playcards
            card0.grid(row = 0, column = 0)
            card1.grid(row = 0, column = 1)
            card2.grid(row = 0, column = 2)
            card3.grid(row = 0, column = 3)
            card4.grid(row = 0, column = 4)
            card5.grid(row = 0, column = 5)
            card6.grid(row = 0, column = 6)
            card7.grid(row = 0, column = 7)
            card8.grid(row = 0, column = 8)
            card9.grid(row = 0, column = 9)
            card10.grid(row = 1, column = 0)
            card11.grid(row = 1, column = 1)
            card12.grid(row = 1, column = 2)
            card13.grid(row = 1, column = 3)
            card14.grid(row = 1, column = 4)
            card15.grid(row = 1, column = 5)
            card16.grid(row = 1, column = 6)
            card17.grid(row = 1, column = 7)
            card18.grid(row = 1, column = 8)
            card19.grid(row = 1, column = 9)
            card20.grid(row = 2, column = 0)
            card21.grid(row = 2, column = 1)
            card22.grid(row = 2, column = 2)
            card23.grid(row = 2, column = 3)
            card24.grid(row = 2, column = 4)
            card25.grid(row = 2, column = 5)
            card26.grid(row = 2, column = 6)
            card27.grid(row = 2, column = 7)
            card28.grid(row = 2, column = 8)
            card29.grid(row = 2, column = 9)
            card30.grid(row = 3, column = 0)
            card31.grid(row = 3, column = 1)
            card32.grid(row = 3, column = 2)
            card33.grid(row = 3, column = 3)
            card34.grid(row = 3, column = 4)
            card35.grid(row = 3, column = 5)
            card36.grid(row = 3, column = 6)
            card37.grid(row = 3, column = 7)
            card38.grid(row = 3, column = 8)
            card39.grid(row = 3, column = 9)

            cards = [card0, card1, card2, card3, card4, card5, card6, card7, card8, card9, card10, card11, card12, card13, card14, card15, card16, card17, card18, card19, 
                    card20, card21, card22, card23, card24, card25, card26, card27, card28, card29, card30, card31, card32, card33, card34, card35, card36, card37, card38, card39]

            # Show cards
            i = 0
            for item in cards:
                show_cards(item, random_cards[i], i)
                i += 1
                
            # Wait for few seconds
            def waithere():
                var = IntVar()
                screen.after(500, var.set, 1)
                screen.wait_variable(var)
            waithere()

            settingsload = open(pathname+"\settings.txt", "r")
            settings = settingsload.read()
            i = 0
            for x in settings:
                i = 1 + i
                if i > 29:
                    displaytimeload.append(x)
            settingsload.close()

            if displaytimeload[0] == "1":
                time.sleep(2.5)
            elif displaytimeload[0] == "2":
                time.sleep(1)
            elif displaytimeload[0] == "2":
                time.sleep(0.5)

            # Hide cards
            card0.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card1.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card2.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card3.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card4.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card5.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
                waithere()
            card6.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card7.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card8.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card9.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card10.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card11.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card12.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card13.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card14.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card15.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
                waithere()
            card16.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card17.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card18.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card19.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card20.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card21.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card22.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card23.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card24.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card25.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
                waithere()
            card26.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card27.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card28.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card29.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card30.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card31.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card32.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card33.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card34.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card35.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
                waithere()
            card36.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card37.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card38.config(image = inverted_tiles_img)
            def waithere():
                var = IntVar()
                screen.after(100, var.set, 1)
                screen.wait_variable(var)
            waithere()
            card39.config(image = inverted_tiles_img)
                
            # Status label
            status_label = Label(lvl, text="Player 1 turn", font=("Helvetica", 32))
            attempts1_label = Label(lvl, text="Player 1 attempts: " + str(attempts))
            attempts2_label = Label(lvl, text="Player 2 attempts: " + str(attempts))

            correct1_label = Label(lvl, text="Player 1 correct: " + str(correct1))
            correct2_label = Label(lvl, text="Player 2 correct: " + str(correct2))

            correct1_label.grid(row = 0, column = 0)
            correct2_label.grid(row = 0, column = 2)
            status_label.grid(row = 1, column = 1)
            attempts1_label.grid(row = 2, column = 0)
            attempts2_label.grid(row = 2, column = 2)
            

        # 2v2 end

        start_btn.destroy()
        options_btn.destroy()
        exit_btn.destroy()
        logo.destroy()

        # Level Menu
        
        # Frames
        top1 = Frame(screen)
        top1.pack(pady = 50, side=TOP)

        top2 = Frame(screen)
        top2.pack(side=TOP)

        # Load image
        loceked_img = pathname+r"\img\levels\locked.png"

        # Loading savegame
        savegameload = open(pathname+"\savegame.txt", "r")
        savegame = savegameload.read()
        i = 0
        levelload = []
        for x in savegame:
            i = 1 + i
            if i > 8:
                levelload.append(x)
                i = -1
        savegameload.close()

        # Level menu grid
        if levelload[0] == "1":
            level01_img = Image.open(pathname+r"\img\levels\01.png")
            level01_img = level01_img.resize((128, 128), Image.ANTIALIAS)
            level01_img = ImageTk.PhotoImage(level01_img)
            level01 = Label(image=level01_img)
            level01.image = level01_img
            level01_btn = Button(top1, image = level01_img, width = 130, heigh = 130, command = lvl01)
        else: 
            level01_img = Image.open(loceked_img)
            level01_img = level01_img.resize((128, 128), Image.ANTIALIAS)
            level01_img = ImageTk.PhotoImage(level01_img)
            level01 = Label(image=level01_img)
            level01.image = level01_img
            level01_btn = Button(top1, image = level01_img, width = 130, heigh = 130)

        if levelload[1] == "1":
            level02_img = Image.open(pathname+r"\img\levels\02.png")
            level02_img = level02_img.resize((128, 128), Image.ANTIALIAS)
            level02_img = ImageTk.PhotoImage(level02_img)
            level02 = Label(image=level02_img)
            level02.image = level02_img
            level02_btn = Button(top1, image = level02_img, width = 130, heigh = 130, command = lvl02)
        else: 
            level02_img = Image.open(loceked_img)
            level02_img = level02_img.resize((128, 128), Image.ANTIALIAS)
            level02_img = ImageTk.PhotoImage(level02_img)
            level02 = Label(image=level02_img)
            level02.image = level02_img
            level02_btn = Button(top1, image = level02_img, width = 130, heigh = 130)

        if levelload[2] == "1":
            level03_img = Image.open(pathname+r"\img\levels\03.png")
            level03_img = level03_img.resize((128, 128), Image.ANTIALIAS)
            level03_img = ImageTk.PhotoImage(level03_img)
            level03 = Label(image=level03_img)
            level03.image = level03_img
            level03_btn = Button(top1, image = level03_img, width = 130, heigh = 130, command = lvl03)
        else: 
            level03_img = Image.open(loceked_img)
            level03_img = level03_img.resize((128, 128), Image.ANTIALIAS)
            level03_img = ImageTk.PhotoImage(level03_img)
            level03 = Label(image=level03_img)
            level03.image = level03_img
            level03_btn = Button(top1, image = level03_img, width = 130, heigh = 130)

        if levelload[3] == "1":
            level04_img = Image.open(pathname+r"\img\levels\04.png")
            level04_img = level04_img.resize((128, 128), Image.ANTIALIAS)
            level04_img = ImageTk.PhotoImage(level04_img)
            level04 = Label(image=level04_img)
            level04.image = level04_img
            level04_btn = Button(top1, image = level04_img, width = 130, heigh = 130, command = lvl04)
        else: 
            level04_img = Image.open(loceked_img)
            level04_img = level04_img.resize((128, 128), Image.ANTIALIAS)
            level04_img = ImageTk.PhotoImage(level04_img)
            level04 = Label(image=level04_img)
            level04.image = level04_img
            level04_btn = Button(top1, image = level04_img, width = 130, heigh = 130)

        if levelload[4] == "1":
            level05_img = Image.open(pathname+r"\img\levels\05.png")
            level05_img = level05_img.resize((128, 128), Image.ANTIALIAS)
            level05_img = ImageTk.PhotoImage(level05_img)
            level05 = Label(image=level05_img)
            level05.image = level05_img
            level05_btn = Button(top1, image = level05_img, width = 130, heigh = 130, command = lvl05)
        else: 
            level05_img = Image.open(loceked_img)
            level05_img = level05_img.resize((128, 128), Image.ANTIALIAS)
            level05_img = ImageTk.PhotoImage(level05_img)
            level05 = Label(image=level05_img)
            level05.image = level05_img
            level05_btn = Button(top1, image = level05_img, width = 130, heigh = 130)

        if levelload[5] == "1":
            level06_img = Image.open(pathname+r"\img\levels\06.png")
            level06_img = level06_img.resize((128, 128), Image.ANTIALIAS)
            level06_img = ImageTk.PhotoImage(level06_img)
            level06 = Label(image=level06_img)
            level06.image = level06_img
            level06_btn = Button(top1, image = level06_img, width = 130, heigh = 130, command = lvl06)
        else: 
            level06_img = Image.open(loceked_img)
            level06_img = level06_img.resize((128, 128), Image.ANTIALIAS)
            level06_img = ImageTk.PhotoImage(level06_img)
            level06 = Label(image=level06_img)
            level06.image = level06_img
            level06_btn = Button(top1, image = level06_img, width = 130, heigh = 130)

        if levelload[6] == "1":
            level07_img = Image.open(pathname+r"\img\levels\07.png")
            level07_img = level07_img.resize((128, 128), Image.ANTIALIAS)
            level07_img = ImageTk.PhotoImage(level07_img)
            level07 = Label(image=level07_img)
            level07.image = level07_img
            level07_btn = Button(top1, image = level07_img, width = 130, heigh = 130, command = lvl07)
        else: 
            level07_img = Image.open(loceked_img)
            level07_img = level07_img.resize((128, 128), Image.ANTIALIAS)
            level07_img = ImageTk.PhotoImage(level07_img)
            level07 = Label(image=level07_img)
            level07.image = level07_img
            level07_btn = Button(top1, image = level07_img, width = 130, heigh = 130)

        if levelload[7] == "1":
            level08_img = Image.open(pathname+r"\img\levels\08.png")
            level08_img = level08_img.resize((128, 128), Image.ANTIALIAS)
            level08_img = ImageTk.PhotoImage(level08_img)
            level08 = Label(image=level08_img)
            level08.image = level08_img
            level08_btn = Button(top1, image = level08_img, width = 130, heigh = 130, command = lvl08)
        else: 
            level08_img = Image.open(loceked_img)
            level08_img = level08_img.resize((128, 128), Image.ANTIALIAS)
            level08_img = ImageTk.PhotoImage(level08_img)
            level08 = Label(image=level08_img)
            level08.image = level08_img
            level08_btn = Button(top1, image = level08_img, width = 130, heigh = 130)
        
        level01_btn.grid(row = 0, column = 0)
        level02_btn.grid(row = 0, column = 1)
        level03_btn.grid(row = 0, column = 2)
        level04_btn.grid(row = 0, column = 3)
        level05_btn.grid(row = 1, column = 0)
        level06_btn.grid(row = 1, column = 1)
        level07_btn.grid(row = 1, column = 2)
        level08_btn.grid(row = 1, column = 3)

        def back_button():
            top1.destroy()
            top2.destroy()
            twovtwo_btn.destroy()
            back_btn.destroy()

            main()
        
        # 2v2 button
        twovtwo_img = Image.open(pathname+r"\img\levels\twovtwo.png")
        twovtwo_img = twovtwo_img.resize((128, 128), Image.ANTIALIAS)
        twovtwo_img = ImageTk.PhotoImage(twovtwo_img)
        twovtwo = Label(image=twovtwo_img)
        twovtwo.image = twovtwo_img
        twovtwo_btn = Button(screen, image = twovtwo_img, width = 150, heigh = 150, command = twoVtwo)
        twovtwo_btn.pack(pady = 0)

        # Back to main screen button
        back_img = Image.open(pathname+r"\img\menu\back_main.png")
        back_img = back_img.resize((32, 32), Image.ANTIALIAS)
        back_img = ImageTk.PhotoImage(back_img)
        back = Label(image=back_img)
        back.image = back_img
        back_btn = Button(screen, text = "     Back", image = back_img, compound = "left", width = 200, heigh = 75, command = back_button)
        back_btn.pack(pady = 30)

    # After cliking options
    def options():
        logo.destroy()
        start_btn.destroy()
        options_btn.destroy()
        exit_btn.destroy()

        # Frame
        top1 = Frame(screen)
        top1.pack(pady = 50, side=TOP)

        # Difficult text
        difficulty_text = Label(top1, text = "Difficulty", font=("Helvetica", 25))
        difficulty_text.pack(pady=20)

        # Load settings
        settingsload = open(pathname+"\settings.txt", "r")
        settings = settingsload.read()
        i = 0
        for x in settings:
            i = 1 + i
            if i > 13:
                difficultyload.append(x)
        settingsload.close()

        # Change game difficulty
        def change_difficulty(name, load):
            global difficultyload
            if load == "1":
                name["text"] = "Normal"
                difficultyload[0] = "2"
                # Save user settings
                with open(pathname+"\settings.txt", "r") as file:
                    settings = file.read()
                    settings = settings.replace("difficulty = 1", "difficulty = 2")
                with open(pathname+"\settings.txt", "w") as file:
                    file.write(settings)

            elif load == "3":
                name["text"] = "Easy"
                difficultyload[0] = "1"
                # Save user settings
                with open(pathname+"\settings.txt", "r") as file:
                    settings = file.read()
                    settings = settings.replace("difficulty = 3", "difficulty = 1")
                with open(pathname+"\settings.txt", "w") as file:
                    file.write(settings)

            elif load == "2":
                name["text"] = "Hard"
                difficultyload[0] = "3"
                # Save user settings
                with open(pathname+"\settings.txt", "r") as file:
                    settings = file.read()
                    settings = settings.replace("difficulty = 2", "difficulty = 3")
                with open(pathname+"\settings.txt", "w") as file:
                    file.write(settings)

        # Difficulty button
        difficulty = Button(screen, text = "", width = 20, heigh = 8, command = lambda: change_difficulty(difficulty, difficultyload[0]))
        difficulty.pack(pady=20)

        if difficultyload[0] == "1":
            difficulty.config(text = "Easy")
        elif difficultyload[0] == "2":
            difficulty.config(text = "Normal")
        elif difficultyload[0] == "3":
            difficulty.config(text = "Hard")
        
        # Card Display time text
        displaytime_text = Label(screen, text = "Card Display time", font=("Helvetica", 25))
        displaytime_text.pack(pady=20)

        # Load settings
        settingsload = open(pathname+"\settings.txt", "r")
        settings = settingsload.read()
        i = 0
        for x in settings:
            i = 1 + i
            if i > 29:
                displaytimeload.append(x)
        settingsload.close()

        # Change card display time
        def change_displaytime(name, load):
            global displaytimeload
            if load == "1":
                name["text"] = "Normal"
                displaytimeload[0] = "2"
                # Save user settings
                with open(pathname+"\settings.txt", "r") as file:
                    settings = file.read()
                    settings = settings.replace("displaytime = 1", "displaytime = 2")

                with open(pathname+"\settings.txt", "w") as file:
                    file.write(settings)
            elif load == "3":
                name["text"] = "Slow"
                displaytimeload[0] = "1"
                # Save user settings
                with open(pathname+"\settings.txt", "r") as file:
                    settings = file.read()
                    settings = settings.replace("displaytime = 3", "displaytime = 1")

                with open(pathname+"\settings.txt", "w") as file:
                    file.write(settings)
            elif load == "2":
                name["text"] = "Fast"
                displaytimeload[0] = "3"
                # Save user settings
                with open(pathname+"\settings.txt", "r") as file:
                    settings = file.read()
                    settings = settings.replace("displaytime = 2", "displaytime = 3")

                with open(pathname+"\settings.txt", "w") as file:
                    file.write(settings)

        # Display time button
        displaytime = Button(screen, text = "", width = 20, heigh = 8, command = lambda: change_displaytime(displaytime, displaytimeload[0]))
        displaytime.pack(pady=20)

        if displaytimeload[0] == "1":
            displaytime.config(text = "Slow")
        elif displaytimeload[0] == "2":
            displaytime.config(text = "Normal")
        elif displaytimeload[0] == "3":
            displaytime.config(text = "Fast")

        # Return to main screen
        def back_button():
            top1.destroy()
            difficulty.destroy()
            displaytime_text.destroy()
            displaytime.destroy()
            back_btn.destroy()

            main()
        
        # Back to main screen button
        back_img = Image.open(pathname+r"\img\menu\back_main.png")
        back_img = back_img.resize((32, 32), Image.ANTIALIAS)
        back_img = ImageTk.PhotoImage(back_img)
        back = Label(image=back_img)
        back.image = back_img
        back_btn = Button(screen, text = "     Back", image = back_img, compound = "left", width = 200, heigh = 75, command = back_button)
        back_btn.pack(pady = 30)

    # Main screen buttons

    # Game logo
    logo_img = Image.open(pathname+"\img\menu\logo_main.png")
    logo_img = logo_img.resize((480, 270), Image.ANTIALIAS)
    logo_img = ImageTk.PhotoImage(logo_img)
    logo = Label(image=logo_img)
    logo.image = logo_img
    logo.pack(pady = 30)

    # Play button
    play_img = Image.open(pathname+"\img\menu\play_main.png")
    play_img = play_img.resize((32, 32), Image.ANTIALIAS)
    play_img = ImageTk.PhotoImage(play_img)
    play = Label(image=play_img)
    play.image = play_img
    start_btn = Button(screen, text = "     Start Memory Card Game", image = play_img, compound = "left", width = 200, heigh = 75, command = start)
    start_btn.pack(pady = 30)

    # Options button
    options_img = Image.open(pathname+"\img\menu\options_main.png")
    options_img = options_img.resize((32, 32), Image.ANTIALIAS)
    options_img = ImageTk.PhotoImage(options_img)
    options_ = Label(image=options_img)
    options_.image = options_img
    options_btn = Button(screen, text = "             Options                      ", image = options_img, compound = "left", width = 200, heigh = 75, command = options)
    options_btn.pack(pady = 30)

    # Exit button
    exit_img = Image.open(pathname+"\img\menu\exit_main.png")
    exit_img = exit_img.resize((32, 32), Image.ANTIALIAS)
    exit_img = ImageTk.PhotoImage(exit_img)
    exit = Label(image=exit_img)
    exit.image = exit_img
    exit_btn = Button(screen, text = "                 Exit                          ", image = exit_img, compound = "left", width = 200, heigh = 75, command = screen.destroy)
    exit_btn.pack(pady = 30)

    screen.columnconfigure(0, weight=1)
    screen.rowconfigure(1, weight=1)



# Calling main function

main()

screen.mainloop()

