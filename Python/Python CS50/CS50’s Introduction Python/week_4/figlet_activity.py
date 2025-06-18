from pyfiglet import Figlet
import random
import sys

def main():
    figlet = Figlet()   # call figlet function
    assigned_font = ask_font()  #ask for font
    text = input("Input: ")     # ask for text
    figlet.setFont(font = assigned_font)    #assigned font
    print(figlet.renderText(text))  #print text with the font

def ask_font():
    inputted_font = input("Font: ")
    figlet = Figlet()
    list_font = figlet.getFonts()

    if inputted_font == "":
        # if "" = random font
        assigned_font = random.choice(list_font)
    else:
        # if not then font should be in the list before returning it
        for font in list_font:
            if inputted_font == font:
                assigned_font = inputted_font
                break
        else:
            sys.exit("Invalid Usage")
    return assigned_font

main()









"""To call figlet function"""
# figlet = Figlet()

"""To get the list of the fonts"""
# figlet.getFonts()

"""To set font"""
# figlet.setFont(font=f)

"""To output text with the font"""
# print(figlet.renderText(s))

