### Request Statistics
​
Write a program that reads a list of URLS (either from standard input or from a file)
For each URL, make a GET request and capture the number of bytes and approximate amount
 of time between request and response.  If the server returns a redirect, follow it and 
 try again. 
​
Output should be of the form:
​
`<input url> <response code> <number of bytes in response> <time>`
​
EX: for an input
```
https://www.google.com/
https://www.netflix.com/
https://www.google.com/this/should/be/a/404
```
​
Should be something like:
```
https://www.google.com/ 200 12110 0.109727
https://www.netflix.com/ 200 415487 0.530711
https://www.google.com/this/should/be/a/404 404 1581 0.093909
```
​
Bonus sub-problem:
​
- Parallelize the requests such that a few slow pages don't slow down the process as much
- Bonus: detect if there is a looping redirect
- Add an HTTP endpoint that shows statistics (ex. latency histogram)
