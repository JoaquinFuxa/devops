# Usar una imagen base de Python
FROM python:3-alpine

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
CMD ["python", "main.py"]
