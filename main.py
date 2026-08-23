import pandas as pd
import sqlite3


##### Part 1: Basic Filtering #####

# Create the connection
# Note the connect is 'conn1' since there will be multiple .db used
conn1 = sqlite3.connect('planets.db')

# Select all
pd.read_sql("""
SELECT * FROM planets;
""", conn1)


# STEP 1
# Return all columns for planets that have 0 moons
df_no_moons = pd.read_sql("""
SELECT *
FROM planets
WHERE num_of_moons = 0;
""", conn1)


# STEP 2
# Return the name and mass of planets with exactly 7 letters
df_name_seven = pd.read_sql("""
SELECT name, mass
FROM planets
WHERE LENGTH(name) = 7;
""", conn1)


##### Part 2: Advanced Filtering #####

# STEP 3
# Return name and mass for planets with mass less than or equal to 1.00
df_mass = pd.read_sql("""
SELECT name, mass
FROM planets
WHERE mass <= 1.00;
""", conn1)


# STEP 4
# Return all columns for planets with at least one moon and mass less than 1.00
df_mass_moon = pd.read_sql("""
SELECT *
FROM planets
WHERE num_of_moons >= 1
AND mass < 1.00;
""", conn1)


# STEP 5
# Return name and color for planets containing "blue" in their color
df_blue = pd.read_sql("""
SELECT name, color
FROM planets
WHERE color LIKE '%blue%';
""", conn1)


##### Part 3: Ordering and Limiting #####

# Create a connection
# Note the connect is 'conn2' since there will be multiple .db used
conn2 = sqlite3.connect('dogs.db')

# Select all
pd.read_sql("""
SELECT * FROM dogs;
""", conn2)


# STEP 6
# Return hungry dogs from youngest to oldest
df_hungry = pd.read_sql("""
SELECT name, age, breed
FROM dogs
WHERE hungry = 1
ORDER BY age ASC;
""", conn2)


# STEP 7
# Return hungry dogs between ages 2 and 7, sorted alphabetically
df_hungry_ages = pd.read_sql("""
SELECT name, age, hungry
FROM dogs
WHERE hungry = 1
AND age BETWEEN 2 AND 7
ORDER BY name ASC;
""", conn2)


# STEP 8
# Return the 4 oldest dogs
df_4_oldest = pd.read_sql("""
SELECT name, age, breed
FROM dogs
ORDER BY age DESC
LIMIT 4;
""", conn2)


##### Part 4: Aggregation #####

# Create a connection
# Note the connect is 'conn3' since there will be multiple .db used
conn3 = sqlite3.connect('babe_ruth.db')

# Select all
pd.read_sql("""
SELECT * FROM babe_ruth_stats;
""", conn3)


# STEP 9
# Return total number of years Babe Ruth played
df_ruth_years = pd.read_sql("""
SELECT COUNT(year)
FROM babe_ruth_stats;
""", conn3)


# STEP 10
# Return total number of home runs
df_hr_total = pd.read_sql("""
SELECT SUM(HR)
FROM babe_ruth_stats;
""", conn3)


##### Part 5: Grouping and Aggregation #####

# STEP 11
# Return each team and number of years played
df_teams_years = pd.read_sql("""
SELECT team, COUNT(year) AS number_years
FROM babe_ruth_stats
GROUP BY team;
""", conn3)


# STEP 12
# Return teams with an average of more than 200 at-bats
df_at_bats = pd.read_sql("""
SELECT team, AVG(at_bats) AS average_at_bats
FROM babe_ruth_stats
GROUP BY team
HAVING AVG(at_bats) > 200;
""", conn3)


# STEP 13
# Close all connections
conn1.close()
conn2.close()
conn3.close()