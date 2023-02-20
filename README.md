# foo-microservice

Python foo microservice


## Example docker run

```bash
 docker run -d -e MESSAGE="Hi v1 foo" -e PORT=3002 -e ROUTE_PATH="v1/foo" --name foo -p 3002:3002 m2stacklab/foo-microservice:latest
```