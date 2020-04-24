# Bing-Money
###### Helps you get gift cards with Bing by earning points.

# Details 
##### This was written with python to make a program that can not be detected as a bot.  This should be able to run on anything that has python works with python 2 and 3. It makes everything random from the time that the program runs to the search results.  This is designed to be used with a raspberry pi or an old pc.

# Requirements
* old pc/raspberry pi
* python 2/3
* list of terms

# Set up
1. Make sure you have python installed if using old pc/set up raspberry pi with [raspbian.](https://www.raspberrypi.org/downloads/raspbian/)
2. Choice file with terms, I used [Jeopardy question list.](https://www.reddit.com/r/datasets/comments/1uyd0t/200000_jeopardy_questions_in_a_json_file/)
3. Open CSV file with Excel and delete all columns but questions.
4. Rename the file to 'ques.txt'(make sure it is converted to txt)
5. Open txt file and use crtl F' and search for ' " ' do a replace all with nothing.
6. Copy both programs and txt file to raspberry pi and place them in the same directory(Folder).
7. Run rasp.py file creates infinite loop.
