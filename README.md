# R6-Stats
Uses a screenshot of the scoreboard to find the stats of players.

Takes a screenshot as the input, crops it, and converts the image into an array of the pixels. The array is then further broken into smaller arrays, each containing a different name. These smaller arrays are then passed into a Name object and further subdivided into individual Letter objects. A function in the Letter class uses a text file to match the white pixels to the pixels of specific letters obtained through testing. If there is a new letter, it is put into the newLetterBankFile text file so it can be added to the main LetterBankFile. The letter with the highest percent match is returned so that the Name object to be added to a name string. It has to be done this way since there are slight inconsistencies with the letter pixels from the scoreboard. Once all the letters have been found and there is a completed name string, it is put into a Player object. Inside the Player class there is a method that uses webscraping to get the users basic stats. The stats are then outputted to the terminal.

The screenshots included are samples.
