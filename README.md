# API Connector:
This is a connector to the Randomuser API service to show random user data

* Backend will pull the data (name, gender, location, email) from [Randomuser API](https://randomuser.me/api)
* The Randomuser API doccumentation can be found [here](https://randomuser.me/documentation)
* Backend controller smartly pulls and serves the data to the frontend UI 
* In case of an unsuccessful synchronization attempt, the backed serve data from the last successful synchronization
* Frontend UI will show the user data such as user name, gender, country, email
* Frontend UI has the functionality to filter data using country and user name
* Frontend UI also provides pagination and sorting of data

# Installations:

## Frontend
Download and install [Node.js and npm](https://docs.npmjs.com/downloading-and-installing-node-js-and-npm)

Then run the following cmd from the /frontend to install required dependancy and run the frontend 
    
    npm install

    npm run serve

## Backed

### Using docker
Install [docker](https://docs.docker.com) and [docker compose](https://docs.docker.com/compose).

Then run the following cmd from the root folder to run the backend

     docker-compose up or $ docker-compose -d to run in the background

### Manually  
Please use the following steps to run the backend manually 
1. Install [python 3.8](https://www.python.org/downloads) or higher
2. Install and create new isolated [conda env](https://docs.conda.io/en/latest/miniconda.html) or [python virtual env](https://docs.python.org/3/tutorial/venv.html) and activate it.
3. Then from /backend run `pip install -r requirements.txt`. it will install all required dependency
4. From /backend run `controller.py` to start the backend controller


# Usage
1. Open any web browser and go to http://localhost:8601, you should get the following response

    `{'message': 'API connector is us and running'}`

2. User data is available at route `http://localhost:8601/users`  
3. Frontend is running at `http://localhost:8610` and consuming data from the backend
4. Open `http://localhost:8610` in any web browser where you can see user data from Randomuser API
5. User data can be filtered by country name and user name
6. There is also a `RELOAD DATA` button to pull updated data from backend/Randomuser API


## Important:
The steps here for backend and frontend are to start and run development uses. for the production and deployment please refer following references.

1. For the Production Deployment of the [vue frontend](https://vuejs.org) please [refer](https://v2.vuejs.org/v2/guide/deployment.html?redirect=true) 
2. For the Production Deployment of the docker [flask backend](https://flask.palletsprojects.com/en/2.1.x) please [refer](https://docs.docker.com/get-started/kube-deploy) 

## Happy coding 
