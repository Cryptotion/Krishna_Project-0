import sqlite3

# Define database
db_name = 'revhire.db'

#Define table

create_user_table = """ CREATE TABLE user(
                        user_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(20),
                        email VARCHAR(20) UNIQUE,
                        password VARCHAR(20) NOT NULL,
                        role VARCHAR(20)
    )"""

create_employ_table =  """
                        CREATE TABLE EMPLOYEER(
                        emp_id INTEGER PRIMARY KEY AUTOINCREMENT,
                        name VARCHAR(25), 
                        email VARCHAR(20) UNIQUE,
                        password VARCHAR(20) NOT NULL,
                        role VARCHAR(20)
    )"""

create_job_table = """ CREATE TABLE jobpost( 
                        job_id INTEGER PRIMARY KEY AUTOINCREMENT, 
                        title VARCHAR(20), 
                        company VARCHAR(20), 
                        discription VARCHAR(20), 
                        skill VARCHAR(20), 
                        emp_id INTEGER NOT NULL,
                        FOREIGN KEY (emp_id) REFERENCES EMPLOYEER(emp_id) )"""

create_application_table = """ CREATE TABLE application(
                                app_id INTEGER PRIMARY KEY AUTOINCREMENT,
                                user_id INTEGER NOT NULL,
                                job_id INTEGER NOT NULL,
                                status TEXT,
                                resume_link TEXT UNIQUE,
                                FOREIGN KEY (user_id) REFERENCES user(user_id)
                                FOREIGN KEY (job_id) REFERENCES job(job_id)
)"""

# con = sqlite3.connect('D:/Revanture/trng-1903-1904/week-1/Project-0/revhire.db')
con = sqlite3.connect(db_name)

cursor = con.cursor()


cursor.execute(create_job_table)
cursor.execute(create_user_table)
cursor.execute(create_employ_table)
cursor.execute(create_application_table)

con.commit()

con.close()