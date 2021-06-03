@echo off
cls
::echo checking internet connection
Ping www.google.nl -n 1 -w 1000 >NUL
cls
if errorlevel 1 (set internet=Not connected to internet) else (set internet=Connected to internet)

echo %internet%

if "%internet%" == "Not connected to internet" (
	echo Exiting
	pause
	exit /B
	)

echo Downloading python as epthon.zip
curl https://www.python.org/ftp/python/3.9.5/python-3.9.5-embed-amd64.zip > epython.zip

echo Unzipping epython.zip as py
unzip -o epython.zip -d env1
del /F /Q epython.zip

echo Downloading get-pip
curl -L https://bootstrap.pypa.io/get-pip.py>env1/get-pip.py
.\env1\python.exe .\env1\get-pip.py  --no-setuptools --no-wheel --no-warn-script-location

echo Setting up python
(echo python39.zip
echo .
echo import site) > env1/python39._pth

echo Downloading Pillow
.\env1\python.exe -m pip install Pillow

echo Making run.bat
(echo @echo off
echo cls
echo .\env1\python.exe PicCode.py
echo pause
echo cls) > run.bat

echo Making uninstall.bat
(echo @echo off
echo cls
echo rmdir /S /Q env1
echo del /Q run.bat
echo echo Unistallation Successful... You may delete the whole folder or use the install.bat to reinstall the program
echo call :deleteSelf^&exit /b
echo :deleteSelf
echo start /b ^"^" cmd /c del ^"%%~f0^"^&exit /b) > uninstall.bat
echo.
echo run.bat will start your program ..... please use Windows Terminal(from Microsoft Store) to see colourful text
echo.
echo Installation done
echo.
pause
cls