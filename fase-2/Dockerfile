# Dockerfile

# Usar una imagen oficial de Python como imagen base
FROM python:3.9-slim

# Establecer el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copiar el contenido del directorio actual al contenedor en /app
COPY . /app

# Instalar las dependencias necesarias desde el archivo requirements.txt
RUN pip install --no-cache-dir -r requirements.txt


# Iniciar el contenedor con un shell bash
CMD ["/bin/bash"]


