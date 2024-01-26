from flask import Flask, request, jsonify
import tensorflow as tf
import numpy as np
import requests
from io import BytesIO

app = Flask(__name__)

model_path = '/Users/rohitjadhav/Desktop/Personal/nsfw-image-detection/models/nsfw_model.h5'
model = tf.keras.models.load_model(model_path)

class_names = ['hentai', 'neutral', 'porn', 'sexy']

@app.route('/upload_images', methods=['POST'])
def upload_images():
    data = request.get_json()
    image_urls = data.get('images', [])

    filteredImages = []

    for image_url in image_urls:

        try:
            response = requests.get(image_url)

            if response.status_code == 200:

                img = tf.keras.utils.load_img(BytesIO(response.content), target_size=(180, 180))
                img_array = tf.keras.utils.img_to_array(img)
                img_array = np.expand_dims(img_array, axis=0)

                predictions = model.predict(img_array)
                score = tf.nn.softmax(predictions[0])
                class_name = class_names[np.argmax(score)]
                print(class_name)
                confidence = 100 * np.max(score)

                if class_name != "neutral":
                    filteredImages.append(image_url)
            else:
                continue
        except Exception as e:
            continue

    print(filteredImages)

    return jsonify({"filteredImages": filteredImages})

if __name__ == '__main__':
    app.run(debug=True)
