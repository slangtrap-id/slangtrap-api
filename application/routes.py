from application import app
from flask import redirect, render_template, url_for, request,session
from application.controller.upload_image import upload_image_controller
from application.controller.predict import predict_controller
import nltk
nltk.download('punkt')

@app.route('/upload_image/<user>', methods=['POST'])
def upload_image_route(user):
    
    return upload_image_controller(user)
    
@app.route('/predict/<user>', methods=['POST'])
def predict_route(user):
    
    return  predict_controller(user)


    


