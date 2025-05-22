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

1. **Clona el repositorio**:
git clone https://github.com/tuusuario/predictcar.git

2. **Ejecuta y haz todas las instalaciones necesarias con pip**:
.\venv\Scripts\activate

pip install transformers flask pandas joblib flask-cors
pip install deep_translator
pip install scikit_learn
pip install torch

python server.py

3. **Ve al enlace que sale en la terminal**:
http://127.0.0.1:5000