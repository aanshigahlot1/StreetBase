# 🏠 streetBase: AI-Automated Real Estate Ecosystem

**streetBase** is an end-to-end AI application designed to revolutionize property valuation. By combining high-precision predictive modeling with Generative AI and NLP-driven market insights, this application bridges the gap between complex data science and user-centric real estate decisions.

---

## 🚀 Live Links
* **Live Web App:** [https://streetbase-7cklxuyaukme8j2uwxjbi8.streamlit.app/](https://streetbase-7cklxuyaukme8j2uwxjbi8.streamlit.app/)
* **GitHub Repository:** [https://github.com/aanshigahlot1/StreetBase](https://github.com/aanshigahlot1/StreetBase)

---

## 🛠️ Project Roadmap & Technical Milestones

### Phase 1: The Predictive Engine (Machine Learning)
The core of streetBase is a robust predictive model built through a rigorous data science pipeline:
* **Data Engineering**: Gathered housing datasets including critical features such as location, area size, room count, and year built.
* **Data Preprocessing**: Implemented comprehensive cleaning to handle missing values, remove outliers, and correct inconsistencies.
* **Feature Engineering**: Utilized categorical encoding and data normalization to optimize model performance.
* **The Champion Model**: **XGBoost** emerged as the top performer with a near-perfect **$R^2$ score of 0.998**.



[Image of machine learning model development lifecycle]


### Phase 2: User Interface & User Experience (UI/UX)
Transformed the trained model into a functional web application using **Streamlit**:
* **Interactive Inputs**: A user-friendly form allows users to enter property details for instant valuations.
* **Financial Toolkit**: Integrated an **EMI Calculator** to assist users in financial planning.
* [cite_start]**Visual Insights**: Dynamic charts illustrating feature importance and market trends powered by Matplotlib and Seaborn [cite: 53-56].

### Phase 3: Advanced Intelligence (GenAI & NLP)
Elevated the platform by integrating advanced AI capabilities:
* **LLM-Powered Chatbot**: Integrated Large Language Models (LLMs) to provide real-time conversational support.
* **NLP News Analysis**: Developed an AI-based news aggregator that uses Natural Language Processing (NLP) to analyze real estate headlines and identify market sentiment.
* **Cloud Deployment**: Fully hosted on **Streamlit Cloud** for global accessibility.

---

## 💻 Tech Stack
* **Language**: Python
* **Frontend/Deployment**: Streamlit
* **Machine Learning**: Scikit-learn, XGBoost, Random Forest, Linear Regression, and Decision Trees
* **Generative AI & NLP**: LLM Integration, NLTK/Spacy
* **Data Analysis**: Pandas, NumPy
* **Visualization**: Matplotlib, Seaborn 

---

## 📊 Model Performance Comparison
Based on our Milestone 1 evaluation metrics:

| Model | R-squared ($R^2$) | Mean Absolute Error (MAE) | Root Mean Squared Error (RMSE) |
| :--- | :--- | :--- | :--- |
| **XGBoost** | **0.998497** | **4.005733** | **5.554039** |
| Random Forest | 0.999655 | 1.734897 | 2.661745 |
| Decision Tree | 0.997794 | 4.645705 | 6.729634 |
| Linear Regression | 0.467310 | 84.848490 | 104.564961 |

---

## ⚙️ Installation & Setup

To run streetBase locally, follow these steps exactly:

1. **Clone the repository**:
   ```bash
   git clone [https://github.com/aanshigahlot1/StreetBase.git](https://github.com/aanshigahlot1/StreetBase.git)
2. **Navigate to the project directory**:
   ```bash
   cd StreetBase
3. **Install dependencies**:
  ```bash
  pip install -r requirements.txt
4. **Run the application**:
  ```bash
  streamlit run app.py

 ## 👤 Author
**Aanshi Gahlot**

