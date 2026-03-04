	
	TEST PLAN DEVELOPMENT
		
		This part of the document will cover the test plan for our Angband monster editor. Before going over major and edge test cases, there is some set up that will need to be tested first. These include:
	
	Ensuring the program can be read in the monster.txt file as well as the other related game files without errors or crashing.
	Ensure all monsters can be searched within the program, and that they appear under their appropriate dungeon level.
	Ensure all features of the editor work as intended and do not crash or create errors. Also that when a user makes a change in the editor, that change is reflected in the newly written file.
	Ensure when the user is finished they are able to write a new file, which the changes they made included, and that this text file works with Angband with the monsters being updated with those changes.
	
	Once these necessary set up steps are completed, our team will move on to testing edge cases and sample test cases, to ensure the program works as intended. Our main methods of testing will be unit and integration testing. These two are the most important as unit testing ensures each of the functions and individual components of the program work as intended such as being able to edit monster stats, edit multiple monsters, search monsters, and write out their changes to a new file. These must work in isolation before moving on to integration testing to ensure that our editor program’s components are all functioning with each other, as well as with Angband. The team must do both these methods of testing to ensure both individual and group parts of the program work as intended. Listed below are several sample test cases we will be checking on our editor. 
	
	
	_______________________________________________________________________________
	1
	Invalid input for changing a stat of a monster, or when searching a monster.
	Within the editor, using the search bar/when inputting a value on the monster edit screen.
	The program will output a invalid input message, removing the input and allowing the user to reattempt. 
	
	  Description of the test: A player ran the program and entered various non_existant monster
	  Output: The game output that the monster does/ chatafgory changed and allowed the player to try again. 
	  Status: PASS
	________________________________________________________________________________
	
	2
	Doing multiple edits to a monster’s stats, or multiple edits to multiple monsters.
	Within the editor when changing the monster's stats, and then leaving that page and going to another monster and editing that one’s stats.
	The editor will store this changed information, ensuring it is reflected in the new text file when the user is finished. 
	
	  Description of the test: The player leaves without agreeing to save the file. thus potentailly not getting edits saved
	  Output: the players edits are saved to a dicanary for a breif time. they can run choose to keep editing and thus their edits are saved in the dictanry or they can cancel the program and delete their edits
	  Status: PASS
	____________________________________________________________________________________
	
	3
	Changing a single stat on a single monster. 
	Choosing a monster either from the dungeon list or search feature, taking the user to the edit page and allowing them to change a stat.
	The changed stat will be stored and reflected in the written text document, with the change reflected in Angband.
	
	  Description of the test: fully writing the changes to the file, and then manually going in an checking the file has been altered. then as a follow up test rerunning the programm and cheking the monster stats to see changes. 
	  Output: the file wase upateing correctly
	  Status: PASS
	_______________________________________________________________________________________
	
	4
	Monsters show up when searched on the search screen.
	Navigating to the search page, and tying in a monster name correctly.
	The monster appears in the search list after its name has been inputted.
	
	  Description of the test: checking for a modificTION sesarch screen , inputing charaters that do not exist, name testing
	  Output: testing for monsters that dont exist i.e 77, result none. no navigation screen
	  Status: FAIL
	_______________________________________________________________________________________
	
	Revisions:
	
	Changing the program runtime to allow more practical navigation. I added an elif to the if statement to include every section as its own option. I placed the if within a while loop to allow the program to continue and not terminate before all edits are completed. I added a third option so that you can edit without the need to monster search.
