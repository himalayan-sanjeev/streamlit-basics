# [Streamlit CSV Visualizer & Data Generator](https://himalayan-getting-started.streamlit.app/)

An interactive **Streamlit** web app that allows users to:
- **Upload CSV files** and preview their data 
- **Visualize data** using dynamic charts 
- **Generate synthetic datasets** using **Google Gemini AI** 
- **Download generated datasets** as CSV files 

---
## 🖥Running the App

To start the **Streamlit CSV Visualizer & Data Generator**, follow these steps:

###  Clone the Repository
```bash
git clone [https://github.com/himalayan-sanjeev/streamlit-basics]
cd streamlit-basics
```

###  Install dependencies
```bash
pip install -r requirements.txt
```

###  Run the app
```bash
streamlit run app.py
```
This will open the web app in your browser. 

#### Set Up Secrets for Gemini API

Create a ```.streamlit/secrets.toml``` file and add your Google Gemini API Key:

```bash
[api_keys]
gemini = "your-gemini-api-key"
```

#### Generating Data with LLM Bot

    - Go to "Generate Data" from the sidebar.

    - Enter a prompt describing the dataset you want to generate (e.g., "Generate a dataset of 50 employees with Name, Age, Salary, and Department in CSV format").

    - Click "Generate Data" – AI will create a structured dataset.

    - Preview the generated data in a table.

    - Click "Download CSV" to save the generated data.
