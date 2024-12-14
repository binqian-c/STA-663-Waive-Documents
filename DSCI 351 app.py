import streamlit as st
from pymongo import MongoClient
from neo4j import GraphDatabase


# Connect to MongoDB
client = MongoClient('mongodb://localhost:27017/')
db = client["project"]
collection = db["movie"]


# Search Movies function for genre with partial match
def search_movies(genre=None):
    query = {}
    if genre:
        regex_pattern = f".*{genre}.*"
        query["genre"] = {"$regex": regex_pattern, "$options": "i"}  # Case-insensitive
    results = collection.find(query, {"_id": 0})
    return list(results)


# Delete Movie function
def delete_movie(movie_name):
    if not movie_name:
        return 0  # Return 0 if no movie name provided
    regex_pattern = f"^{movie_name}$"
    query = {"title": {"$regex": regex_pattern, "$options": "i"}}
    result = collection.delete_one(query)
    return result.deleted_count


# Update Movie function
def update_movie(movie_name, update_data):
    regex_pattern = f"^{movie_name}$"
    query = {"title": {"$regex": regex_pattern, "$options": "i"}}
    update = {"$set": update_data}
    result = collection.update_one(query, update)
    return result.modified_count


# Insert Movie function
def insert_movie(movie_data):
    if not movie_data.get('title'):  # Checks if 'title' is empty or not provided
        return None  # Returns None if no movie name is provided
    # Check if the movie already exists in the dataset
    title = movie_data['title'].strip()
    regex_pattern = f"^{title}$"
    existing_movie = collection.find_one({"title": {"$regex": regex_pattern, "$options": "i"}})
    if existing_movie:
        return "Movie already exists"
    result = collection.insert_one(movie_data)
    return result.inserted_id


# Connect to Neo4j
URI = "neo4j://localhost:7687"
USER = "neo4j"
PASSWORD = "password"


class Neo4jConnection:
    def __init__(self, uri, user, password):
        self.__uri = uri
        self.__user = user
        self.__password = password
        self.__driver = None
        try:
            self.__driver = GraphDatabase.driver(self.__uri, auth=(self.__user, self.__password))
        except Exception as e:
            st.error(f"Failed to create the driver: {e}")

    def close(self):
        if self.__driver is not None:
            self.__driver.close()

    def query(self, query, parameters=None, db=None):
        assert self.__driver is not None, "Driver not initialized!"
        session = None
        response = None
        try:
            session = self.__driver.session(database=db) if db is not None else self.__driver.session()
            response = session.run(query, parameters)
            return [record for record in response]
        except Exception as e:
            st.error(f"Query failed: {e}")
        finally:
            if session is not None:
                session.close()


# Streamlit
def main():
    # system title
    st.title('Movie Recommendation System')
    # Search Movie
    with st.form("Search Movies by Genre"):
        genre_query = st.text_input("Enter movie genre")
        search = st.form_submit_button("Search")
    if search:
        results = search_movies(genre_query)
        if results:
            for movie in results:
                st.write(f"Name: {movie['title']}, Year: {movie['release_year']}, Duration: {movie['duration']}, Director: {movie['director']}, Country: {movie['country']}")
        else:
            st.write("No results found.")
    # Insert Movie
    with st.form("Insert Movie"):
        new_name = st.text_input("Movie name", key="new_name")
        new_duration = st.text_input("Duration", key="new_duration")
        new_year = st.number_input("Year", format="%d", step=1, key="new_year", value=None)
        new_director = st.text_input("Director", key="new_director")
        new_country = st.text_input("Country", key="new_country")
        new_genre = st.text_input("Genre", key="new_genre")
        insert = st.form_submit_button("Insert")
    if insert:
        if new_name:  # Check if the movie name is provided
            movie_data = {
                "title": new_name,
                "release_year": new_year,
                "duration": new_duration,
                "director": new_director,
                "country": new_country,
                "genre": new_genre
            }
            insertion_result = insert_movie(movie_data)
            if insertion_result:
                if insertion_result == "Movie already exists":
                    st.error("Movie already exists. Please enter a different name.")
                else:
                    st.success("Movie inserted successfully.")
            else:
                st.error("Failed to insert movie.")
        else:
            st.error("Please fill in the movie name to insert a new movie.")
    # Update Movie
    with st.form("Update Movie"):
        movie_name = st.text_input("Enter movie name to update")
        update_year = st.number_input("Update year", format="%d", step=1, min_value=1800, max_value=2100, key="update_year", value=None)
        update_duration = st.text_input("Update duration")
        update_director = st.text_input("Update director")
        update_country = st.text_input("Update country")
        update_genre = st.text_input("Update genre")
        update = st.form_submit_button("Update")
    if update:
        update_data = {}
        if update_year:
            update_data["release_year"] = update_year
        if update_duration:
            update_data["duration"] = update_duration
        if update_director:
            update_data["director"] = update_director
        if update_country:
            update_data["country"] = update_country
        if update_genre:
            update_data["genre"] = update_genre
        if update_movie(movie_name, update_data) > 0:
            st.success("Movie updated successfully.")
        else:
            st.error("No movie found to update.")
    # Delete Movie
    with st.form("Delete Movie"):
        delete_name = st.text_input("Enter movie name to delete", key="delete_name")
        delete = st.form_submit_button("Delete")
    if delete:
        if delete_movie(delete_name) > 0:
            st.success("Movie deleted successfully.")
        else:
            st.error("No movie found to delete.")

    # System Title
    st.title("Movie Rating System")
    # Search a Movie
    with st.form("Search Movie"):
        search_movie_title = st.text_input("Movie name")
        search = st.form_submit_button("search")
    if search and search_movie_title:
        conn = Neo4jConnection(URI, USER, PASSWORD)
        search_query = """
        MATCH (m:Movie)
        WHERE toLower(m.title) = toLower($title)
        RETURN m.title AS title, m.rating as rating, m.summary AS summary
        """
        search_params = {'title': search_movie_title}
        result = conn.query(search_query, parameters=search_params)
        conn.close()
        if result:
            record = result[0]
            st.subheader(f"Movie name: {record['title']}")
            st.write(f"Rating: {record['rating']}")
            st.write(f"Summary: {record['summary']}")
        else:
            st.error("No movie found with entered name.")
    # Update a Movie's Rating
    with st.form("Update Movie Rating"):
        update_movie_title = st.text_input("Movie name", key="modify")
        update_movie_rating = st.text_input("New rating (from 0 to 10, integer only)", key="new_rating")
        update = st.form_submit_button("update rating")
    if update and update_movie_title and update_movie_rating:
        try:
            rating_int = int(update_movie_rating)  # convert the rating to an integer
            if not (rating_int >= 0 and rating_int <= 10):  # check if rating is between 0 and 10
                st.error("The rating must be between 0 and 10.")
                rating_int = None
        except ValueError:
            st.error("The rating must be an integer. Please re-enter a number.")
            rating_int = None
        if rating_int is not None:
            conn = Neo4jConnection(URI, USER, PASSWORD)
            # Check if the movie exists
            check_query = "MATCH (m:Movie) WHERE toLower(m.title) = toLower($title) RETURN m"
            check_params = {'title': update_movie_title}
            check_result = conn.query(check_query, parameters=check_params)
            if check_result:  # If the movie name exits, update the rating
                update_query = """
                MATCH (m:Movie) WHERE toLower(m.title) = toLower($title)
                SET m.rating = $rating
                RETURN m.title AS title, m.rating AS rating
                """
                update_params = {'title': update_movie_title, 'rating': update_movie_rating}
                updated_result = conn.query(update_query, parameters=update_params)
                conn.close()
                if updated_result:
                    st.success("Movie rating updated successfully.")
                else:
                    st.error("Failed to update rating. Please check the query or database connection.")
            else:
                conn.close()
                st.error(f"No movie found with the name '{update_movie_title}'. Cannot update rating.")
    else:
        if update:
            if not update_movie_rating:
                st.error("Please enter a rating number.")
            if not update_movie_title:
                st.error("Please enter a movie name to update rating.")
    # Insert a New Movie
    with st.form("Add Movie"):
        st.caption("Please ensure that all fields are filled in.")
        add_movie_title = st.text_input("Movie name", key="add_title")
        add_movie_rating = st.text_input("Rating (from 0 to 10, integer only)", key="add_rating")
        add_movie_summary = st.text_area("Summary", key="add_summary")
        add_movie = st.form_submit_button("add")
    if add_movie:
        if add_movie_title and add_movie_rating and add_movie_summary:
            try:
                rating_int = int(add_movie_rating)  # convert the rating to an integer
                if not (rating_int >= 0 and rating_int <= 10):  # check if rating is between 0 and 10
                    st.error("The rating must be between 0 and 10.")
                    rating_int = None
            except ValueError:
                st.error("The rating must be an integer. Please re-enter a number.")
                rating_int = None
            if rating_int is not None:
                conn = Neo4jConnection(URI, USER, PASSWORD)
                # Check if the entered movie already exists
                check_query = "MATCH (m:Movie) WHERE toLower(m.title) = toLower($title) RETURN m"
                check_params = {'title': add_movie_title}
                check_result = conn.query(check_query, parameters=check_params)
                if not check_result:  # If the movie does not exist, create new movie and director relationships
                    add_query = """
                    CREATE (m:Movie {title: $title, rating: $rating, summary: $summary})
                    RETURN m.title AS title, m.rating AS rating, m.summary AS summary
                    """
                    add_params = {
                        'title': add_movie_title,
                        'rating': add_movie_rating,
                        'summary': add_movie_summary
                    }
                    conn.query(add_query, parameters=add_params)
                    conn.close()
                    st.success("New movie added successfully.")
                else:
                    conn.close()
                    st.error(f"'{add_movie_title}' already exists.")
        else:
            if add_movie:  # Check if all fields are filled
                if not add_movie_title:
                    st.error("Please enter the movie name.")
                if not add_movie_rating:
                    st.error("Please enter the your rating.")
                if not add_movie_summary:
                    st.error("Please enter a brief summary of the movie.")
    # Delete a Movie
    with st.form("Delete A Movie"):
        delete_movie_title = st.text_input("Movie name", key="delete_title")
        delete = st.form_submit_button("delete")
    if delete and delete_movie_title:
        conn = Neo4jConnection(URI, USER, PASSWORD)
        # Check if the movie exists first
        check_query = "MATCH (m:Movie) WHERE toLower(m.title) = toLower($title) RETURN m"
        check_params = {'title': delete_movie_title}
        check_result = conn.query(check_query, parameters=check_params)
        if check_result:  # If movie exists, proceed with deleting the movie
            delete_query = "MATCH (m:Movie) WHERE toLower(m.title) = toLower($title) DELETE m"
            delete_params = {'title': delete_movie_title}
            conn.query(delete_query, parameters=delete_params)
            st.success(f"'{delete_movie_title}' has been deleted.")
        else:
            st.error(f"No movie found with the name '{delete_movie_title}'. Cannot delete.")


if __name__ == "__main__":
    main()
