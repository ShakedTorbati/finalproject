from flask import Flask, render_template, request
import os
import matplotlib.pyplot as plt
from keras.applications.mobilenet_v2 import MobileNetV2
import requests
def search_plant(plant_name):
    token = "rwRs6vCp-lDOt9UajvQII0lswasGv6QFcs-QJs_ChUI"
    url = f"https://trefle.io/api/v1/plants/search?token={token}&q={plant_name}"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        for plant in data['data']:
            print("🔍 Name: ", plant['common_name'])
            print("🌱 Scientific name: ", plant['scientific_name'])
            print("☠️ Toxicity: ", plant.get('toxicity', "safe"))
            print("🖼️ Picture: ", plant.get('image_url', "no picture"))
    else:
        print("error", response.status_code)
        print(response.text)
model = MobileNetV2(weights='imagenet',include_top=False, input_shape=(224, 224, 3))  
app = Flask(__name__)
UPLOAD_FOLDER = 'static/uploads'
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/result', methods=['POST'])
def result():
    image = request.files['image']
    filepath = os.path.join(UPLOAD_FOLDER, image.filename)
    image.save(filepath)
    


    prediction = "this is cat"  
    return render_template("result.html", prediction=prediction, filename=image.filename)

if __name__ == '__main__':
    app.run(debug=True)




