# Unstandard .txt file parser

*This program is my new trying on GUI progame*

## Description

Recently, I am so addicted to the game developed by NetEase named 梦幻西游. However, the 'golden coins' ( currency in the game) really take time to obtain, unless you **MAKE in-app PURCHASE**, which is so not ideal for me since I am just a student still hunting for a job. So the usual solution is create multiple roles in the game and run the game simultaneously, then transfer the money to the main role. 

By using some assistance software which will help to do the daily activities automatically, I can obtain some **小号**. The problem is the recording system of the software. The format they record the account information is for example:

*min****@**.com|shan2046 名扬万里 逍遥生 大唐官府 62 82170*

As you can see, the format is not convenient using Numbers to open since there exists '|' (wtf? Why you decide to use '|' instead of like following components who just use a whitespace? )

So my target is to have a software that can modify the format into:

*min****@**.com shan2046 名扬万里 逍遥生 大唐官府 62 82170*

And add a header:

*Account password server subserver roletype skills levels balance*

Then finally, exprot the file as .csv file.

In the meantime, the program will also generate a log file so it will keep tracking on all the activities.



