# 💰 Personal Finance Assistant (PFA) Chatbot

The **Personal Finance Assistant (PFA) Chatbot** is an intelligent conversational agent designed to assist users with their financial planning needs. Integrated into the [BudgetPro](https://github.com/maharshijani05/BudgetPro) platform, this chatbot leverages advanced machine learning models to provide personalized financial advice, helping users make informed decisions about budgeting, investments, and savings.

## ✨ Features

* **Conversational Financial Guidance**: Engage in natural language conversations to receive tailored financial advice.
* **Machine Learning Integration**: Utilizes trained ML models to analyze user inputs and provide relevant recommendations.
* **MongoDB Support**: Stores and retrieves user data efficiently for a personalized experience.
* **Streamlit Deployment**: Offers an interactive and user-friendly web interface for seamless interactions.
* **Modular Architecture**: Structured codebase for easy maintenance and scalability.

## 📁 Project Structure

```bash
├── personal_finance_chatbot.py   # Core logic for handling chatbot responses
├── streamlit_run.py              # Streamlit app entry point
├── requirements.txt              # Python dependencies
└── LICENSE                       # MIT License
```

## 🛠️ Installation

1. **Clone the Repository**:

   ```bash
   git clone https://github.com/maharshijani05/PFA_CHATBOT.git
   cd PFA_CHATBOT
   ```

2. **Set Up Virtual Environment**:

   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies**:

   ```bash
   pip install -r requirements.txt
   ```

4. **Configure Environment Variables**:
   Create a `.env` file in the root directory and add necessary configurations:

   ```env
   MONGO_URI=your_mongodb_connection_string
   ```

## 🚶‍♂️ Usage

To run the Streamlit application locally:

```bash
streamlit run streamlit_run.py
```

Access the application in your browser at `http://localhost:8501`.

## 🧠 How It Works

* **User Interaction**: Users input financial queries through the Streamlit interface.
* **Processing**: The `personal_finance_chatbot.py` module processes inputs, interacts with the ML model, and fetches relevant data from MongoDB.
* **Response Generation**: Based on analysis, the chatbot formulates and returns personalized financial advice.

## 📆 Dependencies

Key Python packages used:

* `pymongo`
* `streamlit`
* `scikit-learn`
* `xgboost`
* `joblib`
* `python-dotenv`

For a complete list, refer to `requirements.txt`.

## 📄 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## 🤝 Contributing

Contributions are welcome! Please fork the repository and submit a pull request for any enhancements or bug fixes.

## 📬 Contact

For questions or support, please open an issue in the repository.
