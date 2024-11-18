# Usar una imagen base de Python
FROM python:3-alpine

# Instala las dependencias necesarias usando apk en lugar de apt-get
RUN apk update && apk add --no-cache \
    wget \
    && rm -rf /var/cache/apk/*

# Descarga dockerize
RUN wget https://github.com/jwilder/dockerize/releases/download/v0.6.1/dockerize-linux-amd64-v0.6.1.tar.gz \
    && tar -xvzf dockerize-linux-amd64-v0.6.1.tar.gz \
    && mv dockerize /usr/local/bin/
    
# Establecer el directorio de trabajo
WORKDIR /app

# Copiar los archivos de requirements.txt y luego instalar las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de la aplicación Flask
COPY . .

# Exponer el puerto en el que Flask va a escuchar (usualmente el 5000)
EXPOSE 5000

# Establece el comando para esperar por MySQL antes de iniciar la app
CMD ["dockerize", "-wait", "tcp://db:3306", "-timeout", "60s", "python", "main.py"]
