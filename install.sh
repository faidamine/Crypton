#!/bin/bash
echo "[ ]====================================================================[ ]";
echo "[ ]                         Crypton  Tool                               [ ]";
echo "[ ]                  Crypton Tool Install Script                        [ ]";
echo "[ ]====================================================================[ ]";
echo "";

if [ $(whoami) != "root" ];then
    echo "You must be root to do this."
    exit 1
fi
cd ..
pip install requests
pip install Useragent
pip install cookielib
pip install codecs
pip install xml

cp -R Crypton/ /opt/
echo '#!/bin/sh' > /bin/Crypton
echo 'python /opt/Crypton/Crypton.py "$@"' >> /bin/Crypton
chmod 755 /bin/Crypton
chmod +x /bin/Crypton
rm -rf Crypton/
Crypton
if [ $? -eq 0 ]; then
	echo "WORKED ! NOW YOU CAN USE command! : Crypton"
else
    echo "ERROR FAIL!"
fi
