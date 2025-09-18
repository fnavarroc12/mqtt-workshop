# Contenedores Docker para el Workshop

Por favor, asegúrate de tener Docker instalado en tu máquina antes de continuar.
Puedes seguir las instrucciones en [Docker Install](https://docs.docker.com/get-docker/).

Ejecuta los siguientes comandos en tu terminal, para preparar el entorno de trabajo:

## 1. Limpieza de entorno

Ejecuta los siguientes comandos para eliminar contenedores, redes y volúmenes previos, esto es requerido solamente si ya se ha ejecutado algún paso posterior a este, su funcion es limpiar el entorno para evitar conflictos.

```bash
docker stop jlab nodered mosquitto

docker rm -f mosquitto nodered mailhog 2>/dev/null || true

docker network rm demo-net 2>/dev/null || true

docker volume rm -f mosq_conf mosq_data mosq_log nodered_data 2>/dev/null || true

docker rm -f jlab 2>/dev/null || true
```

## 2. Creación de red

Red virtual para que los contenedores puedan comunicarse entre sí.

```bash
docker network create demo-net 2>/dev/null || true
```

## 3. Mosquitto Volumes

Volúmenes para persistencia de datos de Mosquitto

```bash
docker volume create mosq_conf >/dev/null
docker volume create mosq_data >/dev/null
docker volume create mosq_log  >/dev/null
```

# 4. Credenciales de Mosquitto y Configuración básica
```bash
docker run --rm --network demo-net   -v mosq_conf:/mosquitto/config   -v mosq_data:/mosquitto/data   -v mosq_log:/mosquitto/log   eclipse-mosquitto sh -lc 'cat >/mosquitto/config/mosquitto.conf <<EOF
listener 1883
allow_anonymous false
password_file /mosquitto/config/passwd
persistence true
persistence_location /mosquitto/data/
log_dest stdout
EOF
touch /mosquitto/config/passwd
mosquitto_passwd -b /mosquitto/config/passwd nodered nodered
chmod 600 /mosquitto/config/passwd
echo "[OK] Mosquitto config & passwd listos"'
```

## 5. Crear contenedor de Mosquitto

Comando para crear el contenedor de Mosquitto, mapeando el puerto 1883 y montando los volúmenes creados en el paso anterior.

```bash
docker run -d --name mosquitto --network demo-net   -p 1883:1883   -v mosq_conf:/mosquitto/config   -v mosq_data:/mosquitto/data   -v mosq_log:/mosquitto/log   eclipse-mosquitto
```

En este punto ya deberías tener el broker MQTT Mosquitto corriendo en el contenedor, utilizando el MQTT Explorer al puerto `1883`, utilizando las siguientes credenciales:

- **Usuario**: nodered
- **Password**: nodered

## 6. Volumen para Node-RED

El siguiente comando crea un volumen para persistencia de datos de Node-RED.

```bash
docker volume create nodered_data >/dev/null
```

## 7. Configuración de Node-RED

Comando para crear los archivos de configuración iniciales de Node-RED, incluyendo las credenciales para conectarse a Mosquitto.

```bash
docker run --rm -v nodered_data:/data alpine:3.20 sh -lc 'cat >/data/settings.js <<EOF
module.exports = {
  flowFile: "flows.json",
  credentialSecret: false,
  editorTheme: { projects: { enabled: false } },
  functionGlobalContext: {}
}
EOF

cat >/data/flows_cred.json <<EOF
{ "broker1": { "user": "nodered", "password": "nodered" } }
EOF

chown -R 1000:1000 /data
echo "[OK] settings/flows/creds listos"
'
```

## 8. Crear contenedor de Node-RED

Comando para crear el contenedor de Node-RED, mapeando el puerto 1880 y montando el volumen creado en el paso anterior.

```bash
docker run -d --name nodered --network demo-net   -p 1880:1880   -v nodered_data:/data   nodered/node-red:latest
```
En este punto, ya deberías tener Node-RED corriendo en el contenedor, puedes acceder a la interfaz web de Node-RED en tu navegador web, ingresando a la siguiente URL:

[http://localhost:1880](http://localhost:1880)


## 9. Crear contenedor de Jupyterlab

Comando para crear el contenedor de Jupyterlab, mapeando el puerto 8888 y montando un volumen local para persistencia de datos.

```bash
docker run -d --name jlab \
  -p 8888:8888 \
  --network demo-net \
  -v "./workshop":/home/jovyan/work \
  jupyter/scipy-notebook:latest
```

Para acceder al Jupyterlab, se requiere ingresar la URL con el token que se muestra en los logs del contenedor. Puedes obtener la URL ejecutando:

```bash
docker logs jlab 2>&1 | grep -m1 -Eo 'http://127\.0\.0\.1:8888/\S+'
```

Una vez ingreses a Jupyterlab, puedes abrir el archivo `work/workshop.ipynb` para comenzar con el taller.