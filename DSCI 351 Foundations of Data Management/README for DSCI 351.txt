THE MOVIE MANAGEMENT SYSTEM
// The following steps are operated on Mac

File Introduction
1. In the "MongoDB files" folder:
"movie_storage.csv" is the dataset we used in MongoDB database.
"load_mongo.py" is the python file to load data in the csv file into MongoDB.
2. In the "Neo4j files" folder:
"movie_nodes.csv" is the movie data we used in Neo4j.
"director_nodes.csv" is the director data we used in Neo4j.
"relationships.csv" is the relationship file that connects the movie nodes and director nodes in Neo4j.
3. In the main directory:
"app.py" includes all the codes of design of our application.



Implementation:
Use PyCharm to run the application, please put all files in the google drive into the same directory (move the files in "MongoDB files" and "Neo4j files" folders out and put all files under the same directory level)
Please install all the needed packages in Pycharm: use commands "pip install streamlit", "pip install pymongo", "pip install neo4j", "pip install pandas"

1. Load Data into MongoDB database
> Download Studio 3T for MongoDB data visualization.
> Use the command "python3 load_mongo.py movie_storage.csv" in the Pycharm terminal to load the data in movie_storage.csv file into MongoDB database.
2. Load Data into Neo4j database
> Download Neo4j Desktop for Neo4j data visualization.
> Put the files "movie_nodes.csv", "director_nodes.csv", and "relationships.csv" into IMPORT folder in Neo4j Desktop
> Open Neo4j Browser in Neo4j Desktop.
> If there are data already loaded into Neo4j, please use the command "MATCH (n) DETACH DELETE n" to drop data first.
> Use command "LOAD CSV WITH HEADERS FROM 'file:///director_nodes.csv' AS row MERGE (d:Director {name: row.director})" to load director data into Neo4j.
> Use command 
"LOAD CSV WITH HEADERS FROM 'file:///movie_nodes.csv' AS row
CREATE (m:Movie {
title: row.title,
releaseYear: toInteger(row.release_year),
country: row.country,
duration: row.duration,
rating: toInteger(row.rating),
genre: row.listed_in,
summary: row.description})"
to load movie data into Neo4j.
> Use command 
"LOAD CSV WITH HEADERS FROM 'file:///relationships.csv' AS row
MATCH (d:Director {name: row.director})
MATCH (m:Movie {title: row.title})
MERGE (d)-[:DIRECTED]->(m)"
to connect movie nodes with director nodes in Neo4j.
3. Run the application (be sure to keep Studio 3T and Neo4j Desktop opened)
> After successfully loading the data into the databases, go back to Pycharm and run the "app.py" file.
> Open the Pycharm terminal and use command "streamlit run app.py" to run the web-browser GUI
4. You can now interact with our application!


