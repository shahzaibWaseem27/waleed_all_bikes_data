Updates Changelog:

- It is now possible to extract all information of a bike listed in its specifications

- The software will produce an entry in a file for any category of information. e.g: SKUs, Battery, etc.
  Hence, there will be a ".txt" file for any and every category of information

- If a specific category of information is not present in a given bike's specifications table, 
  the entry for that bike would be "not listed" in the corresponding ".txt" file

- You no longer need to make any changes in the python files themselves. Simply copy and paste the URLs
  in the terminal by following the instructions it gives

- Upon running "main.py", there will no longer be a prompt in the terminal for pressing either "d" for adding
  data, or "e" for erasing data. To erase data in a specific bike brand, e.g: merida, norco, enter the following
  command in the terminal:
  
  rm ./bikeBrand/*

  This will delete all files in the folder corresponding to the specified bike brand 

- Due to changes in how erasing of data is performed, running "main.py" assumes you are intending to add data

- Please make sure you are in the correct directory when running "main.py". You can check this in the
  following way:

  1. enter cd waleed_all_bikes_data in the terminal
  2. if an error occurs, it would imply you were already in the correct directory. Simply run the script now
  3. if no error occurs, it would imply you are now in the correct directory. Simply run the script now