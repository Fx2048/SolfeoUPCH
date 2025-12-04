FROM python:3.10-slim

# Instalar dependencias del sistema
RUN apt-get update && apt-get install -y \
    default-jre \
    fluidsynth \
    fluid-soundfont-gm \
    lilypond \
    timidity \
    wget \
    && rm -rf /var/lib/apt/lists/*

# Configurar variables de entorno para LilyPond y Python
ENV LANG=C.UTF-8
ENV LC_ALL=C.UTF-8
ENV GUILE_AUTO_COMPILE=0
ENV PYTHONUNBUFFERED=1

# Configurar directorio de trabajo
WORKDIR /app

# Copiar requirements y instalar dependencias Python
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todo el proyecto
COPY . .

# Crear directorio de salidas con permisos adecuados
RUN mkdir -p /app/static/outputs && chmod 777 /app/static/outputs

# Exponer puerto (Render usa la variable $PORT)
EXPOSE 10000

# Comando de inicio - CRÍTICO: ejecutar desde /app/Src donde está web_app.py
CMD ["gunicorn", "--bind", "0.0.0.0:10000", "--timeout", "120", "--workers", "2", "--chdir", "/app/Src", "web_app:app"]
