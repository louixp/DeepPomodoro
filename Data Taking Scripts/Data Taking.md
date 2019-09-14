DeepPomodoro requires lots of training data. To gather data, we created two simple bash scripts, one to gather focused data and one to gather distracted data. It is the data gatherer's responsibility to run the focused script when they are focused, and the distracted script when they are distracted. 

The scripts require the user to install a tool called imagesnap (https://github.com/rharder/imagesnap), which can be easily installed with homebrew: brew install imagesnap. 

We chose to use Google Drive to store our training dataset. In order for the photos to be synced into our shared folder, Google's Backup and Sync tool must be installed (https://www.google.com/drive/download/). After Backup and Sync is configured, we selected two folders to be synced, one corresponding to distracted photos and the other to focused photos. This allows for the synced folder to be accessed via the command line. To use our scripts to train your own data, change the path directory in the script to whichever folder you choose to house your photos. 

We also found that unless you include "export PATH=/usr/local/bin:$PATH" at the beginning of the script, imagesnap will not be recognized. The script first navigates into the folder housing the training data. Then, it calls imagesnap's -w 1.00 command, which waits for a second before proceeding. This is because we sometimes would get blacked out frames for the first few photos as the camera warms up. Then the script calls the -t 0.10 command, which essentially works like a while loop, taking a photo every .1 second, giving it a name with the date and time, and storing it in the current directory (our folder in Google Drive). 

These scripts can be run in the terminal or, if you are using a Mac, the automator tool. Use whichever suits your needs. 

Happy training!
