# PredictCar

Proyecto de predicción de precios de coches utilizando Machine Learning y un backend en Flask. Este proyecto forma parte de mi Trabajo de Fin de Máster (TFM) en IA y Big Data.

---

## Estructura del proyecto

TFMPrueba/
│
├── data/ # Datos originales
│ └── vehicles.csv # Dataset principal
│
├── ml_model/ # Notebooks y pruebas del modelo
│ ├── AtributosImportantes.ipynb
│ ├── ComprobarOpciones.ipynb
│ ├── pruebaModeloHF.ipynb
│ └── RandomForest.ipynb
│
├── templates/ # Plantillas HTML para Flask
│ └── index.html
│
├── venv/ # Entorno virtual (ignorado por Git)
│
├── modeloPrediCocheV1.pkl # Modelo ya entrenado (ignorado por Git)
├── server.py # API Flask para predicción
├── .gitignore # Ignora archivos/carpetas innecesarios
└── README.md # Este documento

---

## Tecnologías usadas

- Python 3
- Flask
- Scikit-learn
- Pandas
- Matplotlib / Seaborn
- HTML + TailwindCSS
- JavaScript (Axios para frontend)

---


## Cómo ejecutar el proyecto

Sigue estos pasos para poner en marcha PredictCar en tu entorno local:

1. **Clona este repositorio**
   Abre tu terminal y ejecuta:

   ```bash
   git clone https://github.com/tuusuario/predictcar.git
   cd predictcar
   ```

2. **Crea y activa un entorno virtual (opcional pero recomendado)**
   En Windows:

   ```bash
   python -m venv venv
   .\venv\Scripts\activate
   ```

3. **Instala las dependencias necesarias**
   Ejecuta lo siguiente para instalar todos los paquetes requeridos:

   ```bash
   pip install flask flask-cors pandas joblib transformers torch scikit_learn deep_translator
   ```

4. **Ejecuta el servidor Flask**
   Lanza la aplicación ejecutando:

   ```bash
   python server.py
   ```

5. **Abre la aplicación en tu navegador**
   Una vez que el servidor esté en marcha, abre el siguiente enlace:

   [http://127.0.0.1:5000](http://127.0.0.1:5000)

---