from flask import Flask, request, jsonify
import tensorflow as tf

app = Flask(__name__)

# Załaduj zrzucony model
model = tf.keras.models.load_model('multisteplstm.h5')

@app.route('/predict', methods=['POST'])
def predict():
  #ramka: 66.23333333,	0.089,	5.4, 2.9,	0.008,	676.9785714,	21.52857143,	227.552381,	6.936684628,	50.00928571,	0.998714286,	4.786642857,	4.890142857,	0.913571429,	97.85142857,	329.2614146	12.78
  # Pobierz dane z requestu
  data = request.get_json()
  input_data = data['input']

  # Wywołaj metodę predykcji modelu
  prediction = model.predict(input_data).tolist()

  # Zwróć wynik jako odpowiedź
  return jsonify({'prediction': prediction})

if __name__ == '__main__':
  app.run()