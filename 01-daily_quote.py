#!/usr/bin/env python3
"""
Daily Quote Generator

This script selects a random quote for the day and prints it. Optional: The same quote should be generated for a given day.

Your task:
1. Complete the get_quote_of_the_day() function
2. Set up a cron job to run this script daily at 8:00 AM and append the output to a file

Hint: Look up `random.choice()` to select a random item from a list. You can use the `date` module to get the current date and set a seed for the random number generator.
"""

# import Python's built-in random module to generate random numbers/selections
import random 
from datetime import date

# create a list of quotes to choose from
quotes = [
    "The only way to do great work is to love what you do.",
    "It does not matter how slowly you go, as long as you do not stop.",
    "Success is not final, failure is not fatal: It is the courage to continue that counts.",
    "Believe you can and you're halfway there.",
    "You don’t have to be great to start, but you have to start to be great.",
    "Thousands of candles can be lit from a single candle, and the life of the candle will not be shortened. Happiness never decreases by being shared.",
    "Challenges are what make life interesting, and overcoming them is what makes life meaningful.",
    "Every morning we are born again. What we do today is what matters most.",
    "The mind is everything. What you think, you become.",
    "In the end, only three things matter: how much you loved, how gently you lived, and how gracefully you let go of things not meant for you."
]

# define a function called "get_quote_of_the_day" that pulls from the list of quotes
# random.choice() selects a random quote from the list
def get_quote_of_the_day(quotes):
    todays_quote = random.choice(quotes)

    return todays_quote

if __name__ == "__main__":
    print(get_quote_of_the_day(quotes))

# Cron job (add this to your crontab):
# 0 8 * * * /usr/bin/python3/workspaces/03-data-structures-erica892/01-daily_quote.py >> //workspaces/03-data-structures-erica892/daily_quote.txt
