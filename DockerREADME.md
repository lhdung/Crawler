# Docker

## Defintion
Docker is a platform for developers and sysadmin to develop, deplay and run app with CONTAINERS, it allows the creation of independent and separate environments for launching and developing app and this enviroments is called the container. When you need to deploy any server just run the Docker container, your application will be launched immediately.

## Dockerfile
Dockerfile is a config file for Docker to build the image
Config will be using:
  -FROM: specify the original image (python, unbutu,...)
  -LABEL: Provides metadata for the image (using docker inspect)
  -ENV: Set an environment variable
  -RUN: Used to install packages into containers
  -COPY: Copy files and folders into the containers
  -ADD: Copy files and folders into the containers
  -CMD: Provide a command and argument fof executable container
  -WORKDIR: Set up working directory 
  -ARG: Defines the variables value used when image build 
  -ENTRYPOINT: Provides commands and arg for executable containers
  
 ## Basic Command
 - List images/containers:
  ``` docker image/containers ls```
 - Delete image/container:
  ``` docker image/containers rm image/container <name image/container>```
 - Delete all image:
  ``` docker image rm $(docker images -a -q)```
 - List all container:
  ``` docker ps -a```
 - Stop a container:
  ``` docker stop <name container>```
 - Run container from image and change name of container
  ``` docker run -name <name container> <name image>```
 - Show log a container:
 ``` docker logs <name container>```
 - Build image from container:
  ``` docker build -t <name container>```
 - Download image from dockerhub
  ``` docker pull <name image>```
 - Start container:
  ``` docker start <name container>```
 
  

