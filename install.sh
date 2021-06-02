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

read -n 1 -s -r -p "Press any key to continue"

clear

exit 0
EOF

cp additions/uninstall_linux.txt uninstall.sh

chmod 777 run.sh uninstall.sh

read -n 1 -s -r -p "Installation done .... Press any key to continue"

clear
