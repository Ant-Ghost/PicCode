#!/bin/bash

clear

case "$(curl -s --max-time 2 -I http://google.com | sed 's/^[^ ]* *\([0-9]\).*/\1/; 1q')" in
    [23])
        echo -e "Internet is up... Downloading\n\n";;
    5)
        echo "the web proxy won't let us through"
        exit;;
    *)
        echo "The network is down or very slow"
        exit;;
esac

echo -e "Checking requirements\n\n"
touch additions/installed.txt
chmod 777 additions/installed.txt

A=$(python --version)

if [[ "$A" == *"command not found"* ]]
then
    echo -e "\n\nRunning command: sudo apt-get install python3\n"
    sudo apt-get install python3
    echo -e "Python3\n" >> additions/installed.txt
else
    echo -e "Python3 exits\n\n"
fi


B=$(python3 -m pip --version)

if [[ "$B" == *"No module"* ]]
then
    echo -e "\n\nRunning command: sudo apt-get install python-pip\n"
    sudo apt-get install python3-pip
    echo -e "Pip\n" >> additions/installed.txt
else
    echo -e "Pip exists\n\n"
fi

C=$(python3 -c "from PIL import Image" 2>&1)

if [[ "$C" == *"No module"* ]]
then
    echo -e "\n\nRunning command: python3 -m pip install Pillow"
    python3 -m pip install Pillow
    echo -e "Pillow\n" >> additions/installed.txt
else
    echo -e "Pillow exists\n\n"
fi

echo -e "\n\n"

cat > run.sh <<EOF
#!/bin/bash

clear

python3 PicCode.py

read -n 1 -s -r -p "Press any key to continue..."

clear

exit 0
EOF

cat > uninstall.sh <<EOF
#!/bin/bash

a=\$(cat additions/installed.txt)
if [[ "\$a" == *"Pillow"* ]]
then
    echo -e "\n\nRunning command: python3 -m pip uninstall Pillow\n"
    echo y | python3 -m pip uninstall Pillow
fi

if [[ "\$a" == *"Pip"* ]]
then
    echo -e "\n\nRunning command: sudo apt-get uninstall -y python3-pip\n"
    sudo apt-get remove -y python3-pip
fi

if [[ "\$a" == *"Python3"* ]]
then
    echo -e "\n\nRunning command: sudo apt-get uninstall -y python3\n"
    sudo apt-get remove -y python3
fi

echo -e "\n\nUninstallation Successfull.... You may delete the folder or you may reinstall this program using install.sh"

read -n 1 -s -r -p "Press any key to continue..."

clear

rm run.sh uninstall.sh additions/installed.txt
exit 0
EOF

chmod 777 run.sh uninstall.sh


read -n 1 -s -r -p "Installation done ....Press any key to continue"

clear