FROM ubuntu:latest

# Actualizar paquetes e instalar herramientas
RUN apt-get update && apt-get install -y 
    
RUN apt-get install python3.10 -y
RUN apt-get update && apt-get install -y python3-pip

COPY . /app
WORKDIR /app
RUN python3.10 -m pip install --no-cache-dir -r requirements.txt

RUN apt-get update
RUN apt-get install -y libgl1-mesa-glx

RUN apt-get update
RUN apt-get install -y libglib2.0-0

EXPOSE 8501

CMD ["streamlit", "run", "Fruits_Vegetable_Classification.py"]

