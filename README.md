# ProyectoSustitutoCristianTamayo

Estudiante: Cristian David Tamayo Espinosa cc1007240828

fase-1
En el directorio fase-1 encontrará un notebook donde se muestra cómo se entrena y se predice con el modelo, allí encontrara un boton para abrir el notebook en colab donde podra ejecutarlo, allí debera subir un token kaggle.json para poder ejecutar el notebook.

fase-2

1. clonar el repositorio:

Abrir linea de comandos y clonar:

```bash
git clone https://github.com/CrissPr/ProyectoSustitutoCristianTamayo.git

Una vez clonado debera dirigirse al directorio fase-2 del repositorio clonado, para ello puede hacer uso de:

cd (ruta-carpeta-donde-se-clonó-el-repositorio)/ProyectoSustitutoCristianTamayo/fase-2

2. crear imagen

docker build -t imagenmodelo .

3. crear y correr contenedor

docker run -it --name container imagenmodelo

4. correr scripts

debera correr los scripts en el siguiente orden

python train.py

python predict.py

python run-scripts.py

este ultimo servira para listar predicciones






