# Usa una imagen base oficial de Python
FROM python:3.9

# Establece el directorio de trabajo
WORKDIR /app

# Copia los archivos del proyecto al directorio de trabajo
COPY . /app
COPY main/data /app/data

# Instala las dependencias del proyecto
RUN pip install -r requirements.txt

# Expone el puerto en el que corre la aplicación
EXPOSE 8000

# Comando para correr la aplicación
CMD ["python", "main/main.py"]