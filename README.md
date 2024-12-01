# ProyectoSustitutoCristianTamayo

Estudiante: Cristian David Tamayo Espinosa cc1007240828
Ing de sistemas

**fase-1**
En el directorio fase-1 encontrará un notebook donde se muestra cómo se entrena y se predice con el modelo, allí encontrara un boton para abrir el notebook en colab donde podra ejecutarlo, allí debera subir un token kaggle.json para poder ejecutar el notebook.

**fase-2**

**1.** clonar el repositorio:

Abrir linea de comandos y clonar:

```bash
git clone https://github.com/CrissPr/ProyectoSustitutoCristianTamayo.git
```

Una vez clonado debera dirigirse al directorio fase-2 del repositorio clonado, para ello puede hacer uso de:

```bash
cd (ruta-carpeta-donde-se-clonó-el-repositorio)\ProyectoSustitutoCristianTamayo\fase-2
```


2. crear imagen

```bash
docker build -t imagenmodelo .
```


3. crear y correr contenedor

```bash
docker run -it --name container imagenmodelo
```


4. Una vez adentro del container creado, correr los siguientes scripts:

   debera correr los scripts en el siguiente orden

```bash
python train.py
```
```bash
python predict.py
```
```bash
python run-scripts.py
```
este ultimo ejecutara predicciones y permitira visualizar las predicciones de las primeras filas.

**Nota:** Recuerde correr primero train.py y luego predict.py , ya que train.py guardara un modelo como model.pkl , el cual sera usado posteriormente por predict.py 

**breve descripción de cada script:**

**train.py:** Este script carga un conjunto de datos de entrenamiento (train.csv), preprocesa los datos (rellena valores faltantes y codifica variables categóricas) y entrena un modelo de RandomForest. Luego el modelo se guarda como model.pkl

**predict.py:** Este script carga el conjunto de datos de prueba (test.csv), lo preprocesa de manera similar a los datos de entrenamiento y utiliza el modelo previamente guardado (model.pkl) para hacer predicciones. Los resultados se guardan en un archivo predictions.csv.

**run-scripts.py:** Este script automatiza el flujo de trabajo ejecutando primero train.py para entrenar y luego ejecutando predict.py para generar las predicciones. También listara las predicciones de las primeras filas.


**fase-3**


**1.** clonar el repositorio:

Abrir linea de comandos y clonar:

```bash
git clone https://github.com/CrissPr/ProyectoSustitutoCristianTamayo.git
```

Una vez clonado debera dirigirse al directorio fase-3 del repositorio clonado, para ello puede hacer uso de:

```bash
cd (ruta-carpeta-donde-se-clonó-el-repositorio)\ProyectoSustitutoCristianTamayo\fase-3
```


2. crear imagen

```bash
docker build -t titanic-api-test .
```


3. crear y correr contenedor en el puerto 5000

```bash
docker run -it -p 5000:5000 titanic-api-test
```


4. abrir otra consola de comandos y correr:

```bash
python client.py
```




