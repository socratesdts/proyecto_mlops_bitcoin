# Usa una imagen base oficial de Python
FROM python:3.9

# Establece el directorio de trabajo en el contenedor
WORKDIR /app

# Copia los archivos del proyecto al directorio de trabajo
COPY . /app

# Lista los archivos en el directorio /app
RUN ls /app

# Instala las dependencias del proyecto
RUN pip install --no-cache-dir -r requirements.txt

# Expone el puerto en el que corre la aplicación
EXPOSE 8000

# Establece la variable de entorno IN_DOCKER
ENV IN_DOCKER=1

# Comando para correr la aplicación
CMD ["python", "main/main.py"]