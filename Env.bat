@ECHO OFF
ECHO Activating Anaconda
call conda activate Data_Science
ECHO Anaconda is ON
call cd A:/config
ECHO Folder locked in
call conda env export > Data_Science.yml
ECHO Enviroment file generated
call pip freeze > Data_Science.txt
ECHO Packages file generated
ECHO ALL DONE!!
ECHO CLOSING
ping -n 3 localhost >nul
ECHO .
ping -n 3 localhost >nul
ECHO ..
ping -n 3 localhost >nul
ECHO ...
ping -n 3 localhost >nul
ECHO ....
ping -n 3 localhost >nul
ECHO .....
exit
