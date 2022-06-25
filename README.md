# Workout_Tracker
This is a workout tracker that uses the nutritionix API and NLP to process raw input and organize it into a workout sheet.
The code is fully written in Python3, so make sure to have it installed before you run the code

# Create your account and get API_KEY and APP_ID 
use https://www.nutritionix.com/business/api to create free or paid account and get your API_KEY and APP_ID 
Both variables should be saved as enviromental variables for your own security 
the folowing command can be used in your Bash console 

```bash
$ export APP_ID=YOUR_APP_ID
```

# Create your workout sheet using sheety
use https://sheety.co/ to get your own excersise sheet, it can be connected to your Google account 
save the url of your sheet under sheet_endpoint

# Authentication 
finally, this app uses bearer authentication
this can be accessed and setup by following the sheety guide on authentication https://sheety.co/docs/authentication.html
then the module os can be used to acess enviromental variables using the environ.get() function 
