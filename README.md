# Deimos AI Bot 
###  This is a bot deployable to platforms ranging from Telegram, Slack and also discord

To run the program:

````bash
Poetry init $$ poetry shell
````

Concat requirements.txt to poetry and add :  

````bash
cat requirements.txt | xargs poetry add

````

or: 

````bash

poetry add $(cat requirements.txt)

````
install dependencies:
````bash
Poetry install
````

Then install package dependencies:
````bash
Python bot.py
````


#### Config.json contains the target deployment platform config credentials

#### Services contains different AI services implemented to help automate chat flow

#### Cogs file contains the discord bot implementation

