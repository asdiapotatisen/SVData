# SVUserData
## Functions
### Get Data
Get Data is the most basic mode. It retrieves data by scraping SVIDs from spookvooper.com and then feeds it through the SpookVooper API to get the user data. The process is quite long, taking an average of 10 to 15 minutes. That is why it is recommended you only retrieve data daily, as the information retrieved would be fairly accurate for general searching.

Do take note that two files, database.json and svidlist.txt, will be created in the same directory as where the .exe file is. Do NOT delete database.json as the other modes rely on it to function. svidlist.txt is just there so you can easily access a list of SVIDs should you need it.

### Search
Search is by far the most useful mode. It searches through database.json and finds all suitable results based on your 6 inputs: 
* output type
* key
* operation
* value
* date
* filter (True by default)

These inputs can be put into the following sentence:

Find all [output type] such that [key] [operator] [value] on [date (DD-MM-YYYY)].

For example, "Find all [username] such that [credits] [is less than] [100000] on [14-11-2020].

### Compare
Compare is used to get a list from two lists, based on your mode (operation). There are 3 inputs:

* input type
* mode (operation)
* output type

Input type is the type of your two inputs; both inputs must be the same. 

Mode (operation) is how you want to filter both lists. There are 3 modes: AND, OR and XOR.

AND returns a list of elements such that all elements can be found in both input lists.

| Input 1 | Input 2 | Output |
| --- | --- | --- |
|     0     |     0     |     0     |
|     1     |     0     |     0     |
|     0     |     1     |     0     |
|     1     |     1     |     1     |

OR returns a list of elements such that all elements can be found in at least one input list.

| Input 1 | Input 2 | Output |
| --- | --- | --- |
|     0     |     0     |     0     |
|     1     |     0     |     1     |
|     0     |     1     |     1     |
|     1     |     1     |     1     |

XOR returns a list of elements such that all elements can only be found in exactly one input list.

| Input 1 | Input 2 | Output |
| --- | --- | --- |
|     0     |     0     |     0     |
|     1     |     0     |     1     |
|     0     |     1     |     1     |
|     1     |     1     |     0     |
        
Output type is the type you want the output to be.
## Future Updates
* Save searches as text files, use in Compare
* Add multiple search fields at once
* Regex query for values
