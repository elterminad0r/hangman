# hangman
A bit of a legacy project on Hangman. It's an implementation of hangman, where the man being hanged is drawn in Turtle. I have to say I'm actually pretty proud of it. It originally used some slightly messy terminal escape codes to try and hide user input - this has since been replaced with `getpass`. It also features a pretty robust command line interface which happens in parallel with the turtle graphics. Here it is in action (where the invisibly entered word is `"izaak van dongen"`):

	What should the word be? 
	Can you verify?
	Incorrect letters you have guessed:
	 
	This how much you have currently guessed:
	_ _ _ _ _ / _ _ _ / _ _ _ _ _ _
	You have 10 remaining guesses
	Guess a letter
	a
	You guessed correctly!
	Incorrect letters you have guessed:
	 
	This how much you have currently guessed:
	_ _ a a _ / _ a _ / _ _ _ _ _ _
	You have 10 remaining guesses
	Guess a letter
	v
	You guessed correctly!
	Incorrect letters you have guessed:
	 
	This how much you have currently guessed:
	_ _ a a _ / v a _ / _ _ _ _ _ _
	You have 10 remaining guesses
	Guess a letter
	n
	You guessed correctly!
	Incorrect letters you have guessed:
	 
	This how much you have currently guessed:
	_ _ a a _ / v a n / _ _ n _ _ n
	You have 10 remaining guesses
	Guess a letter
	x
	That was wrong.
	Incorrect letters you have guessed:
	 x
	This how much you have currently guessed:
	_ _ a a _ / v a n / _ _ n _ _ n
	You have 9 remaining guesses
	Guess a letter
	y
	That was wrong.
	Incorrect letters you have guessed:
	 xy
	This how much you have currently guessed:
	_ _ a a _ / v a n / _ _ n _ _ n
	You have 8 remaining guesses

After several more failures, the screen will turn red and look like this (NB this has been building up in steps like a proper hangman game):

![screenshot](https://github.com/elterminad0r/hangman/blob/master/fail.png)
