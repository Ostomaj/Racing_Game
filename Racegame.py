import pygame
import sys
import time
from neopixel import *
import argparse

# LED strip configuration:
LED_COUNT      = 300    # Number of LED pixels.
LED_PIN        = 18      # GPIO pin connected to the pixels (18 uses PWM!).
#LED_PIN        = 10      # GPIO pin connected to the pixels (10 uses SPI /dev/spidev0.0).
LED_FREQ_HZ    = 800000  # LED signal frequency in hertz (usually 800khz)
LED_DMA        = 10      # DMA channel to use for generating signal (try 10)
LED_BRIGHTNESS = 30    # Set to 0 for darkest and 255 for brightest
LED_INVERT     = False   # True to invert the signal (when using NPN transistor level shift)
LED_CHANNEL    = 0       # set to '1' for GPIOs 13, 19, 41, 45 or 53

# Create NeoPixel object with appropriate configuration.
strip = Adafruit_NeoPixel(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
# Intialize the library (must be called once before other functions).
strip.begin()


#Denote the screen elements
screen = pygame.display.set_mode((626, 601))  # Size of the background image.
#set a clock
clock = pygame.time.Clock() #Create a clock

#Ostrich Button
Ostrichbutton = pygame.image.load("/home/pi/Desktop/RACEGAME/RaceGameFiles/Buttons/OstrichButton.png")
#Set the ostrich button
Ostrichbutton = pygame.transform.scale(Ostrichbutton,(150,150))

#Squirrel Button
Squirrelbutton = pygame.image.load("/home/pi/Desktop/RACEGAME/RaceGameFiles/Buttons/SquirrelButton.png")
#Set the squirrel Button
Squirrelbutton = pygame.transform.scale(Squirrelbutton,(150,150))

#Turtle Button
Turtlebutton = pygame.image.load("/home/pi/Desktop/RACEGAME/RaceGameFiles/Buttons/TurtleButton.png")
#Set the turtle button
Turtlebutton = pygame.transform.scale(Turtlebutton,(150,150))

#define a function to load an image
def load_image(name):
    image = pygame.image.load(name)
    return image

#Define a class of test sprite
class TestSprite(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite, self).__init__()
        self.images = []
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/ostrichpics/ostrich1.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/ostrichpics/ostrich2.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/ostrichpics/ostrich3.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/ostrichpics/ostrich4.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/ostrichpics/ostrich5.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/ostrichpics/ostrich6.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/ostrichpics/ostrich7.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/ostrichpics/ostrich8.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/ostrichpics/ostrich9.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/ostrichpics/ostrich10.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/ostrichpics/ostrich11.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/ostrichpics/ostrich12.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/ostrichpics/ostrich13.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/ostrichpics/ostrich14.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/ostrichpics/ostrich15.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/ostrichpics/ostrich16.png"))

        # assuming both images are 64x64 pixels

        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(245, 23, 190, 200)

#define a moveright function
    def moveright(self,pixels):
        self.rect.x += pixels

#Goes through the images
    def update(self):
        '''This method iterates through the elements inside self.images and
        displays the next one each tick. For a slower animation, you may want to
        consider using a timer of some sort so it updates slower.'''
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

def load_image2(name2):
    image = pygame.image.load(name2)
    return image

class TestSprite2(pygame.sprite.Sprite):
    def __init__(self):
        super(TestSprite2, self).__init__()
        self.images = []
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/Turtlepics/Turtle1.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/Turtlepics/Turtle2.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/Turtlepics/Turtle3.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/Turtlepics/Turtle4.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/Turtlepics/Turtle5.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/Turtlepics/Turtle6.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/Turtlepics/Turtle7.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/Turtlepics/Turtle8.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/Turtlepics/Turtle9.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/Turtlepics/Turtle10.png"))
        self.images.append(load_image("/home/pi/Desktop/RACEGAME/RaceGameFiles/Turtlepics/Turtle11.png"))
        self.index = 0
        self.image = self.images[self.index]
        self.rect = pygame.Rect(245, 492, 190, 200)


    def moveright(self,pixels):
        self.rect.x += pixels

    def update(self):
        '''This method iterates through the elements inside self.images and
        displays the next one each tick. For a slower animation, you may want to
        consider using a timer of some sort so it updates slower.'''
        self.index += 1

        if self.index >= len(self.images):
            self.index = 0
        self.image = self.images[self.index]

#Load the background
bg = pygame.image.load("/home/pi/Desktop/RACEGAME/RaceGameFiles/Background.jpg")
#Define the main game
def main():
    #Define the name on the banner
    pygame.display.set_caption('Race the Animal Game')
    #Deine boundaries for ost,squ, and turt
    xost=400
    yost=300
    xsqu=240
    ysqu=300
    xturt=80
    yturt=300
    #Initialize pygame
    pygame.init()
    #Background size
    screen = pygame.display.set_mode((626, 601))  # Size of the background image.
    #Load the background
    screen.blit(bg, (0, 0))  # Load background
    #Load the buttons
    screen.blit(Ostrichbutton,(xost,yost,150,150))
    screen.blit(Squirrelbutton,(xsqu,ysqu,150,150))
    screen.blit(Turtlebutton,(xturt,yturt,150,150))
    #Load teh sprites
    my_sprite = TestSprite()
    my_sprite2 = TestSprite2()
    my_group = pygame.sprite.Group(my_sprite)
    my_group2 = pygame.sprite.Group(my_sprite2)
    screenchange = 0
    #Define the quit function
    while screenchange == 0:
        clock.tick(30)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit(0)
            #If there's an event where the mouse clicks find out where
            #Then select an animal based off x and y positions
            if event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                mpos = pygame.mouse.get_pos()
                print(event.pos)
                #Position for ostrich
                if mpos[0] >= 413 and mpos[1] <= 437 and mpos[0] <=539 and mpos[1] >=312:
                    print('Clicked on Ostrich')
                    screenchange = 1
                    Animalchoice = 3
                #Position for squirrel
                if mpos[0] >= 249 and mpos[1] <= 440 and mpos[0] <= 379 and mpos[1] >= 311:
                    print('Clicked on Squirrel')
                    screenchange = 1
                    Animalchoice = 2
                #Position for Turtle
                if mpos[0] >= 85 and mpos[1] <= 436 and mpos[0] <=223 and mpos[1] >=311:
                    print('Clicked on Turtle')
                    screenchange = 1
                    Animalchoice = 1

        # Calling the 'my_group.update' function calls the 'update' function of all
        # its member sprites. Calling the 'my_group.draw' function uses the 'image'
        # and 'rect' attributes of its member sprites to draw the sprite.

        #When something is clicked flip the screen to 3,2,1, go
        pygame.display.update()
        pygame.display.flip()
        my_group.update()
        my_group.draw(screen)
        my_group2.update()
        my_group2.draw(screen)
        while screenchange == 1:
            bg2 = pygame.image.load("/home/pi/Desktop/RACEGAME/RaceGameFiles/Countdown/Large3.png")
            bg2 = pygame.transform.scale(bg2,(630,626))
            bg3 = pygame.image.load("/home/pi/Desktop/RACEGAME/RaceGameFiles/Countdown/Large2.jpg")
            bg3 = pygame.transform.scale(bg3,(630,626))
            bg4 = pygame.image.load("/home/pi/Desktop/RACEGAME/RaceGameFiles/Countdown/Large1.png")
            bg4 = pygame.transform.scale(bg4,(630,626))
            bg5 = pygame.image.load("/home/pi/Desktop/RACEGAME/RaceGameFiles/Countdown/LargeGo.png")
            bg5 = pygame.transform.scale(bg5, (630, 626))

            screen = pygame.display.set_mode((626, 601))  # Size of the background image.
            pygame.mixer.init()
            pygame.mixer.music.load("/home/pi/Desktop/RACEGAME/RaceGameFiles/Audio/Three.mp3")
            pygame.mixer.music.play()
            screen.blit(bg2,(0,0))  # Load background 3
            pygame.display.update()
            pygame.time.wait(1000)
            pygame.mixer.music.load("/home/pi/Desktop/RACEGAME/RaceGameFiles/Audio/Two.mp3")
            pygame.mixer.music.play()
            screen.blit(bg3, (0,0)) # Load background 2
            pygame.display.update()
            pygame.time.wait(1000)
            pygame.mixer.music.load("/home/pi/Desktop/RACEGAME/RaceGameFiles/Audio/One.mp3")
            pygame.mixer.music.play()
            screen.blit(bg4,(0,0))  # Load background 1
            pygame.display.update()
            pygame.time.wait(850)
            pygame.mixer.music.load("/home/pi/Desktop/RACEGAME/RaceGameFiles/Audio/Go.wav")
            pygame.mixer.music.play()
            screen.blit(bg5, (0, 0))
            pygame.time.wait(850)
            pygame.display.update()  # Load background GO!
            
            #If TURTLE IS CHOSEN
            if Animalchoice == 1:
                print("You chose a Slow Speed animal")
                #Create a color Green then show the pixels
                for i in range(0, strip.numPixels(), 1):
                    strip.setPixelColor(i, Color(200,   0,   0))
                    strip.show()
                    time.sleep(100/4000.0)
                #Make the pixels all color none
                #for i in range(0, strip.numPixels(), 1):
                #    strip.setPixelColor(i, Color(203,   255,   192))
                #    strip.show()
                #    time.sleep(100/4000000.0)
                time.sleep(0.5)
                for i in range(0, strip.numPixels(), 1):
                    strip.setPixelColor(i, Color(0,   0,   0))
                    strip.show()
                    time.sleep(100/9000000000.0)
                #if you choose squirrel
            elif Animalchoice == 2:
                #Lights for medium animal
                print("You chose a Medium Speed animal")
                #Show lights yellow
                for i in range(0, strip.numPixels(), 2):
                    strip.setPixelColor(i, Color(255,   255,   0))
                    strip.show()
                    time.sleep(1/400000.0)
                #Clear lights
                #for i in range(0, strip.numPixels(), 1):
                #    strip.setPixelColor(i, Color(203,   255,   192))
                #    strip.show()
                #    time.sleep(100/4000000.0)
                time.sleep(2)
                for i in range(0, strip.numPixels(), 2):
                    strip.setPixelColor(i, Color(0,   0,   0))
                    strip.show()
                    time.sleep(100/9000000000.0)

            elif Animalchoice == 3:
                #Lights for fast animal
                print("You chose a Fast Speed animal")
                #Create lights red
                for i in range(0, strip.numPixels(), 5):
                    strip.setPixelColor(i, Color(0,   255,   0))
                    strip.show()
                    time.sleep(1/9000000000.0)
                #Clear lights
                #for i in range(0, strip.numPixels(), 1):
                #    strip.setPixelColor(i, Color(192,   255,   203))
                #    strip.show()
                #    time.sleep(100/4000000.0)
                time.sleep(2)
                for i in range(0, strip.numPixels(), 5):
                    strip.setPixelColor(i, Color(0,   0,   0))
                    strip.show()
                    time.sleep(100/9000000000.0)
            #Wait for lights to clear
            pygame.time.wait(2000)
            #Go back to main screen
            screenchange = screenchange -1
            #Go through main again
            main()
            #Exit event
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit(0)


#Run main to start
if __name__ == '__main__':
    main()
