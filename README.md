# PicCode #

This program hides your text inside an innocent picture.

**HASH (#)** *NOT ALLOWED*

## Windows ##

To install, double click on `install.bat` or simply write `install.bat` on your cmd.

**Please be online while installing as the program need to download few prerequisites.**



To run, double click on `run.bat` or simply write `run.bat` on your cmd.


If want to see coloured text, download latest `Windows Terminal` from Microsoft store (free of cost).


To uninstall, either delete the folder or double click `uninstall.bat`. It only removes the prerequistes(downloaded during installation) from your computer.



## Linux / MacOS ##

To install, double click on `install.sh` or simply write `./install.sh` on your cmd.

**Please be online while installing as the program need to download few prerequisites.**



To run, double click on `run.sh` or simply write `./run.sh`  on your terminal


To uninstall, either delete the folder or double click `uninstall.sh`. It only removes the prerequistes(downloaded during installation) from your computer.

*While installation, the `install.sh` creates `additions/installed.txt` to keep a record of prequisites downloaded. During uninstallation, `uninstall.sh` use `additions/installed.txt` to remove the prerequisites(downloaded during installation). You may edit `additions/installed.txt` to keep your desired packages.*


### SAD NEWS ###

`cmd` doesnt supports ANSI escape codes, which means characters cannot not be coloured. To solve that I used ansicon.exe ... but most antiviruses treat like a virus as it kind of rewrites your virtual memory. To use it deactivate your antivirus or download a terminal which can support ANSI escape codes (eg. windows terminal). 
