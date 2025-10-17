# WORKING WITH FAKE STORE API DATASET
https://fakestoreapi.com/

## 1. set up project folder and git repo
- create a folder where you will work on
- set up remote git repo, so you can avoid the working on different machines problem

## 2. create and activate python virtual environment
- Create an virtual environment is recommended (self-contained Python workspace). It allows each projects to have a different Python version, dependencies and packages.
	```bash 
	python -m venv .venv
	```
- Activate it in Git Bash (which I use)
	- check with your folder, if .venv has /Script or /bin
	- for me it's /Script:	
		```bash	
		source .venv/Scripts/activate	
		```
	- promt should return with (.venv) like this	
		```markdown
		(.venv)
		Trang Pham@Trang
		```
- check Python verison: 
	```bash
	python --version
	which python
	``` 
	should point to python version in
	```python
	.venv/Scripts/python
	```
## 3. install required packages.
- install the required packages in a requirements.txt file.
	```bash
	pip install --upgrade pip
	pip install -r requirement.txt
	```

## 4. scripts
- fetch_data.py: to fetch all the products data
- transform_data.py: clean up and transform to correct type for each data type
- analysis.py: calculate the KPI and show graph

=> Run the scripts:
```python
python *.py
```
## 5. save your installed packages in the current python env
Every working session, when you upgrade or install new packages necessary for your work, free it. 
```python
pip freeze > requirements.txt
```
This allows you to work on another machine or someone else to recreate a similar env necessary for the files to run
```python
python -m venv .venv
source .venv/Scripts/activate
pip install -r requirements.txt
```

