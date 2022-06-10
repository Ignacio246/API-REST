# API-REST

## Crear la imagen de Docker

```bash
docker build -t api_rest:10.06.22 .
```

## Crear la imagen de Docker

```bash
docker run -it -v "$PWD"/code:/home/code --net host --nmae api-rest 
-h api-rest api_rest:10.06.22
```