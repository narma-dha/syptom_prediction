
#  Symptom Prediction Using NLP

##  Project Overview

The **Symptom Prediction Using NLP** project is a Python-based application that analyzes medical text (such as patient reports or symptom descriptions) to extract **symptoms**, **diagnosis**, and **medicines**, and helps in predicting possible diseases. The project uses **Natural Language Processing (NLP)** techniques to process unstructured medical data.

This project is suitable for **academic purposes**, especially for **2nd–3rd year engineering students**, and demonstrates the real-world use of NLP in healthcare.

-------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

## Objectives

* Extract meaningful medical information from text or PDF files
* Identify patient symptoms automatically using NLP
* Predict possible diseases based on extracted symptoms
* Reduce manual effort in analyzing medical reports
* Demonstrate the application of NLP in healthcare systems

-------------------------------------------------------------------------------------------------------------------------------------------

## Technologies Used

* **Programming Language:** Python
* **Libraries & Tools:**

  * NLTK (Natural Language Toolkit)
  * PyPDF2 (for PDF text extraction)
  * re (Regular Expressions)
  * pandas (optional, for data handling)
* **IDE:** VS Code / PyCharm
* **Dataset:** Predefined symptom–disease mapping (CSV or dictionary-based)

------------------------------------------------------------------------------------------------------

## System Architecture

1. Input Medical Text / PDF
2. Text Extraction (PyPDF2)
3. Text Preprocessing (Tokenization, Cleaning)
4. Symptom Extraction (Keyword-based NLP)
5. Disease Prediction Logic
6. Output Display (Symptoms, Diagnosis, Medicines)

-------------------------------------------------------------------------------------------------------------

## How to Run the Project

### Step 1: Install Required Libraries

```bash
pip install nltk PyPDF2 pandas
```

### Step 2: Download NLTK Data

```python
import nltk
nltk.download('punkt')
```

### Step 3: Provide Input

* Place the medical report PDF inside the `input/` folder
* OR directly enter symptom text in the program

### Step 4: Run the Project

```bash
python main.py
```

---

## Sample Output

```
SYMPTOMS: ['fever', 'cough', 'headache']
PREDICTED DISEASE: Viral Fever
SUGGESTED MEDICINES: Paracetamol, Rest, Fluids
```

--------------------------------------------------------------------------------------------------------------------------------------------------

##  Advantages

* Automates medical text analysis
* Reduces human error
* Easy to understand and modify
* Useful for learning NLP concepts
* Can be extended into a web or mobile application

------------------------------------------------------------------------------------------------------------

## Limitations

* Accuracy depends on dataset quality
* Not a replacement for professional medical diagnosis
* Limited to predefined symptoms and diseases
* No real-time learning (static model)

---------------------------------------------------------------------------------------------------------

##  Future Enhancements

* Integrate Machine Learning / Deep Learning models
* Improve accuracy using larger datasets
* Add a web interface (Flask / Django)
* Support multiple languages
* Connect to real hospital databases

-------------------------------------------------------------------------------------------------------------------
## Author

Narmadhadevi D
B.Tech – Information Technology
St. Joseph’s College of Engineering

------------------------------------------------------------------------------------------------------------------------------------------

## Disclaimer

This project is developed **only for educational purposes** and should not be used for real medical diagnosis or treatment.
                                              
                                            
                                            
  --------------------------XXXXXXXXXXXXXXXX----------
