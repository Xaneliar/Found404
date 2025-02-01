# **Found404**  

## **Movie & TV Show Recommendation System**  

Welcome to the **Movie & TV Show Recommendation System**! This project leverages **machine learning** and **web technologies** to provide personalized recommendations based on user input. Whether you're looking for a thrilling movie or a binge-worthy TV show, this application has got you covered!  

## **Features**  

- **Personalized Recommendations**: Get tailored movie and TV show suggestions based on your input.  
- **Dynamic Image Carousel**: View recommended titles with corresponding images in an interactive carousel format.  
- **User-Friendly Interface**: Simple and intuitive design for seamless navigation.  

## **Tech Stack**  

- **Frontend**: HTML, CSS, JavaScript  
- **Backend**: Flask (Python)  
- **Machine Learning**: Scikit-learn, Pandas, NumPy  
- **APIs**: SerpAPI for fetching images and recommendations  

## **Prerequisites**  

Before you begin, ensure you have the following installed:  

- **Python 3.x**  
- **pip** (Python package installer)  

## **Installation**  

### **1. Clone the Repository**  
```bash
git clone https://github.com/HarishDvs/Found404.git
cd Found404
```

### **2. Install Dependencies**  

**Create a virtual environment:**  
```bash
python -m venv venv
source venv/bin/activate  # On Windows use `venv\Scripts\activate`
```

**Install the required packages:**  
```bash
pip install -r requirements.txt
```

### **3. Set Up API Key**  

- Sign up for **SerpAPI** and obtain your API key.  
- Create a file named `api_key.py` in the root directory and add the following line:  

```python
API_KEY = 'your_api_key_here'
```

### **4. Run the Application**  
```bash
python app.py
```

## **Usage**  

1. Enter a **movie or TV show title** in the input field.  
2. Click the **submit button** to receive personalized recommendations.  
3. Enjoy browsing through the **dynamic carousel of recommendations**!  

## **Contributing**  

Contributions are welcome! If you have suggestions for improvements or new features, feel free to **open an issue** or **submit a pull request**.  

## **License**  

This project is licensed under the **MIT License** – see the `LICENSE` file for details.  

## **Acknowledgments**  

Thanks to the developers of **Flask, Scikit-learn, and SerpAPI** for their amazing tools and resources!  

---
