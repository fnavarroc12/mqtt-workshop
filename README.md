# Mqtt Workshop - IoT

Requerimientos para ejecutar este taller

1. Git instalado en tu máquina.
2. Docker instalado en tu máquina.
3. Un navegador web moderno (Google Chrome, Firefox, Edge, Safari).
5. Conexión a Internet para descargar las imágenes de Docker y las dependencias de Python.
6. [MQTT Explorer](https://mqtt-explorer.com) (opcional, pero recomendado para visualizar mensajes MQTT).

## Instrucciones para ejecutar el taller

## Paso 1: Instalación de Git

### Windows

1. Descarga Git desde [git-scm.com](https://git-scm.com/download/win)
2. Ejecuta el instalador descargado
3. Sigue las instrucciones del asistente de instalación (puedes usar las opciones por defecto)
4. Verifica la instalación abriendo Command Prompt o PowerShell y ejecutando:

```powershell
git --version
```

### Apple MacOS

**Opción 1: Usando Homebrew (recomendado)**
```zsh
brew install git
```

**Opción 2: Descarga directa**
1. Descarga Git desde [git-scm.com](https://git-scm.com/download/mac)
2. Ejecuta el instalador .dmg
3. Sigue las instrucciones de instalación

**Opción 3: Usando Xcode Command Line Tools**
```bash
xcode-select --install
```

Verifica la instalación:
```bash
git --version
```

### Linux

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install git
```

**CentOS/RHEL/Fedora:**
```bash
# CentOS/RHEL
sudo yum install git

# Fedora
sudo dnf install git
```

**Arch Linux:**
```bash
sudo pacman -S git
```

Verifica la instalación:
```bash
git --version
```

## Paso 2: Instalación de Docker

### Windows

1. Descarga Docker Desktop desde [docs.docker.com/desktop/windows/install/](https://docs.docker.com/desktop/windows/install/)
2. Ejecuta el instalador descargado
3. Sigue las instrucciones del asistente de instalación
4. Reinicia tu computadora cuando se te solicite
5. Verifica la instalación abriendo Command Prompt o PowerShell y ejecutando:

```powershell
docker --version
```

### Apple MacOS

1. Descarga Docker Desktop desde [docs.docker.com/desktop/mac/install/](https://docs.docker.com/desktop/mac/install/)
2. Ejecuta el archivo .dmg descargado
3. Arrastra Docker a la carpeta Applications
4. Inicia Docker Desktop desde Applications
5. Verifica la instalación:

```bash
docker --version
```

### Linux

**Ubuntu/Debian:**

Sigue las instrucciones oficiales en [docs.docker.com/engine/install/ubuntu/](https://docs.docker.com/engine/install/ubuntu/)

```bash
# Comandos básicos de instalación
sudo apt update
sudo apt install docker.io
sudo systemctl start docker
sudo systemctl enable docker
```

**CentOS/RHEL/Fedora:**

Sigue las instrucciones oficiales en [docs.docker.com/engine/install/centos/](https://docs.docker.com/engine/install/centos/)

**Otras distribuciones:**

Consulta la documentación oficial en [docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)

Verifica la instalación:
```bash
docker --version
```





## Paso 3: Preparación del Laboratorio

Continúa con las instrucciones en el archivo [Containers.md](Containers.md) para configurar los contenedores Docker necesarios para ejecutar el taller.
