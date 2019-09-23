import psycopg2
from flask import Flask

import os

class DatabaseConnection():
    def __init__(self):
        """
        This constructor creates a connection to the database
        :param dbname: 
        :param user: 
        :param password: 
        :param host: 
        :param port: 
        """

        self.conn_params = dict(
            user=os.getenv("USER"),
            password=os.getenv("PASSWORD"),
            host=os.getenv("HOST"),
            port=os.getenv("PORT"),
            database=os.getenv("DATABASE"),
        )
        if os.environ.get('APP_SETTINGS') == 'production':
            self.connection = psycopg2.connect(os.environ.get("DATABASE_URL"))
        else:
            self.connection = psycopg2.connect(dbname=self.conn_params['database'], user=self.conn_params['user'],
                                               password=self.conn_params['password'], port=self.conn_params['port'],
                                               host=self.conn_params['host'])
        self.connection.autocommit = True
        self.cursor = self.connection.cursor()

    def create_tables(self):
        """ This method creates all tables"""
        create_table_query_for_user = (
            """ CREATE TABLE IF NOT EXISTS 
                users(
                    user_id SERIAL PRIMARY KEY NOT NULL,
                    name VARCHAR(50) NOT NULL,
                    email VARCHAR (50) UNIQUE,
                    username VARCHAR(20) UNIQUE,
                    password VARCHAR(100) NOT NULL,
                    date_created TIMESTAMP, 
                    date_modified TIMESTAMP
                    );"""
        )

        create_table_query_for_role = (
            """
            CREATE TABLE IF NOT EXISTS
            role(
                role_id SERIAL PRIMARY KEY NOT NULL,
                role_name VARCHAR(30) NOT NULL,
                user_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(user_id)
                ON DELETE CASCADE ON UPDATE CASCADE
            )
            """
        )

        create_table_query_for_tel_numbers = (
            """
            CREATE TABLE IF NOT EXISTS
            tel_numbers(
                tel_id SERIAL PRIMARY KEY NOT NULL,
                user_id INTEGER,
                tel_number VARCHAR(20) NOT NULL,
                FOREIGN KEY(user_id) REFERENCES users(user_id)
                ON DELETE CASCADE ON UPDATE CASCADE
            )
            """
        )

        create_table_query_for_packages = (
            """
            CREATE TABLE IF NOT EXISTS
            packages(
                package_id SERIAL PRIMARY KEY NOT NULL,
                package_name VARCHAR(100) NOT NULL,
                date_created TIMESTAMP,
                date_modified TIMESTAMP,
                user_id INTEGER,
                FOREIGN KEY(user_id) REFERENCES users(user_id)
                ON DELETE CASCADE ON UPDATE CASCADE
            )
            """
        )

        create_table_query_for_loading_types  = (
            """
            CREATE TABLE IF NOT EXISTS
            loading_types(
                loading_type_id SERIAL PRIMARY KEY NOT NULL,
                loading_type VARCHAR(20) NOT NULL,
                package_id INTEGER,
                FOREIGN KEY (package_id) REFERENCES packages(package_id)
                ON DELETE CASCADE ON UPDATE CASCADE
            )
            """
        )

        create_table_query_for_location = (
            """
            CREATE TABLE IF NOT EXISTS
            location(
                location_id SERIAL PRIMARY KEY NOT NULL,
                package_id INTEGER,
                location_name VARCHAR(50) NOT NULL,
                FOREIGN KEY(package_id) REFERENCES packages(package_id)
                ON DELETE CASCADE ON UPDATE CASCADE
            )
            """
        )

        create_table_query_for_delivery_times=(
            """
            CREATE TABLE IF NOT EXISTS
            delivery_times(
                delivery_time_id SERIAL PRIMARY KEY NOT NULL,
                delivery_time VARCHAR(20) NOT NULL,
                location_id INTEGER,
                FOREIGN KEY(location_id) REFERENCES location(location_id)
                ON DELETE CASCADE ON UPDATE CASCADE
            )
            """
        )


        # Execute creating tables
        self.cursor.execute(create_table_query_for_user)
        self.cursor.execute(create_table_query_for_role)
        self.cursor.execute(create_table_query_for_tel_numbers)
        self.cursor.execute(create_table_query_for_packages)
        self.cursor.execute(create_table_query_for_loading_types)
        self.cursor.execute(create_table_query_for_location)
        self.cursor.execute(create_table_query_for_delivery_times)

    # Remove all the records from the table
    def drop_table(self, table_name):
        """
        This method truncates a table
        :param table_name:
        :return:
        """
        self.cursor.execute("TRUNCATE TABLE {} RESTART IDENTITY CASCADE"
                            .format(table_name))
