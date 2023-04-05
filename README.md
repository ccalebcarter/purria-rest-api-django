Dockerized Rest Django Api
steps for cloning and running the repo localy on docker container


- create folder where u want to clone the repository
- cd (name of the created folder)
- git clone https://github.com/martinstojcevski95/purria-rest-api-django.git into the <create folder path>
- code . (to open vs code), if it doesnt open vs code, open it manually and open : View -> Command Pallete and type shell command install 'code'command in PATH
- in vs code open the terminal and cd into purria-rest-api-django folder, then write set -a and source .env.dev
- docker-compose build (to build the docker images)
- docker-compose up -d (to start the containers and the db)
- localhost:8000 in the browset to access the api. the url for the api is http://localhost:8000/apiv1/ Here you can see all other endpoint url's as clickable links.
- docker-compose down to close the running containers 
