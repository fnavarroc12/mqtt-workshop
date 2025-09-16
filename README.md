# Mqtt Workshop - IoT

Requerimientos para ejecutar este taller

1. Git instalado en tu máquina.
2. Docker instalado en tu máquina.
3. Python 3.x instalado en tu máquina.
4. Un navegador web moderno (Google Chrome, Firefox, Edge, Safari).
5. Conexión a Internet para descargar las imágenes de Docker y las dependencias de Python.
6. MQTT Explorer (opcional, pero recomendado para visualizar mensajes MQTT).


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





## Paso 3: Instalación de Python 3.x

### Windows

**Opción 1: Descarga desde el sitio oficial (recomendado)**
1. Ve a [python.org/downloads/](https://www.python.org/downloads/)
2. Descarga la última versión de Python 3.x para Windows
3. Ejecuta el instalador descargado
4. **IMPORTANTE**: Marca la casilla "Add Python to PATH" durante la instalación
5. Sigue las instrucciones del asistente de instalación
6. Verifica la instalación abriendo Command Prompt o PowerShell y ejecutando:

```powershell
python --version
# o también
python3 --version
```

**Opción 2: Usando Microsoft Store**
1. Abre Microsoft Store
2. Busca "Python"
3. Instala la versión más reciente de Python 3.x

### Apple MacOS

**Opción 1: Usando Homebrew (recomendado)**
```bash
brew install python3
```

**Opción 2: Descarga directa**
1. Ve a [python.org/downloads/](https://www.python.org/downloads/)
2. Descarga la última versión de Python 3.x para macOS
3. Ejecuta el instalador .pkg
4. Sigue las instrucciones de instalación

Verifica la instalación:
```bash
python3 --version
```

### Linux

**Ubuntu/Debian:**
```bash
sudo apt update
sudo apt install python3 python3-pip
```

**CentOS/RHEL:**
```bash
sudo yum install python3 python3-pip
```

**Fedora:**
```bash
sudo dnf install python3 python3-pip
```

**Arch Linux:**
```bash
sudo pacman -S python python-pip
```

Verifica la instalación:
```bash
python3 --version
pip3 --version
```

**Nota**: En algunos sistemas Linux, Python 3 ya está preinstalado. Si no tienes `pip` instalado, puedes instalarlo por separado:
```bash
# Para la mayoría de distribuciones
sudo apt install python3-pip  # Ubuntu/Debian
sudo yum install python3-pip  # CentOS/RHEL
sudo dnf install python3-pip  # Fedora
```

## Paso 4: Clonar el repositorio del taller

1. Abre una terminal (Command Prompt, PowerShell, Terminal, etc.)
2. Navega al directorio donde deseas clonar el repositorio:
```bashbash
cd ruta/del/directorio
```
3. Clona el repositorio usando Git:
```bash
git clone https://github.com/fnavarroc12/mqtt-workshop.git
``` 

4. Navega al directorio del proyecto:
```bash
cd mqtt-workshop
``` 

## Paso 5: Preparar el entorno de Python

Este taller utiliza un archivo de Jupyter Notebook (.ipynb) para guiarte a través de los conceptos y ejercicios prácticos, por lo cual
es recomendable usar un entorno virtual para gestionar las dependencias de Python y ejecutar nuestro notebook.

Sigue estos pasos para configurar tu entorno:

1. Crea un entorno virtual (opcional pero recomendado):
```bash
python3 -m venv venv
``` 

2. Activa el entorno virtual:
   - En Windows:
   ```bash
   .\venv\Scripts\activate
   ```
   - En macOS/Linux:
   ```bash
   source venv/bin/activate
   ```
3. Instala Jupyter. En este taller usaremos Jupyter Lab para tener acceso sencillo a los notebooks:
```bash
pip install jupyterlab
``` 

4. Ejecuta Jupyter Lab:
```bash
jupyter lab
```

5. Abre el archivo `workshop.ipynb` en Jupyter Lab para comenzar con el taller.
