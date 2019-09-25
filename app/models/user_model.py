from database import DatabaseConnection
import datetime
connection = DatabaseConnection()
response = []


class UserModel():
    @staticmethod
    def register_user(full_name, email, username, password, date_created, date_modified):
        """
        This method registers a user
        :param name:
        :param email:
        :param username:
        :param password:
        """
        try:
            query_to_check_for_username = "SELECT * FROM users WHERE username=%s"
            connection.cursor.execute(query_to_check_for_username, [username])
            row_username = connection.cursor.fetchone()

            query_to_check_for_email = "SELECT * FROM users WHERE email=%s"
            connection.cursor.execute(query_to_check_for_email, [email])
            row_email = connection.cursor.fetchone()
            if not (row_username or row_email):
                register_user_query = "INSERT INTO users(name, email, username, password, date_created, date_modified) VALUES (%s, %s, %s, %s, %s, %s)"
                connection.cursor.execute(register_user_query, [
                                          full_name, email, username, password, date_created, date_modified])

                query_to_check_for_inserted_user = "SELECT * FROM users WHERE username=%s"
                connection.cursor.execute(
                    query_to_check_for_inserted_user, [username])
                row = connection.cursor.fetchone()
                if not row:
                    return "No results to fetch"
                response = {
                    'id': row[0],
                    'name': row[1],
                    'email': row[2],
                    'username': row[3],
                    'password': row[4]
                }
                return response
            return "Email or username already exists"
        except Exception as exc:
            print(exc)

    @staticmethod
    def check_if_is_valid_user(username):
        """
        This method logs in a user
        :param username: 
        :param password: 
        :return: 
        """
        try:
            query_to_check_for_user = "SELECT * FROM users WHERE username=%s"
            connection.cursor.execute(query_to_check_for_user, [username])
            row = connection.cursor.fetchone()
            if not row:
                return "user not found"
            return row
        except Exception as exc:
            print(exc)
