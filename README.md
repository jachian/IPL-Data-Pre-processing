# IPL-Data-Pre-processing
Scripts for pre-procssing IPL data

In line with the requirements above, the CRICSHEET datasets of ball by ball match coverage was used for this project. These datasets are available at https://cricsheet.org/downloads/  as both yaml and cvs files. Specifically, the Indian Premier League (IPL) dataset was applied to this project (https://cricsheet.org/downloads/ipl_csv_male.zip).
The IPL dataset is presented as a zipped file containing a number of CSV files. Each CSV file contains the data for a single match, starting with the general match, venue and toss information followed by at least 240 rows of play data. Each row contains the data about a single ball/bowling event with the following fields:
•	The word 'ball' to identify it as such
•	Innings number, starting from 1
•	Over and ball
•	Batting team name
•	Batsman
•	Non-striker
•	Bowler
•	Runs-off-bat
•	Extras
•	Kind of wicket, if any
•	Dismissed played, if there was a wicket
A minimum of 50 CSV sheets from a single zipped file were used to build our visualisations. Each CSV representing a single match.

Iteration # 1 - The first iteration of data preparation involved collating all of the 50 CSV match documents into a single CSV that could be loaded into Spotfire to begin preliminary data visualization and exploration. This process not only involved concatenation of the 50 CSVs but also reformatting of the data rows to enforce data type consistency across column values.
Iteration # 2 - During the initial data exploration and visualization some difficulties were discovered in visualizing certain columns of categorical data. A second transformation was required to convert key categorical columns like 'Wicket', which holds a categorical string if a wickets as taken, into a numeric value. With the 'Wicket' example, the current wicket column was made to hold the numeric value '1' if a wicket was taken or '0' if no wicket was taken. An additional column labeled 'Wicket_type' was used to hold the categorical data previously held in the wicket column.
