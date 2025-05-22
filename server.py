from flask import Flask, request, jsonify, render_template
import joblib
import pandas as pd
from flask_cors import CORS
from transformers import pipeline
from deep_translator import GoogleTranslator

# ejecutandose en               python 3.10.0
# crear venv                    python -m venv venv
# activar venv                  .\venv\Scripts\activate
# instalaciones necesarias      pip install transformers flask pandas joblib flask-cors
#                               pip install deep_translator
#                               pip install scikit_learn        ns si esta bien escrito
#                               pip install torch



app = Flask(__name__)
CORS(app)

# Carga del modelo
modelo = joblib.load('modeloPrediCoche.pkl')
columnas_modelo = modelo.feature_names_in_

# Ruta para el main de la web y /predecir
@app.route('/')
def home():
    return render_template('index.html')

# Uso del modelo para mandar el precio estimado
@app.route('/predecir', methods=['POST'])
def predecir():
    # Datos reecibidos del frontend
    data = request.get_json()
    df_entrada = pd.DataFrame([data])
    df_transformado = pd.DataFrame([[0]*len(columnas_modelo)], columns=columnas_modelo)
    # cambio de los nombres ya que el modelo usa unos diferentes
    for col in df_entrada.columns:
        val = df_entrada[col][0]
        if col in ['brand', 'fuel', 'condition', 'traction', 'vehicleType', 'cylinders']:
            nombre_col = f"{col}_{val}"
            if nombre_col in df_transformado.columns:
                df_transformado[nombre_col] = 1
        elif col in ['year', 'KM', 'mileage']:
            if col == 'mileage' and 'KM' in df_transformado.columns:
                df_transformado['KM'] = val
            elif col in df_transformado.columns:
                df_transformado[col] = val
    # Uso del modelo con los datos recibidos y procesados
    try:
        prediccion = modelo.predict(df_transformado)
        return jsonify({'precio_estimado': round(float(prediccion[0]), 2)})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Cargar el modelo de las emociones de Hugging Face
modelo_emociones = pipeline("text-classification", model="bhadresh-savani/bert-base-uncased-emotion")

@app.route('/analizar_comentario', methods=['POST'])
def analizar_comentario():
    data = request.get_json()
    comentario = data.get('comentario', '')

    if not comentario:
        return jsonify({'error': 'Comentario vacío'}), 400

    try:
        comentario_traducido = GoogleTranslator(source='auto', target='en').translate(comentario)
        resultado = modelo_emociones(comentario_traducido)
        emocion = resultado[0]['label']
        return jsonify({'emocion': emocion})
    except Exception as e:
        return jsonify({'error': str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)