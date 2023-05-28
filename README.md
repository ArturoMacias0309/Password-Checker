# Most Secure Password Checker Program With Python

## Password checker created using the API for https://haveibeenpwned.com/

The reason this password checker is the most secure option, is because of the way the API works. It works by taking in a hashed, 5 character version of your password using SHA1.
This prevents users from sending a password in plain text to the API, which can be intercepted by a hacker.
The program then sends that 5 character version of your password (also knowing the last 5 characters) to the API and looks for it in the database.
Once it finds a password with the exact same starting and ending characters (your password), it will let you know how many times it has been found in a data breach.
