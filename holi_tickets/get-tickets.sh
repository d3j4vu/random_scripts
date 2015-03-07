#!/bin/bash


NOW=$(date +"%m-%d-%Y:%l:%M")

echo $NOW

FILE="./old.html"
 
if [ -f $FILE ];
then
   curl -s http://www.eventbrite.com/e/asha-holi-stanford-2014-tickets-10693902751 > "latest.html"
   if `md5sum latest.html` -eq `md5sum old.html`; then
	echo "File has not changed"
   else
	echo "File changed"
   fi
   mv old.html archive.$NOW
   mv latest.html old.html
else
   #curl -s http://www.eventbrite.com/e/asha-holi-stanford-2014-tickets-10693902751 > "latest.html"
   echo "Something is wrong"
fi

curl -s http://www.eventbrite.com/e/asha-holi-stanford-2014-tickets-10693902751 > "latest.html"
