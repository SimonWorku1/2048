#importing and initializing libraires we need
import pygame
import random
import time
from values import *
from tile import *
from pygame.locals import *
pygame.init()
pygame.font.init()
pygame.mixer.init()

#text font variables
titleFont = pygame.font.SysFont("comicsansms", 100)
blockFont = pygame.font.SysFont("comicsansms", 20)
scoreFont = pygame.font.SysFont("comicsansms", 50)
menuFont = pygame.font.SysFont("comicsansms", 50)

#sound files
sound = pygame.mixer.Sound('bubble.mp3') #merge sound effect
background = pygame.mixer.Sound('C418 - Stal.mp3') #background sound file


class App2048:

    def __init__(self):
        self.goal = 2048
        self.window = pygame.display.set_mode((720, 720))
        pygame.display.set_caption('CMSI 2048 - By Devan, Nathan and Simon')
    
    def resetVariables(self): #Sets the board into a new game state
        self.playing = True
        self.score = 0
        self.board = [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]
        self.randomTile()

    def exit(self): #Exits game
        pygame.quit()
        quit()

    def up(self): #calls the move and merge from board class in the corresponding direction
        for i in range(3):
            self.moveUp()
        self.mergeUp()
        for i in range(3):
            self.moveUp()
        self.drawWindow()
        self.update()

    def down(self): #calls the move and merge from board class in the corresponding direction
        for i in range(3):
            self.moveDown()
        self.mergeUp()
        for i in range(3):
            self.moveDown()
        self.drawWindow()
        self.update()
    
    def left(self): #calls the move and merge from board class in the corresponding direction
        for i in range(3):
            self.moveLeft()
        self.mergeLeft()
        for i in range(3):
            self.moveLeft()
        self.drawWindow()
        self.update()

    def right(self): #calls the move and merge from board class in the corresponding direction
        for i in range(3):
            self.moveRight()
        self.mergeRight()
        for i in range(3):
            self.moveRight()
        self.drawWindow()
        self.update()
    
    def gameState(self): #returns the string of the current game state
        for row in range(len(self.board)):
            for col in range(len(self.board[row])):
                if self.board[row][col] == self.goal: #if any tile is equal to the goal 2048, returns WIN
                    self.drawWindow()
                    return "WIN"
                
        if not self.isFull(): #if the board is NOT full, then returns AVAILABLE
            return "AVAILABLE"
        
        if self.validMoves(): #runs only if the board IS full, if any two touching tiles are equal, returns CANMOVE
            return "CANMOVE"
        
        self.drawWindow()
        return "LOSE" #only runs if all other states above aren't true
    
    def update(self): #checks the game state and changes screen accordingly
        state = self.gameState()
        self.drawWindow()
        if state == "WIN":
            self.drawWindow()
            x = time.time()
            if time.time() - x <= 1000:
                self.gameWin(True)
        elif state == "AVAILABLE":
            self.randomTile()
        elif state == "LOSE":
            self.drawWindow()
            x = time.time()
            if time.time() - x <= 1000:
                self.gameWin(False)

    def drawWindow(self): #updates the screen
        self.window.fill("black")
        self.drawGrid()
        self.drawTiles()
        self.drawScore()

    def drawGrid(self): #making the grid the game is played on
        blockSize = 125
        for x in range(112, 512, blockSize):
            for y in range(200, 600, blockSize):
                rect = pygame.Rect(x, y, blockSize, blockSize)
                pygame.draw.rect(self.window, "gray", rect, 2)

        self.tiles = []
        for row in range(4):
            for column in range(4):
                if not self.getValue([row, column]) == 0:
                    tile = Tile(self.window, [row * 125, column * 125], Color_Cells.get(self.getValue([row,column])), str(self.getValue([row, column])))
                    self.tiles.append(tile)

    def drawTiles(self): #converts the values from the 2d array into visuals in the gui
        for Tile in self.tiles:
            Tile.drawTile()
        

    def gameWin(self, win): #ends game, check if you won or not through the argument
        self.drawWindow()
        self.drawEnd()
        background.stop()
        if win: 
            text = menuFont.render("You win!", True, 'Blue')
        else: 
            text = menuFont.render("Better luck next time!", True, 'Red')
        self.window.blit(text, (100, 100))
        text = menuFont.render("Your score:" + str(self.score), True, 'White')
        self.window.blit(text, (100, 200))
        text = menuFont.render("Press Space to play again", True, 'White')
        self.window.blit(text, (100, 300))
        text = menuFont.render("Press Esc to quit playing", True, 'White')
        self.window.blit(text, (100, 400))
        pygame.display.update()
        screen = True
        while screen:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.exit()
                if event.type == KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_SPACE:
                        self.screen = False
                        self.main()

    def drawEnd(self): #creates a blank screen for when you win or lose
        self.window.fill('black')


    def drawScore(self): #draws score on game screen
        text = titleFont.render("CMSI 2048", True, "white")
        self.window.blit(text, (100, 0))
        text = scoreFont.render("Score:" + str(self.score), True, "white")
        self.window.blit(text, (400, 100))

    def main(self): #main loop for playing game
        self.resetVariables()
        background.play()
        background.set_volume(0.25)
        while self.playing:
            self.drawWindow()
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == QUIT:
                    pygame.quit()
                    quit()
                if event.type == KEYDOWN:
                    if event.key == pygame.K_w or event.key == pygame.K_UP:
                        self.up()
                        self.drawWindow()
                    if event.key == pygame.K_s or event.key == pygame.K_DOWN:
                        self.down()
                        self.drawWindow()
                    if event.key == pygame.K_a or event.key == pygame.K_LEFT:
                        self.left()
                        self.drawWindow()
                    if event.key == pygame.K_d or event.key == pygame.K_RIGHT:
                        self.right()
                        self.drawWindow()
            final = ""
            for ro in range(4):
                for col in range(4):
                    final += str(self.board[ro][col])
                final+= "\n"
            print(final)
        self.mainMenu()

    def mainMenu(self): #draws the main screen
        self.window.fill("black")
        text = menuFont.render("Welcome to 2048", True, "white")
        self.window.blit(text, (150, 360))
        text = menuFont.render("Press any key to play", True, "white")
        self.window.blit(text, (120, 460))
        pygame.display.update()
        playing = True
        while playing:
            for event in pygame.event.get():
                if event.type == QUIT:
                    self.exit()
                if event.type == pygame.KEYDOWN:
                    playing = False
        self.main()

    def newBoard(self): #resets the board
        self.score = 0
        self.board = [[0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0],
                      [0,0,0,0]]
        
    def emptyTile(self): 
        """loops through 2d array, returns list of indexes of empty tiles"""
        emptyIndex = []
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if self.board[row][column] == 0:
                    emptyIndex.append([row, column])
        return emptyIndex
    
    def isFull(self):
        """Checks board if there are any empty tiles. Returns false if there is"""
        for row in range(len(self.board)):
            for column in range(len(self.board[row])):
                if self.board[row][column] == 0:
                    return False
        return True
    
    def validMoves(self):
        """if the board isn't full or there is a valid move, returns True"""
        for row in range(len(self.board)):
            for column in range(3):
                if self.getValue([row, column]) == self.getValue([row, column + 1]):
                    return True

        for column in range(len(self.board)):
            for row in range(3):
                if self.getValue([row, column]) == self.getValue([row + 1, column]):
                    return True
    
    def getValue(self, coordinates):
        """returns value of tile at index coordinates """
        row = coordinates[0]
        column = coordinates[1]
        return self.board[row][column]

    def updateTile(self, coordinates, value): 
        """takes a list for coordinates, updates the tile at coordinates to value"""
        row = coordinates[0]
        column = coordinates[1]
        self.board[row][column] = value

    def randomTile(self): 
        """checks empty tile coordinates and randomly updates one of them to 2 or 4, 10% chance"""
        emptyTiles = self.emptyTile()
        randomCoordinate = random.choice(emptyTiles)
        chanceFour = random.randint(0,9)
        if chanceFour == 0:
            self.updateTile(randomCoordinate, 4)
            return randomCoordinate
        else:
            self.updateTile(randomCoordinate, 2)
            return randomCoordinate

    def __str__(self): #converts the 2d array into a string for testing purposes
        final = ""
        for ro in range(4):
            for col in range(4):
                final += str(self.board[ro][col])
            final+= "\n"
        return final       
        
    def moveUp(self):
        for row in range(len(self.board)): #checking if the blocks are empty from top to bottom
            for column in range(len(self.board[row])):
                if(self.board[row][column] == 0 and row < 3):
                    self.board[row][column] = self.board[row + 1][column] #replaces first box with the previous
                    self.board[row + 1][column] = 0 #makes previous box 0 so the code can move down                              

    def moveDown(self):
        for row in range(len(self.board)): #checking if the blocks are empty from bottom to top
            for column in range(len(self.board[row])):
                if(self.board[row][column] == 0 and row > 0):
                    self.board[row][column] = self.board[row - 1][column] #replaces first box with the previous
                    self.board[row - 1][column] = 0 
        

    def moveLeft(self):
        for row in (range(len(self.board))): #checking if the blocks are empty from right to left
            for column in (range(len(self.board[row]))):
                if(self.board[row][column] == 0 and column < 3):
                    self.board[row][column] = self.board[row][column + 1] #replaces first box with the previous
                    self.board[row][column + 1] = 0 #
        
    def moveRight(self):
        for row in (range(len(self.board))): #checking if the blocks are empty from right to left
            for column in (range(len(self.board[row]))):
                if(self.board[row][column] == 0 and column > 0):
                    self.board[row][column] = self.board[row][column - 1] #replaces first box with the previous
                    self.board[row][column - 1] = 0 #  
                        
    def mergeUp(self): #merges tiles next to each other of equal value when w key is pressed
        for column in range(len(self.board)):
            row = 0
            while row < len(self.board) - 1:
                checker = row + 1
                if self.getValue([row,column]) == self.getValue([checker,column]) and self.getValue([row,column]) != 0:
                    sound.play()
                    newValue = self.getValue([row,column]) * 2
                    self.updateTile([row,column], newValue)
                    self.updateTile([checker,column], 0)
                    self.score += newValue
                    self.drawTiles()
                row += 1

    def mergeDown(self): #merges tiles next to each other of equal value when s key is pressed
        for column in range(len(self.board)):
            row = 3
            while row > 1:
                checker = row - 1
                if self.getValue([row,column]) == self.getValue([checker,column]) and self.getValue([row,column]) != 0:
                    sound.play()
                    newValue = self.getValue([row,column]) * 2
                    self.updateTile([row,column], newValue)
                    self.updateTile([checker,column], 0)
                    self.score += newValue
                    self.drawWindow()
                row -= 1

    def mergeLeft(self): #merges tiles next to each other of equal value when a key is pressed
        for row in range(len(self.board)):
            column = 0
            while column < 3:
                checker = column + 1
                if self.getValue([row,column]) == self.getValue([row,checker]) and self.getValue([row,column]) != 0:
                    sound.play()
                    newValue = self.getValue([row,column]) * 2
                    self.updateTile([row,column], newValue)
                    self.updateTile([row,checker], 0)
                    self.score += newValue
                    self.drawWindow()
                column += 1

    def mergeRight(self): #merges tiles next to each other of equal value when d key is pressed
        for row in range(len(self.board)):
            column = 3
            while column > 0:
                checker = column - 1
                if self.getValue([row,column]) == self.getValue([row,checker]) and self.getValue([row,column]) != 0:
                    sound.play()
                    newValue = self.getValue([row,column]) * 2
                    self.updateTile([row,column], newValue)
                    self.updateTile([row,checker], 0)
                    self.score += newValue
                    self.drawTiles()
                column -= 1

    def spawnRandom(self): #spawns random wherever there is an open space
        tileCoordinates = self.randomTile()
        if tileCoordinates != None:
            tile = Tile(self.window, [tileCoordinates[0] * 120 + 2, tileCoordinates[1] * 120 + 2], Color_Cells.get(self.getValue([tileCoordinates[0],tileCoordinates[1]])), str(self.getValue([tileCoordinates[0], tileCoordinates[1]])))