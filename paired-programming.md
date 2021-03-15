# Goal of the project
The goal of your program is clear (create a brick-breaker game that teaches something about climate change, but there is no mention of specific Python packages you plan to use to create this game. It would be helpful to collaborators if you included a link to `kivy`, like this: [`kivy`](https://kivy.org/#home).

# The Data
Screentouch as input data makes sense conceptually, but I don't understand how to write code that recognizes screentouch. Sounds interesting!

# The code
Yes, there is a good skeleton for this project. Currently, the code can initialize a game with stock .png files as a background and bounce a ball off of a paddle and off of the top and sides of the screen. The ball speeds up as it hits the paddle more often. The code allows the user to control the paddle (not sure how well yet), and there is a counter on the screen that keeps score if you miss the ball with the paddle.

# Code contributions/ideas
I reformatted some things because the linter was telling me to add docstrings to all of the Classes and functions - so make sure to add docstrings when you have proper descriptions for what each function does. You also need to consider what to put into your `__init__` functions for each Class object. I think that some of the functions you have written could be placed inside the `__init__` function instead...maybe.

I also started reading into how to change the color of widgets in `kivy`, but it's a little confusing to me. I created a skeleton of a function that will change paddle color in response to the NumericProperty changing, but I'm not sure if that's the right way to go about it. See [here](https://stackoverflow.com/questions/12997545/how-do-i-change-the-color-of-my-widget-in-kivy-at-run-time) for more ideas about changing paddle color. I added a line (line 16) in your `brickbreak.kv` file to start working with paddle color.
