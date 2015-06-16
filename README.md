<<<<<<< HEAD
# README #

This file explains all steps that are necessary to get our
scrapper of bet ratios and match results up and running.

It consists of a Python script that fetches results of matches
and bet information (from http://www.mackolik.com/Genis-Iddaa-Programi)

Scrapped data is stored to a MySQL database, and bet results are calculated
automatically.

The scrapper should be set up as a continuous cronjob to keep the data up-to-date.

### What is this repository for? ###

* Quick summary
* Version

### How do I get set up? ###

* Summary of set up
* Configuration


* Dependencies


* Database configuration

Once MySQL is installed, the following user must be created:
user: 'sportbets'@'localhost'
password: sportbets

subsequently run

mysql -u root -proot < db_schema.sql

this will create a database with all required tables and triggers

* Set up cronjob

as root run
`crontab -e`

then add the following line, save and exit:

`*/5 * * * * /home/sportbets/scrapebets.sh`


* How to run tests
* Deployment instructions

### Contribution guidelines ###

* Writing tests
* Code review
* Other guidelines

### Who do I talk to? ###

* Repo owner or admin
* Other community or team contact
=======
# iddaa-bets
>>>>>>> 42415ecefbf68924c7b7abf0c63a147e0c0ec4cf
