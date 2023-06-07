# mdi-task
## Why was weatherapi.com used instead of visuallcrossing.com
In itself, Visualcrossing provides a great service as weather API. It has field selection at the API level making it really easy to use. Unfortunately the free account only allows 1000 queries/day, which is not enough to retrieve historical weather data starting from 2023 - when send a GET requests with the route "https://weather.visualcrossing.com/VisualCrossingWebServices/rest/services/timeline/Vilnius,LT/2023-01-01/2023-06-06" error 429 (too many requests) is shown immediately.
For this reason, another weather API service was used - weatherapi.com. This service is not nearly as polished as Visualcrossing, since you cannot use field selection at an API level, only data for 1 month can be requested per one request and the API's return data is not structured as well as Visualcrossing, though, owing to the fact that after registering you get 2 weeks of Pro Plan use, it got the job done.
Because of using weatherapi.com more code had to written to make it work and structure the data by the requirements of the task (filter_data functions in weather_api.py).
## Prerequisites and deployment
### Prerequisites
- Python must be installed in the system (latest release)
- In order for the database writting functionality work, a database table must be present and the connection string should be modified in the .env file
```
    CREATE TABLE weather (
    city VARCHAR(100),
    date DATE,
    max_temp FLOAT,
    min_temp FLOAT,
    conditions VARCHAR(100)
    );
```
### Deployment
- Clone the git repo: git clone https://github.com/emkah4/mdi-task
- Create a virtual enviroment and launch it (recommended): python3 -m venv env -> source evn/bin/activate 
- source evn/bin/activate
- Install dependencies: pip install -r requirements.txt
- Launch the app: python3 main.py
