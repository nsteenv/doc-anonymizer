# Document anonymizer

This is a small project written in Python to anonymize doc/docx documents for french administrations.

It's just a simple web project with a nginx proxy and flask web app behind.

## Requirements

In order to set up the project you'll need to have 

* [docker](https://docs.docker.com/)
* [docker-compose](https://docs.docker.com/compose/)
* [docker-machine](https://docs.docker.com/machine/) (you should really move to linux though)

## Configuration

Feel free to edit the sample .env file if you want to tune things a bit (ex: security key or folders)

## Installation

Build the main docker image (this will pip install requirements.txt as well)

> docker-compose build

Set up the containers

> docker-compose up -d

You can then access the web UI at http://127.0.0.1

## Team

[Armand Gilles](https://github.com/armgilles)
[Vincent Van Steenbergen](https://github.com/nsteenv)