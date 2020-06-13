### Anagrams
​
Given a file containing a list of words, write a program which takes a single word
as a command line argument and outputs all the anagrams of this word in the list to 
standard output.  Do not output the original word if it is present.  
​
**Example:**
​
Wordlist file:
```
alerting
altering
hacks
integral
post
pots
relating
shack
spot
stop
tops
triangle
```
​
Usage:
​
```
$ ./anagrams hacks
shack
​
$ ./anagrams altering
alerting
integral
relating
triangle
```
​
**Challenge:** do the same thing but look for multiple word anagrams for a multiple word input -
ex. "Clint Eastwood" -> "Old West Action"
