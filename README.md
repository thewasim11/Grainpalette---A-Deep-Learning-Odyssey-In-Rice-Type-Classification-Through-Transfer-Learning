# Grainpalette-a-deep-learning-odyssey-in-rice-type-classification-through-transfer-learning
grainpalette - a deep learning odyssey in rice type classification through transfer learning
# 🌾 GrainPalette – A Deep Learning Odyssey in Rice Type Classification Through Transfer Learning

GrainPalette is a deep learning-based web application that classifies different types of rice grains using a transfer learning model (MobileNetV2). This solution automates rice quality detection and classification using image recognition, supporting farmers, food processing units, and distributors.

---

## 📽️ Demo Video

🎥 [Click to Watch Demo Video on Google Drive](https://drive.google.com/file/d/1bTNDHuM2fZFiwAwXxgC2l0D80T8IBsKu/view?usp=drive_link)

---

## 👨‍💻 Team Members

- **Puchakayala Asritha** – UI/UX Designer  
- **Pithani Narendra Mukhesh** – Full Stack Developer  
- **Pavan Srivastavkokku** – Model Training & Integration  
- **Pinjala Bhu Vardan** – Deployment and Testing  

---

## 🎯 Project Purpose

To develop an intelligent, user-friendly system that can accurately identify rice grain types, reducing the need for manual classification and increasing efficiency in agriculture and food sectors.

---

## ✨ Features

- Upload image of rice grain and get instant classification
- Transfer learning with MobileNetV2 for high accuracy
- Easy-to-use web interface using Flask
- Real-time prediction with image preview
- 5-class rice type detection

---

## 🏗️ Tech Stack

| Layer         | Technology                  |
|--------------|-----------------------------|
| Frontend     | HTML, CSS (Jinja2 with Flask) |
| Backend      | Python, Flask               |
| ML Model     | TensorFlow, Keras (MobileNetV2) |
| Data Handling| Numpy, OpenCV               |
| Dataset      | 5-class Rice Image Dataset  |
| Deployment   | Localhost (Flask)           |

---

## 🛠️ Setup Instructions

### ⚙️ Prerequisites
- Python 3.8+
- TensorFlow
- Flask
- Jupyter Notebook
- Anaconda (recommended)

### 🔧 Installation Steps

# 1. Clone the repository
git clone https://github.com/narendramukhesh-007/grainpalette---a-deep-learning-odyssey-in-rice-type-classification-through-transfer-learning
cd grainpalette...

# 2. Create virtual environment
conda create -n riceenv python=3.8
conda activate riceenv

# 3. Install dependencies
pip install -r requirements.txt

 4. Run the app
python app.py
GrainPalette/
│
├── data/
│   └── Rice_Image_Dataset/
├── templates/
│   └── index.html
├── static/
│   └── (Uploaded images and styling)
├── app.py
├── train.ipynb
├── split_dataset.py
├── class_names.json
├── rice_classifier_v2.h5
└── README.md


Testing
Model trained for 5 epochs with over 99% accuracy

Manual testing of all five rice types

Performance validated with validation split and confusion matrix

🔐 Authentication
No user login for this version. Future versions can include user authentication using Flask sessions or JWT.

🧾 API Overview
Endpoint	Method	Description
/	GET	Loads home page
/predict	POST	Accepts image & returns result

🖼️ Sample UI

(Replace with actual image if needed)

🚧 Known Issues
Some rice types may be misclassified if image quality is poor

Works best with clear, zoomed-in images on white background

🔮 Future Enhancements
Add more rice types to classification

Deploy on cloud (Render, Heroku, or AWS)

Add authentication and user profile history

Build as PWA (Progressive Web App)

📎 Appendix
📁 Google Drive Demo Video

💻 Project Documentation (.docx)

🤖 Dataset: Used 5 rice types — Arborio, Basmati, Jasmine, Ipsala, Karacadag


---

✅ You can now:
- Copy and paste this into your `README.md` on GitHub.
- Or I can generate the updated version and upload it for you if you give access.

Would you like this `README.md` saved as a file for download too?
