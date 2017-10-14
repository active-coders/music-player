# import the required modules
from pygame import mixer
from pathlib import Path
from time import sleep
from tinytag import TinyTag
mixer.init()  # initialise sound
while True:
    music = input("what is the name of your music? ")
    my_file = Path(music)
    if my_file.is_file():
        print("")
        loop = input("would you like to loop it? y or n? ")
        if loop == "y":
            tag = TinyTag.get(music)
            mixer.music.load(music)
            mixer.music.play()
            sleep(5)
            mixer.music.pause()
            sleep(5)
            mixer.music.unpause()
            sleep(tag.duration)
            
        print("")
        print("what will you play next?")
        print("")
    else:
        print("")
        print("please enter a file that exists")
        print("")
        
