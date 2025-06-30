Rice Grain Classifier - Web Application
=======================================

This project is a Deep Learning-based web app that classifies rice grain types using images. 
It uses a Convolutional Neural Network (CNN) model built with MobileNet and served through Flask.

---------------------------------------
📁 Folder Structure:
---------------------------------------
GrainApp/
├── app.py
├── rice_model.h5
├── environment.yml
├── README.txt
│
├── static/
│   └── farmer.jpg
│
└── templates/
    └── index.html

---------------------------------------
💻 Prerequisites:
---------------------------------------
- Anaconda (Python)
- Internet connection (initial setup)
- VS Code / Jupyter Notebook (optional)

Install the required Python packages:
Open Anaconda Prompt and run:
> conda activate riceenv

If not installed already:
> pip install tensorflow==2.3.2  
> pip install keras==2.3.1  
> pip install flask  
> pip install numpy  
> pip install pandas  

---------------------------------------⚙️ How to Run the Project:
---------------------------------------

1. Open Anaconda Prompt.

2. Activate the virtual environment:
> conda activate riceenv

3. Navigate to the project directory:
> cd C:\Users\pnmuk\GrainApp

4. Run the Flask app:
> python app.py

5. Open your web browser and go to:
> http://127.0.0.1:5000

---------------------------------------
🌾 How It Works:
---------------------------------------

- Upload an image of a rice grain using the interface.
- The trained MobileNet model (`rice_model.h5`) will classify it as one of:
  Arborio, Basmati, Brown, Jasmine, Red
- The prediction will appear on the same page along with the image.

---------------------------------------
🎨 Interface Features:
---------------------------------------
- Full-screen background of a farmer (farmer.jpg)
- Centered title: "Welcome to Rice Type Detection"
- Clean upload & prediction form
- Image preview + result display

---------------------------------------
✅ Notes:
---------------------------------------
- Ensure farmer.jpg is placed inside the "static" folder
- Ensure index.html is inside the "templates" folder
- Ensure rice_model.h5 is in the project root folder
- Use .jpg, .png files for uploading rice images

Based on MobileNet CNN Transfer Learning
