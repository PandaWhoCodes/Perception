# What ?
Perception is an app that tries to get the first thoughts a user had about a word/image.
The user will be given several words, and for each word the user has to enter word(s) that come to his/her mind. 

This can be a Android/Web/Electron/ or sometihng thats made from blockly.
**You can reuse the entire backend code, or write one yourself.**

# Main Screen:

-   On selecting a topic, a screen with an image (with a phrase/word) and space to input text will be shown.
    
-   A 10 sec timer will be shown to the user and at the bottom, three buttons: submit, skip & end, will be there.
    
-   Once the timer runs out, the next word will be shown automatically. Words entered by the user will be saved.
            
-   End button leads to result(shows your inputs)

**EXTRA: Based on API and data provided, it will show the % of others who chose the same words as the user for a given word.**

# How to run?
- Install requirements from requirements.txt
- Run your local sql server
- Create a db (mysql) if you do not have one already
- Change the credentials in db_secrets.py if you have to.
- Run create_db.py to create the tables in your database.
- Run app.py to start the API