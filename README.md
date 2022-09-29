# FBI-Flask-API-Docker
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


![alt text] (https://user-images.githubusercontent.com/58385909/174687348-8fc54f22-8d94-4924-b362-b0efa579287e.png)

![Screenshot](https://user-images.githubusercontent.com/58385909/174687348-8fc54f22-8d94-4924-b362-b0efa579287e.png)



