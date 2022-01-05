#coding:utf-8

from libs.display import consoleOutput

def mainMenu():
    userInput = input("the doggy has arrived.... you must make a choice to save a new generation..........\n> ")
    
    if type(userInput) != int:
        consoleOutput.clearConsole()
        return -1