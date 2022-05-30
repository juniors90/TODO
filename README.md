# TODO

[![GitHub stars](https://img.shields.io/github/stars/juniors90/TODO)](https://github.com/juniors90/TODO/stargazers)
[![GitHub forks](https://img.shields.io/github/forks/juniors90/TODO)](https://github.com/juniors90/TODO/network)
[![GitHub issues](https://img.shields.io/github/issues/juniors90/TODO)](https://github.com/juniors90/TODO/issues)
[![GitHub contributors](https://img.shields.io/github/contributors/juniors90/TODO?color=green)](https://github.com/juniors90/TODO/graphs/contributors)
[![black](https://img.shields.io/badge/code%20style-black-000000.svg)](https://github.com/psf/black)
[![codecov](https://codecov.io/gh/juniors90/TODO/branch/main/graph/badge.svg?token=zg5NMZ47Rg)](https://codecov.io/gh/juniors90/TODO)


## Base de datos y App Engine con Flask:

- *Bases de Datos SQL*: su composición esta hecha con bases de datos llenas de tablas con filas que contienen campos estructurados. No es muy flexible pero es el más usado. Una de sus desventajas es que mientras más compleja sea la base de datos más procesamiento necesitará.

- *Base de Datos NoSQL*: su composición es no estructurada, es abierta y muy flexible a diferentes tipos de datos, no necesita tantos recursos para ejecutarse, no necesitan una tabla fija como las que se encuentran en bases de datos relacionales y es altamente escalable a un bajo costo de hardware.


[https://console.cloud.google.com/](https://console.cloud.google.com/)

## Configuración de Google Cloud SDK

### Paso 1:

Instalar el Google Cloud SDK para [Windows](https://cloud.google.com/sdk/docs/quickstart-windows), [MacOS](https://cloud.google.com/sdk/docs/quickstart-macos) ó [Linux](https://cloud.google.com/sdk/docs/quickstart-linux)

### Paso 2:

Una vez que corrimos el instalador, podemos verificar que instalamos correctamente el SDK corriendo en una terminal el siguiente comando:

```
$> which gcloud
/path/to/the/google-cloud-sdk/bin/gcloud
```

### Paso 3:

Ahora inicializamos `gcloud` y hacemos login con:

```
$> gcloud init
$> gcloud auth login
$> gcloud auth application-default login
```

Para saber la configuración de mi proyecto:

```
$> gcloud config list
[core]
account = username@gmail.com
disable_usage_reporting = False
project = flask-123456

Your active configuration is: [default]
```

Para cambiar la configuración de a otro proyecto:

```
$> gcloud config set project <other-project>
Update property [core/project]
```

Para saber la configuración de mi proyecto actual llamado `<other-project>`:

```
$> gcloud config list
[core]
account = username@gmail.com
disable_usage_reporting = False
project = <other-project>

Your active configuration is: [default]
``` 

# conexion a la base de datos:

[Firebase](https://firebase.google.com/docs/admin/setup/#python) en Python.