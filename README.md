# FBI Most Wanted Fugitives(Flask,Docker)
FBI Most Wanted Fugitives Python API Flask app in Docker.

### Build application
Build the Docker image manually by cloning the Git repo.
```
$ git clone https://github.com/canogluonur/FBI-Flask-API-Docker.git
$ docker build -t dockerpython . 
```
Note: dockerpython can be replaced with any name.

```

### Run the container
Create a container from the image.
```
docker run -p 5000:5000 dockerpython 
```

Now visit http://localhost:5000
```
 The hostname of the container is 6095273a4e9b and its IP is 172.17.0.2. 
```

### Verify the running container

```
![Screenshot](https://user-images.githubusercontent.com/58385909/193022232-e7938a35-ea47-440f-8f06-cfc955b89797.png)

```
Also you can run from Docker Hub;
$ docker pull onurcanoglu/fbi

$ docker container run -p 5000:5000 onurcanoglu/fbi:latest
```
