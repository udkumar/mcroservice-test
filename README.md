## Microservice for file handling test assignment

### What I have covered in this app

* Three endpoint (routes)
* Added controller and services
* Written unittest for services methods
* Dockerized the complate application with `Flask`, `Gunicorn`, `Nginx`, `docker-compose`
* Tested with production environment

### What I can add more for production environment to make more scalable

* Can add LB at two level (As database is not required for this assignment)
   * Between user-request  and web-server
   * Between web-server and application server

### How to setup this application with docker

* Prerequisite:
  * Ubuntu 20.04.3 LTS
  * python 3.8 or +
  * Docker and docker-compose 
    * [Link to install docker-compose](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-compose-on-ubuntu-20-04)
    * [Link to install docker](https://www.digitalocean.com/community/tutorials/how-to-install-and-use-docker-on-ubuntu-20-04)
  * git []

* Steps to run the application with docker
  * `git clone https://github.com/udkumar/microservice-test.git`
  * `cd microservice-test`
  * `chmod u+x run_docker.sh`

* Steps to run the application without docker
  * `git clone https://github.com/udkumar/microservice-test.git`
  * `cd microservice-test`
  * `python3 -m venv env_ikea` (May be for you only `python -m venv env_ikea`)
  * `source env_ikea/bin/activate` (For Windows user `./env_ikea/Scripts/activate`)
  * `pip install -r requirements.txt`
  * `gunicorn app` (If any error showing, just run `python app.py`)

### APIs endpoint to test the app :- [Postman collection for testing APIs](https://github.com/udkumar/microservice-test/blob/master/ikea_python_test.postman_collection.json)

* Base URL: `http://localhost:9011`
  * Endpoint 1: `/api/v1/\.js*`
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

  * Endpoint 2: `/api/v1/frequent_words`
  * Method: `POST`
  * Payload: `form-data`
    * file (select .txt file)
    * freq (Type: Integer [ How many frequent words user want to list] )
    * camelCase (Type: Integer [As python is casensative language to file's word which we need as provided or need small case only])
  * Response:
    ```code
        {
          "data": [
                    {
                        "devasthanam": 1,
                        "in": 2,
                        "the": 4,
                        "tirumala": 2,
                        "tirupati": 1,
                        "ttd": 6,
                        "venkateswara": 3,
                        "venkateswari": 2
                    },
                    {
                        "boy": 1,
                        "is": 2,
                        "this": 1,
                        "who": 1,
                        "working": 1
                    },
                    {
                        "after": 1,
                        "and": 3,
                        "baron": 1,
                        "mlc": 1,
                        "party": 2,
                        "perfume": 1,
                        "samajwadi": 1,
                        "the": 3
                    },
                    {
                        "and": 1,
                        "ec": 1,
                        "of": 1,
                        "president": 1,
                        "the": 3,
                        "to": 2,
                        "will": 1,
                        "write": 1
                    }
                  ],
            "err": "",
            "message": "8 Most frequent words",
            "status": 1
        }
      ```

  * Endpoint 2: `/api/v1/longest_words`
  * Method: `POST`
  * Payload: `form-data`
    * file (select .txt file)
  * Response:
    ```code
      {
        "data": [
            {
                "line 1": [
                    "Venkateswara",
                    "Venkateswari"
                ],
                "line 2": [
                    "This",
                    "Working"
                ],
                "line 3": [
                    "Opposition",
                    "Commission"
                ],
                "line 4": [
                    "President",
                    "Samajwadi"
                ]
            }
        ],
        "err": "",
        "message": "Longest two words !!",
        "status": 1
      }
    ```

Author: [Uday Kumar](udayonrails@gmail.com)
