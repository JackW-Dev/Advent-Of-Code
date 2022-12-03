#!/bin/bash

sumPlayerOne=0
sumPlayerTwo=0

while read -r playerOne playerTwo; do
  if [ "$playerOne" == 'A' ]; then
    if [ "$playerTwo" == 'X' ]; then 
      ((sumPlayerOne+=4))
      ((sumPlayerTwo+=3))
    elif [ "$playerTwo" == 'Y' ]; then
      ((sumPlayerOne+=8))
      ((sumPlayerTwo+=4))
    else
      ((sumPlayerOne+=3))
      ((sumPlayerTwo+=8))
    fi
  elif [ "$playerOne" == 'B' ]; then
    if [ "$playerTwo" == 'X' ]; then
      ((sumPlayerOne+=1))
      ((sumPlayerTwo+=1))
    elif [ "$playerTwo" == 'Y' ]; then
      ((sumPlayerOne+=5))
      ((sumPlayerTwo+=5))
    else
      ((sumPlayerOne+=9))
      ((sumPlayerTwo+=9))
    fi
  elif [ "$playerOne" == 'C' ]; then
    if [ "$playerTwo" == 'X' ]; then
      ((sumPlayerOne+=7))
      ((sumPlayerTwo+=2))
    elif [ "$playerTwo" == 'Y' ]; then
      ((sumPlayerOne+=2))
      ((sumPlayerTwo+=6))
    else
      ((sumPlayerOne+=6))
      ((sumPlayerTwo+=7))
    fi
  fi
done < input.txt

echo Part A: "$sumPlayerOne"
echo Part B: "$sumPlayerTwo"