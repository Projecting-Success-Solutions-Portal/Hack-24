# Power BI Chatbot - Documentation

## Project Overview
The **Power BI Chatbot** is a Django-based application that integrates AI-driven responses using OpenAI and ChromaDB embeddings. It processes structured Excel data into text, embeds it into a vector database, and retrieves relevant context for intelligent chatbot interactions.

## File Directory Structure
```
/power_bi_chatbot/
│── chatbot_project/
│   │── chatbot/
│   │   │── __pycache__/
│   │   │── data/
│   │   │── embedded_data/
│   │   │── exported_txt/
│   │   │── migrations/
│   │   │── staticfiles/
│   │   │── templates/
│   │   │── __init__.py
│   │   │── admin.py
│   │   │── ai_logic.py
│   │   │── apps.py
│   │   │── embeddings.py
│   │   │── excel_to_text.py
│   │   │── models.py
│   │   │── tests.py
│   │   │── views.py
│   │
│   │── __pycache__/
│   │── __init__.py
│   │── asgi.py
│   │── settings.py
│   │── urls.py
│   │── wsgi.py
│
│── db.sqlite3
│── manage.py
│── dot-env
│── README.txt
│── requirements.txt
```

## Specific Files & Descriptions
### **Django Core Files**
- **`manage.py`**: Django's command-line utility for administrative tasks【50†source】.
- **`settings.py`**: Configuration settings including database, middleware, and OpenAI API key【37†source】.
- **`urls.py`**: Defines URL patterns and maps views to endpoints【48†source】.
- **`wsgi.py`**: WSGI configuration for server deployment【49†source】.
- **`asgi.py`**: ASGI configuration for asynchronous capabilities【36†source】.

### **Chatbot Functionality**
- **`ai_logic.py`**: AI-powered chatbot logic, using OpenAI and ChromaDB for intelligent responses【29†source】.
- **`embeddings.py`**: Processes and stores text data as embeddings for efficient AI retrieval【31†source】.
- **`excel_to_text.py`**: Converts structured Excel sheets (`Risks`, `Mitigations`) into cleaned text files for processing【32†source】.

### **Django App Structure**
- **`admin.py`**: Placeholder for Django admin site registration【28†source】.
- **`apps.py`**: Defines the chatbot Django app configuration【30†source】.
- **`models.py`**: Placeholder for database model definitions【33†source】.
- **`tests.py`**: Placeholder for Django unit tests【34†source】.
- **`views.py`**: Handles chatbot user requests and calls AI logic for responses【35†source】.

### **Configuration & Setup**
- **`dot-env`**: Stores environment variables such as the OpenAI API key. Keep this file secure.
- **`requirements.txt`**: Lists all Python dependencies required to run the project.

### **Project Documentation**
- **`README.txt`**: Contains setup instructions, including:
  - Creating a virtual environment
  - Installing dependencies
  - Running the Django server
  - Overview of key scripts【52†source】.

## Installation & Setup Guide
### **1. Clone the Project**
```sh
$ git clone <repository-url>
$ cd power_bi_chatbot
```

### **2. Set Up the Virtual Environment**
```sh
$ python -m venv .venv
$ source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### **3. Install Dependencies**
```sh
$ pip install -r requirements.txt
```

### **4. Configure Environment Variables**
- Create a `.env` file and enter your OpenAI API key:
```sh
OPENAI_API_KEY=your-api-key-here
```

### **5. Run the Django Development Server**
```sh
$ cd chatbot_project/
$ python manage.py runserver
```

## Info
This documentation was created as part of **Project:Hack** – a hackathon run by **Projecting Success** for the Project Data Analytics community.
