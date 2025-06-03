# Usa imagen oficial de python 3.12
FROM python:3.12-slim

# Instala ffmpeg
RUN apt-get update && apt-get install -y ffmpeg

# Copia archivos de tu proyecto al contenedor
WORKDIR /app
COPY . /app

# Instala dependencias
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Ejecuta el bot
CMD ["python", "main.py"]
