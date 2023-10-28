### Connection to Azure and GCP:
- First logged into the platform (this case Azure or GCP)
- Then navigated to the MySQL databases tab and created an instance
  - We chose all the options that would minimize the cost per day
  - Also ensured that within those options, in the Networking tab we added the IP address of 0.0.0.0/0 to ensure that its public to all for the purpose of this assignment
- After deploying both MySQLs within both platforms we ensured that the appropriate pool size and timeout settings fit the requirements.
### Database Schema:
- Opening the environment we chose to work on (in this case Google Cloud Shell) we cloned the repo we wanted to store all the information in.
- Then we would ensure that we can connect and access our database through Google Shell by using the command ``` mysql -u _username_ -h _host(IP-address)_-p```
- The next step starting with Azure was to create the database schema 
- Created an ```azure.py``` file were we store all of the code including the schema of our tables
- Within our code we ensured that we had the command line of authorizing access when provided with the correct information ```
