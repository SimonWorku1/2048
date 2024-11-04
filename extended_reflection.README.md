Your original project plan, your final project plan, and a description of how and why it changed from its original form.

Our original project plan was to at minimum have a replica of the 4x4 grid with the working 2048 game, have a homepage for the user when they run the game, and screens with messages when the game is won or lost used for the game 2048. Some extra features we initially hoped to add were to let the user keep playing after reaching 2048 if they chose to, adding a score counter, and to make a “opposite 2048” where the keys did the opposite as they would suggest, and sound effects for the tiles merging
Our final project plan is to have all of the minimum requirements we set for ourselves, but besides the score tracker, we likely won't have the time needed to add any of the additional features. We were able to add a score counter feature, and we also added sound effects for our game. However, we ran out of time when it came to extending our game beyond the 2048 value, and we weren’t able to create an “opposite 2048” game mode.
Our project plan had to change because it ended up taking longer to figure out how to make our game work. We even had to change the structure for our classes and objects because the game wasn’t working with our first iteration of code, so we had to make a hard pivot and try something new. Having that detour caused our project to fall quite a bit behind schedule, so for the rest of the project time, we had to focus that on making sure we hit our minimum requirements, and we chose to add only the easiest “extra” features such as sound effects and a score counter.

A list of which team members did what during the project.

Devan: Spearheaded figuring out new libraries like pygame, and figuring out the class-object relationships so our group would know how to structure our game coding wise.
Nathan: Planned group meetings, and helped add code for the front end part of our project like sounds, drawing the grid, etc
Simon: Main person to check code, and came up with the different tasks our team needed to do, and then divided the tasks for each person.

A description of any difficulties you had and how you overcame them. Also include anything interesting you learned about Python, programming, or working on a team.

Our biggest struggle was learning how to use the pygame library. There were multiple occasions where we had a “how the heck does this library even work?” moment.
Another big issue was figuring out how to use liveshare since only one person can run the code, and sometimes multiple people can’t work on the code at the same time.
We overcame these problems with determination and being an adaptive team. We weren’t able to figure out how to use pygame on the first general google search, but rather after a series of google searches where we started to piece together the features we needed to learn and figuring out how to apply them to our code. For the liveshare, we had to change our approach to testing very frequently. So when one piece of code was updated, we would test it right away to make sure it works. That way we were able to keep track of what problems we needed to fix since it’s not like we could all run the code. So essentially, a lot of our meetings became research, code, test, repeat. Slow and steady won the race.
Some lessons we learned as a team are that communication is key: whether it’s setting up team meetings and finding times that work for everyone’s schedule, being willing to do tasks you weren’t originally planning on doing so that you can help the team. In the end, working together as a team made us a lot stronger because we were able to rely on each other for ideas and work off of each other instead of being stuck on certain tasks alone.

A reflection on whether and how ChatGPT was used during the final project (e.g., changes you made based on code style feedback or bugs it found). If you used ChatGPT, how helpful did you find it? How was your experience?

Surprisingly, our team ended up not really using chatgpt. There were definitely instances where we tried to use it when we were really stuck on a certain piece of code, but when we tried to ask ChatGPT for help with our code, it wasn’t too much use. Maybe part of that was on us for not specifying our problems enough for ChatGPT, it also might be that ChatGPT wouldn’t have helped us that much regardless of how well we explained our code problems to ChatGPT.


Acknowledgements for any code or libraries used in your project that wasn’t explicitly written by a member of your team

https://www.pygame.org/docs/tut/ChimpLineByLine.html

A complete user’s manual (in a file named Readme) for how to run your program and what you can do with it. The user’s manual should be designed for someone who does not know or need to know how your project works. Instead, it should contain enough information to enable others to run your code.

Hello gamer! Welcome to 2048! Whether you’ve played this game or not, we hope you enjoy our version of the classic 2048 game.
To start, you will need to run the main.py file, and press run to start the game. When you open the game, you should see a homescreen with directions on it. Please follow the directions on the homescreen to start the game.
You will now be playing the game. At first, your game should spawn either a 2 or 4 tile. You might be thinking, “what can I even do with one tile?” Well, start the game by pressing either the w key to move the tile up, s key to move the tile down, a key to move the tile left, or d key to move the tile right. Each time you press an arrow, a new 2 or 4 tile will randomly spawn in any space in the grid that isn’t occupied. What you want to try and do is press the keys to combine tiles of the same values. Each time you merge tiles, you’ll add to your score, but what you should really focus on is trying to merge tiles efficiently. Remember, your goal is to get to a tile with the value 2048. So if two 2s is 4, two 4s is 8, etc, you get the point. You’ll have to combine quite a few tiles to get to 2048, but once your 4x4 grid fills up and no two tiles of the same value are adjacent to each other, the game will be over.
If that’s the case, you’ll be directed to a screen where you can choose to play again, or you can exit the game. If you play again, a new game will start up.
If you get to 2048, you’ll get a screen congratulating you on winning the game. You’ll have the option to restart the game or quit the game.
