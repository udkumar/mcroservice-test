## Microservice for file handling test assignment

### What I have covered in this app
 * Three endpoint (routes)
 * Added controller and services
 * Written unit test for service methods
 * Dockerized the complate application with `Gunicorn`, `Nginx`, `docker-compose`
 * Tested with production environment

### What I can add more for production environment to make more scalable
 * Can add LB at two level (As database is not required for this assignment)
   * Between user-request  and web-server
   * Between web-server and application server

### How to setup this application with docker
    * Prerequisite:
        * python 3.8
        * Docker and docker-compose 
            * [Link to install docker-compose](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04)
            * [Link to install docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)
        * git
    * Steps for run the application
        * `git clone https://github.com/udkumar/microservice-test.git`
        * `cd microservice-test`
        * `chmod u+x run_docker.sh`

### APIs endpoint to test the app
    * Base URL: `http://localhost:9011`
        * Endpoint: `/api/v1/\.js*`
        * Method: `GET`
        * Response:
        ```code
        {
            "data": [
                "package.json",
                "main.js",
                "App.jsx"
            ],
            "err": "",
            "message": "File listed successfully !",
            "status": 1
        }
        ```