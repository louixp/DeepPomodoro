export PATH=/usr/local/bin:$PATH
while :
do
	cd PhotoFolder
	imagesnap -w 1.00 $(date +%y%m%d%H%M%S).jpg
    cd ~/LocalTestFolder
    python findLandmarks.py
done
