import streamlit as st
from keras.models import load_model
from PIL import Image
import numpy as np
from util_chest import classify, set_background
import os 
os.chdir(r"C:\AI APPS\Final project")

def run(): 
    set_background('./bgs/chest.jpg')
    
    # set title

    # upload file
    file = st.file_uploader('', type=['jpeg', 'jpg', 'png'])
    
    # load classifier
    model = load_model('./model_chest/pneumonia_classifier.h5')
    
    # load class names
    with open('./model_chest/labels.txt', 'r') as f:
        class_names = [a[:-1].split(' ')[1] for a in f.readlines()]
        f.close()
    
    # display image
    if file is not None:
        image = Image.open(file).convert('RGB')
        st.image(image, use_column_width=True)
    
        # classify image
        class_name, conf_score = classify(image, model, class_names)
    
        # write classification
        st.write("## {}".format(class_name))
        st.write("### score: {}%".format(int(conf_score * 1000) / 10))
