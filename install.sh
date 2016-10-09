#!/bin/bash
echo "[ ]====================================================================[ ]";
echo "[ ]                         Crypton  Tool                               [ ]";
echo "[ ]                  Crypton Tool Install Script                        [ ]";
echo "[ ]====================================================================[ ]";
echo "";
echo "[!] Install.sh will install Crypton tool in the system [Y/n]" ; 
read baba
if [ $baba == "y" ] ; 
  then
    echo " "
  else
    exit
fi

echo "[!] Where Do you want to install the tool? [Ex:/usr/share/doc]:";
read refdir
echo "[!] Checking directories..."
if [ -d "$refdir/Crypton" ] ;
then
echo "[!] A directory Panel-Tracker was found! Do you want to replace it? [Y/n]:" ; 
read mama
if [ $mama == "y" ] ; 
then
 rm -R "$refdir/Crypton"
else
 exit
fi
fi

 echo "[!] Installing ...";
 echo "";
 git clone https://github.com/faidamine/Crypton.git $refdir/Crypton;
 echo "#!/bin/bash 
 perl $refdir/Crypton/crypton.py" '${1+"$@"}' > crypton;
 chmod +x crypton;
 sudo cp crypton /usr/bin/;
 rm crypton;


if [ -d "$refdir/Crypton" ] ;
then
echo "";
echo "Tool istalled with success!";
echo "";
  echo "[ ]====================================================================[ ]";
  echo "[ ]     All is done!! You can execute crypton by typing crypton !        [ ]"; 
  echo "[ ]====================================================================[ ]";
  echo "";
else
  echo "[!] Installation faid!! ";
  exit
fi