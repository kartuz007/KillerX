echo -e "
\033[1;92m
██╗░░██╗██╗██╗░░░░░██╗░░░░░███████╗██████╗░██╗░░██╗
██║░██╔╝██║██║░░░░░██║░░░░░██╔════╝██╔══██╗╚██╗██╔╝
█████═╝░██║██║░░░░░██║░░░░░█████╗░░██████╔╝░╚███╔╝░
██╔═██╗░██║██║░░░░░██║░░░░░██╔══╝░░██╔══██╗░██╔██╗░
██║░╚██╗██║███████╗███████╗███████╗██║░░██║██╔╝╚██╗
╚═╝░░╚═╝╚═╝╚══════╝╚══════╝╚══════╝╚═╝░░╚═╝╚═╝░░╚═╝
░░░░░░░░░░░░░░░Created by: MrHacker-X░░░░░░░░░░░░░░
░░░░░░░░░░░░░░░Instagram: 0hacker_x0░░░░░░░░░░░░░░░
"
echo
echo

if [ -d "/data/data/com.termux/files" ];then
    echo -e '\033[1;92m[*] Installing required packages and modules in your termux'
    echo
    apt update -y
    apt upgrade -y
    apt install python -y
    apt install python2 -y 
    pip install colorama
    pip install requests
    pip install asyncio
    pip install firebase-admin
    pip install python-dotenv
    pip install proxybroker
    pip install warnings
    echo
    echo
    echo -e "\033[1;92m[*] Installation is finished."
    echo -e "So, now you can run KillerX by command >>"
    echo
    echo -e "python killerx_tmux.py"
    echo
    echo -e "Done"
    echo

    

else
    echo -e '\033[1;92m[*] Installing required packages and modules in your Linux'
    echo
    sudo apt update -y
    sudo apt upgrade -y
    sudo apt install python -y
    sudo apt install python2 -y 
    sudo apt install python3-pip -y 
    sudo apt install python3-pip-whl -y 
    sudo pip install colorama
    sudo pip install requests
    sudo pip install asyncio
    sudo pip install firebase-admin
    sudo pip install python-dotenv
    sudo pip install proxybroker
    sudo pip install warnings
    echo
    echo
    echo -e "\033[1;92m[*] Installation is finished."
    echo -e "So, now you can run KillerX by command >>"
    echo
    echo -e "python killerx.py"
    echo
    echo -e "Done"
    echo
    
fi
