#!/bin/bash

clear

case "$(curl -s --max-time 2 -I http://google.com | sed 's/^[^ ]*  *\([0-9]\).*/\1/; 1q')" in
  [23]) 
	  echo -e "Internet is up.... Downloading\n\n";;
  5) 
	  echo "The web proxy won't let us through"
	  exit;;
  *) 
	  echo "The network is down or very slow"
	  exit;;
esac


echo -e "\n\nRunning command: sudo apt-get insatall python3\n"
sudo apt-get install python3

echo -e "\n\nRunning command: sudo apt-get install python3-pip\n"
sudo apt-get install python3-pip

echo -e "\n\nRunning command: python3 -m pip install Pillow\n"
python3 -m pip install Pillow

echo -e "\n\n"

cat > run.sh <<EOF
#!/bin/bash

clear

python3 PicCode.py

clear

read -n 1 -s -r -p "Installation done .... Press any key to continue"

exit 0
EOF

cat > uninstall.sh << 'EOF'
#!/bin/bash

echo -e "\n\n***WARNING***\n"
echo "Do you want to uninstall Pillow?(Y/N)"
read -n 1

if [[ $REPLY == 'Y' ]] || [[ $REPLY -eq 'y' ]]
then
        echo -e "Running command: python3 -m pip -y uninstall Pillow"
        echo y | python3 -m pip uninstall Pillow
if

echo -e "\n\n***WARNING***\n"
read -n 1 -s -r -p "Do you want to uninstall python3-pip?(Y/N)" $CH

if [ $CH -eq 'Y' -o $CH -eq 'y' ]
then
        echo -e "Running command: sudo apt-get uninstall python3-pip"
        sudo apt-get uninstall python3-pip
fi

echo -e "\n\n***WARNING***\n"
read -n 1 -s -r -p "Do you want to uninstall python3?(Y/N)" $CH

if [ $CH -eq 'Y' -o $CH -eq 'y' ]
then
        echo -e "Running command: sudo apt-get uninstall python3"
        sudo apt-get uninstall python3
fi

echo -e "\n\n"
echo -e "Uninstallation complete"

rm run.sh uninstall.sh

exit 0
EOF
chmod 777 run.sh uninstall.sh

read -n 1 -s -r -p "Installation done .... Press any key to continue"

clear
