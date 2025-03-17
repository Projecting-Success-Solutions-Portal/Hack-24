Instructions on how to run the program

1. Download power_bi_chatbot folder

2. in the .env file, enter your OpenAI API key

3. create a virtual environment in the folder
	python -m venv .venv

4. activate environment:
	source .venv/bin/activate

5. install requirements:
	pip install -r -requirements.txt

6.since there are different installs for pytorch sometimes so:
	pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cu126

7.change directory to chatbot_project
	cd chatbot_project/

8.run development server
	python manage.py runserver

if there are any package installation issues, just follow the console.

excel_to_text.py - turns excel data into txt files
embeddings.py - embeds the txt file into vector space
ai_logic.py - retrieves the relevant contexts and forms an answer
