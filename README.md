# CS50 AI

CS50 AI - is a part of famous Harvard Computer Science course CS50 which targeted on teaching the basic of AI.

All course: https://cs50.harvard.edu/ai/2023/


## Installation

```bash

git clone https://github.com/aunth/CS50_AI

cd CS50_AI

```

# Table of Contents
- SEARCH - First week of the course in which you have to do 2 project
   	- Tic-Tac-Toe: Project in which you have to implement [minimax](https://en.wikipedia.org/wiki/Minimax) algorithm. In the end if you did all corectly,you cannot win in the game.
		Running the game:
		```bash
		source .cs50ai/bin/activate
		cd search/tictactoe
		python3 runner.py
		```
		Сhoose who you want to play as and good luck)
	- Degrees: According to [Six Degrees of Kavin Bacon](https://en.wikipedia.org/wiki/Six_Degrees_of_Kevin_Bacon) anyone in the Hollywood film industry can be connected to Kevin Bacon within six steps, where each step consists of finding a film that two actors both starred in.
		Let's find out whether this true or not). In this project you have to type algorithm which print number of separation between 2 actors. In this project you have 2 Folder (small and large) each of them consist of 3 CSV table: People (which consist id, name and birth of an actor), Movies (id, title and year of this film), Stars (person_id, movie_id which correspond which person stared in which movie).
		Runnig the program:
		```bash
		cd search/degrees
		python3 degrees.py small/large 
		```
		small/large you have to type from which database you want grab the data. Small has 20 rows, large has more than 1M rows.
		After this you have to choose 2 actors from People table and give them as input to the program.
