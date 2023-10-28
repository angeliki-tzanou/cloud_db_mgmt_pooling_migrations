### Connection to Azure and GCP:
- First logged into the platform (this case Azure or GCP)
- Then navigated to the MySQL databases tab and created an instance
  - We chose all the options that would minimize the cost per day
  - Also ensured that within those options, in the Networking tab, we added the IP address of 0.0.0.0/0 to ensure that it is public to all for the purpose of this assignment
- After deploying both MySQLs within both platforms we ensured that the appropriate pool size and timeout settings fit the requirements.
### Database Schema:
- Opening the environment we chose to work on (in this case Google Cloud Shell) we cloned the repo we wanted to store all the information in.
- Then we would ensure that we can connect and access our database through Google Shell by using the command ``` mysql -u _username_ -h _host(IP-address)_ -p```
- The next step starting with Azure was to create the database schema 
- Created an ```azure.py``` file were we store all of the code including the schema of our tables
- Within our code we ensured that we had the command line for authorizing access when provided with the correct information ```engine = create_engine("mysql+pymysql://username:password@host/databasename",
                         connect_args={'ssl': {'ssl-mode': 'preferred'}},
                         )```
    - We can ensure that we connected to our database accurately by using the commands ```inspector = inspect(engine) & inspector.get_table_names()``` and we get as a result an empty [] it would mean that it displays our empty database without any table since we have not run the code of the tables yet. After doing so it should also display the tables created.
      <img width="1000" alt="Screenshot 2023-10-27 at 2 25 37 PM" src="https://github.com/angeliki-tzanou/cloud_db_mgmt_pooling_migrations/assets/141374140/30d231e4-a9ed-4086-8a89-875d687a1588">

- We can log into our MySQL by using the command above in our terminal, then from there pick the database we want to use (that we have previously created through Azure and GCP platform) through the ```use _databasename_;```
- Then we can see the tables being successfully created by running ```show tables;```
<img width="953" alt="Screenshot 2023-10-27 at 5 24 01 PM" src="https://github.com/angeliki-tzanou/cloud_db_mgmt_pooling_migrations/assets/141374140/1ad4dfd3-ed05-4415-bde3-9a0797a567eb">

### Workbench MySQL to Generate ERD:
- Then to proceed and connect our Azure and GCP with the workbench
- We create an instance and fill in the information based on the ones included in our database setup for each like the images shown below:
  
  <img width="700" alt="Screenshot 2023-10-27 at 3 55 46 PM" src="https://github.com/angeliki-tzanou/cloud_db_mgmt_pooling_migrations/assets/141374140/114ea448-641e-458f-83a3-f97e8d2cc2b4">
  <img width="700" alt="Screenshot 2023-10-27 at 3 56 20 PM" src="https://github.com/angeliki-tzanou/cloud_db_mgmt_pooling_migrations/assets/141374140/1aa2fb0d-1de8-4854-a8e0-233beec0825a">
- Then we repeat the same steps for GCP as well:
 <img width="609" alt="Screenshot 2023-10-27 at 5 59 27 PM" src="https://github.com/angeliki-tzanou/cloud_db_mgmt_pooling_migrations/assets/141374140/ef4e74bf-bbb8-4348-8c9d-541427fab436">
<img width="833" alt="Screenshot 2023-10-27 at 5 59 20 PM" src="https://github.com/angeliki-tzanou/cloud_db_mgmt_pooling_migrations/assets/141374140/ca97121d-1b2c-40bd-b0db-5141b7e7cc35">

- Then we can go ahead and create our ERD for each as also shown below:
  
<img width="1000" alt="Screenshot 2023-10-27 at 6 00 23 PM" src="https://github.com/angeliki-tzanou/cloud_db_mgmt_pooling_migrations/assets/141374140/b939ec8e-4641-418a-8f8c-f5eed3f95d97">

<img width="1000" alt="Screenshot 2023-10-27 at 3 53 47 PM" src="https://github.com/angeliki-tzanou/cloud_db_mgmt_pooling_migrations/assets/141374140/c5809909-1bb1-44d1-b798-a9f48ea48d75">

### SQL Alchemy & FLask Integration:
- While trying to create a Flask application that would rely on the information of the tables that were provided in the databases already, I ran into a couple of issues:
- First, when trying to create a simple flask application code which included the app.py, & the html file, the flask app would not deploy after trying multiple templates of codes and changing the whole structure of the application
- The error message shown below was being shown persistently:
<img width="1000" alt="Screenshot 2023-10-27 at 8 30 36 PM" src="https://github.com/angeliki-tzanou/cloud_db_mgmt_pooling_migrations/assets/141374140/05e4cd36-c716-49ed-86dc-df3e9a26e057">

### Database Migrations with Alembic:
- Running the following commands in the terminal should ensure a seamless migration connection with both databases
- First, we would run simply ```alembic```
- Then would run ```alembic init migrations```
- Then in order to authorize and edit the alembic.ini to point to our database
```sqlalchemy.url = mysql+mysqlconnector://username:password@host/database_name```
- Then within our env.py file that was automatically generated we should go back in there and use the following ```from db_schema import Base``` ```target_metadata = Base.metadata```
- Then we can create a migration by using the following command and running it in our terminal ```alembic revision --autogenerate -m "create tables"```
- By running that command it should autogenerate a file for each table autogenerated as pictured below:
  
<img width="279" alt="Screenshot 2023-10-27 at 10 18 32 PM" src="https://github.com/angeliki-tzanou/cloud_db_mgmt_pooling_migrations/assets/141374140/7afbcc53-c756-44eb-bde3-084327689f0c">




  

