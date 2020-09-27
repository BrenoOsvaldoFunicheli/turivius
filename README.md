# Turivius API

## Backend Challenge to provide the API implementation

A complete implementation of RESTful API to store and consume some structures that it contains, which were created using django 3 and django rest_framework.

## Sections

* :scroll: [Patterns](#scroll-patterns) (optional)
* :blue_book: [Requirements](#blue_book-requirements)
* :postbox: [Testing](#postbox-testing)
* :wrench: [Building App](#wrench-building-app)
* :key: [Authentication](#key-authentication)

## :scroll: Patterns

In order to create the real stage API to consuming I follow some best pratice and concepts of RESTful APIs must has, beside this, I provide the detailed documentation about API with the postman to test endpoints.

### Implemented concepts

* Versioning: All endpoints contains as prefix /api/v1/ that show the version api is first. So when I change some detail or implementation of API I Don't broken any implementation on my API in other application.

* Pagination: As many people can consuming the endpoints I need provide some throughput data. to first version we apply the limit with 5 registries.

* Authentication: I make the API visualization with the JWT tokens to Authentication on each endpoints

* 12-Factor: I provide the config on the .env file

* Container Build: I provide the easy start with docker containers that wrapper the network problems, installations problems and virtual environments

* Git-Flow: Approach that allow the flow to create, update and deploy your code on simple steps

## :blue_book: Requirements

The system consists of a judge legal view API, where the user can view legal decisions about the certain case

### Requirements

* Authentication: The user registry himself with the password and email and can be get the token to access any endpoint to create and delete his registry by request.

## :postbox: Testing

Test automation is the use of software to control the execution of the software test, the comparison of the expected results with the actual results, the configuration of the test pre-conditions and other control and test report functions.
In this repository I provide some task to show the knowledge with tests.

## :wrench: Building App

There are two way to build and run this application, first is running with isolate app, second is with docker that separates the context and allows running withou previous dependecies.  

### Normal build

1. Get repository
2. Make the virtualenv
3. Run o virtualenv
4. Install all dependecies
5. Run test
6. Run migrations
7. Run app

```console

    git clone https://github.com/BrenoOsvaldoFunicheli/turivius
    python3 -m venv .env
    source .env/bin/activate
    pip install -r requirements.txt
    python manage.py test
    python manage.py migrate
    python manage.py runserver 0.0.0.0:8002

```

### Docker Build

This API was construct with the docker implementation, so you can run without others dependecies and scale after make your implementations, so you need make docker and docker compose in your machine.

#### Docker installation

To install docker follow the instructions in the links below depending on your operating system:

* CentOS: https://docs.docker.com/install/linux/docker-ce/centos/
* Debian: https://docs.docker.com/install/linux/docker-ce/debian/
* Fedora: https://docs.docker.com/install/linux/docker-ce/fedora/
* Ubuntu: https://docs.docker.com/install/linux/docker-ce/ubuntu/
* MacOS: https://docs.docker.com/docker-for-mac/install/
* Windows: https://docs.docker.com/docker-for-windows/install/

#### Step by Step to Set Up

For API build you need some simple steps, download the this repository with the follow command:

``` linux

git clone https://github.com/BrenoOsvaldoFunicheli/turivius

```

before the next step you need create the docker-volume to store the database data.

``` linux

docker volume create turi

```

Next, you need setting the app and database containers with the follow command on the folder downloaded, that make(download all dependencies of the project), building(when you don't have container in your machine it downloaded it) and setting containers with docker compose.

``` linux

docker-compose build

docker-compose up

```

After this you need create database on container, because django can't create automatic, the database container is running the postgres. so you need create the database with the name magalu.

* Docker attach

``` linux

docker exec -it [container-name] /bin/sh -c "[ -e /bin/bash ] && /bin/bash || /bin/sh"

```

* Postgres DDL

``` sql

CREATE DATABASE turi;

```

Finally, you can use the API !!!

## :key: Authentication

As the API was implemented with JWT tokens all access on the endpoints are do with the jwt tokens, so you need apply the request and set in the authorization.

### Token duration

So when you access token through the url [uri]/api/v1/[resource] you can get two values on the payload response, first is the access token, with it, you can access the endpoint for 5 minutes, after you need used the refresh endpoint that gives the token to access for 24 hours.  

### Observations

* The first note is the fact of .env is at this repository. It's because to this challenge, in real development this pratices is wrong;

* Other thing, it is fact of the doesn't have the extra features on the project, because of the time consuming;

* Because of the time consuming, I don't provide the heroku deploy and import_script(to get data on drive), but it's simple to implement and test;

