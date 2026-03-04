In this assignment your team will perform an impact analysis on adding a change to the Angband game. The change is to add a realtime clock that tracks the amount of realtime spent by the user playing a character. So the timer should start when a player starts a new character and ends when the character dies. The time played will need to be managed across play sessions for a character.

In class we discussed several option for displaying the information. Your team can decide if the time spent is visible in the main screen either in the stats bar to the left or the status bar at the bottom of the screen or in the Character Information display - possibly replacing the Game Ticks information.

This is a team BEST project. A member of the team needs to create the feature branch,  A03, off of main and push it to create it in Github.iu.edu. Then each member can pull the branch from GitHub.iu.edu git pull origin A03. Then each member creates their development branch, A03-user 

Now you can create the markdown file: angband-analysis.md. Each team member will write their own version and then the team will choose and/or assemble the team's version to commit to the A03 branch. The team will submit a PR for the A03 branch to Canvas. 

Task 
Identify what components and/or source files that will likely need to be modified to implement this feature.

Areas that will need to be addressed:
Location of the time display and the items that will need changed. Include when the time display will be updated.
The mechanism for getting the current time and updating it between sessions.
How and where the information will be saved between sessions.
Display the played time when the character dies. 
A short description of the advantages or trade-offs with each decision, i.e. placement of the time on the screen, storage format of the time, save file format changes, etc.
Optionally including the information in the Hall of Fame.
Estimate the amount of effort that would be required for your team to make the changes. This should not be a detailed estimate. Use a scale of 1-5 with 1 being a trivial change of adding additional line and a unit test or two to verify. 5 would be a complete re-work of core functionality in the program to achieve the result and extensive test suite development to ensure nothing is broken. This rating should be assigned to each component or .c file you expect to have to modify. 
Markdown Format:
# Angband Analysis TeamXX
## List of areas to be modified
- Area 1: The player model is an area that will need to be modified in order to store the real time. (src/player.h), (src/player.c).
No display in this area. Add the real time played in seconds and minutes, then add the real time session start/stop marks.
Set timer to 0 which will be the session start marker which will add the total time spent in the session to this mark.
Will most likely need a method where the savefile gets written and saved to the system.
Some pros of this approach is separation. A trade off is needing to save/load to continue in a new session.
- Area 2: Character creation area will be modified to set the timer at 0. (src/player-birth.c)
No display yet.
set the real time played in seconds to 0 and the real time session start/stop marks to 0. Has to count as soon as the new character is birthed.
Create a new session mark.
The real time played in seconds will have to be written in the savefile.
Pros are that it guarantees that the timer begins in the first session.
- Area 3: When a user loads a previous save file will need to be modified, resuming the total time whenever the user creates a new session. (src/load.c)
No display yet.
Make sure no time is added during loading. It will only restart the mark.
The time at 0 will create a new session mark. It will make sure that the time it takes to load the game will not be counted.
Pros are it does not include adding to the timer when the game is offline. A trade off is that the user will not be able to see their time including the breaks.
- Area 4: Where the user saves a game will need to be modified as well since the time needs to be saved at the current time the game was saved at. (src/save.c), (src/savefile.c)
No display.
The real time played method should be called before writing the savefile.
It should write the real time played in seconds method into the savefile.
The total playtime will be updated when there is a manual save, autosave, save when the user quits the game, save when the user's character dies.
real time played will use the 0 time mark and the real time session mark.
The information will be saved in the character savefile.
Some pros are that this appraoch is simple and not much risk. A tradeoff is that if the game crashes the timer will use the last autosave.
- Area 5: The in game character display will need to be modified so the user can see playtime when they open their character's stats. (src/ui-player.c)
The display timer will be displayerd on the character stats screen.
Will need a string that will display the current real time in the character stat screen which will still be updating.
Some pros are that it display every time the user opens their character's stats. A tradeoff is that the screen could be overcrowded.
- Area 6: When the character ends the game by dying is where it needs to display the time as well. (src/ui-death.c)
## List of .c files likely to be modified
- src/player.h and the src/player.c where the team will add functions and fields for the timer.
- src/player-birth.c will be modified which will create new fields for a character that is made.
- src/load.c is going to be where the session start time will be implemented when the game has loaded.
- src/savefile.c will be the location where the save is going to be updated and will read and write the new timestamp.
- src/save.c will need to be looked into in order to write the save timestamp.
- src/ui-player.c will be the location where the team will work on displaying the time on the character stats display.
- src/ui-death.c will be another display where the user can see the timestamp whenever the game has ended.
The display will call the real time played method before the death screen. It will render a line of the time played.
The game should already finalize the total playtime if there is a written save or death.
Time should be displayed and finalized when the character dies.
Some pros are that it will definitely display the time at the end. A tradeoff is deciding if there needs to be multiple displays depending on how many screens are displayed after death.
### for each file in the list the estimated effort and nature of the change
- src/player.c & src/player.h: 2
- src/player.birth.c: 1
- src/load.c: 2
- src/save.c: 2
- src/savefile.c: 4
- src/ui-player.c: 3
- src/ui-death.c: 2
YOU DO NOT NEED TO PROVIDE THE MODIFIED CODE! I am not asking you to implement this feature. I am only asking to you do a rough but relatively thorough estimate of the impact of this feature change.  

Criteria for Success 
Submit the A03 PR URL from the team repository. This should merge the markdown file specified above.  You should be able to identify at least a half dozen modifications to be made.
