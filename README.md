<p align="center">
  <a href="" rel="noopener">
 <img src="https://www.python.org/static/img/python-logo@2x.png" alt="Project logo"></a>
</p>

<h3 align="center">AI Chat System REST API</h3>

<div align="center">

[![Status](https://img.shields.io/badge/status-active-success.svg)]()
[![GitHub Issues](https://img.shields.io/github/issues/kylelobo/The-Documentation-Compendium.svg)]
[![GitHub Pull Requests](https://img.shields.io/github/issues-pr/kylelobo/The-Documentation-Compendium.svg)]
[![License](https://img.shields.io/badge/license-MIT-blue.svg)](/LICENSE)

</div>

---

<p align="center"> Django Rest Framework project
    <br> 
</p>

## 📝 Table of Contents

- [About](#about)
- [Getting Started](#getting_started)
- [Deployment](#deployment)
- [Usage](#usage)
- [Built Using](#built_using)
- [TODO](../TODO.md)
- [Contributing](../CONTRIBUTING.md)
- [Authors](#authors)
- [Acknowledgments](#acknowledgement)

## 🧐 About <a name = "about"></a>

A DRF project for a chat system. It covers all features of a user and a chat system.

### Prerequisites

For installing the project, you will need to have
- Python installed. Python version supported is `3.11`. The Github actions use 3.11 for running live tests.
- Must have PostgreSQL installed. You can use WSL2 to do this on Windows 10 and 11.

### Installing

A step by step series of examples that tell you how to get a development environment running.

Clone the project

```bash
git clone https://github.com/BISHOPDAN/chat-user-api/
```

Setup env & install dependencies

Linux

```bash
python -m venv venv
source venv/bin/activate
pip install -r piprequirements.txt
```

Windows

```bash
python -m venv venv
venv\Scripts\activate
pip install -r piprequirements.txt
```

Run migrations

```bash
python manage.py migrate
```

Run the server

```bash
python manage.py runserver
```


> For the database keys in the env file, you can create a new user and password for the project.

This must be used to ensure all coding style guidelines are met

```bash
flake8
```

## 🎈 Usage <a name="usage"></a>

To run the API on your local system.

```bash
python manage.py runserver
```

API server will run on `http://localhost:8000/`. Visit [Swagger](http://localhost:8000/swagger/) to read the Swagger API documentation.

The following method describes how to deploy this on a live system.

### Using Ngrok
- Install [Ngrok](https://ngrok.com/docs/getting-started) on your machine.
- Run API server
- Open CMD / CLI, Run `ngrok http 8000`. `8000` is used if that's the port the API server is listening to. Otherwise, use the listening port.
- The rest is history!


### Using Nginx on an Ubuntu Server
#### Coming soon!
<!-- A deploy script.sh should be created to automate the deployment on a new server -->
<br>


## Contributing

Use the following steps below to contribute to this project.

1. First checkout to the `master` branch
2. Create a new branch for your feature
3. Make your changes
4. Commit your changes
5. Push your changes to your branch
6. Create a pull request to the `master` branch
7. Wait for review and merge


## ⛏️ Built Using <a name = "built_using"></a>

- [Django](https://www.djangoproject.com/) - Web Framework
- [Django Rest Framework](https://www.django-rest-framework.org/) - Building Web APIs
- [PostgreSQL](https://www.postgresql.org/) - Database
- [Python](https://www.python.org/) - Programming Language


## :book: Documentation <a name = "documentation"></a>

Things to note about the project

## ✍️ Authors <a name = "authors"></a>

- [@devvspaces](https://github.com/devvspaces) - Project Setup & Initial work

## 🎉 Acknowledgements <a name = "acknowledgement"></a>

- Hat tip to anyone whose code was used
- Inspiration
- References
