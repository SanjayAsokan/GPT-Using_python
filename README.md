**GPT - Using Python**

**Project Overview**
This is a Django web application that integrates GPT (Generative Pre-trained Transformer) for natural language processing tasks. 
The app allows users to interact with GPT for various language-based functionalities.

**Prerequisites**
1.Python 3.x
2.SQLite3 (included with Python)

**Installation and Setup**

-Download the project files and navigate to the project directory:
cd project_directory

-Set up a virtual environment:
python3 -m venv venv
--source venv/bin/activate (On Windows, use venv\Scripts\activate)

-Install the dependencies:
pip install -r requirements.txt

-Set up the database:
python manage.py migrate

-Run the development server:
python manage.py runserver

-Access the app by opening your browser and navigating to:
http://127.0.0.1:8000