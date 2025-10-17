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
	- for me it's /Script:	 ```bash	
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
	point to .venv/Scripts/python
	```

## 3. install required packages.
- install the required packages in a requirements.txt file.
	```bash
	pip install --upgrade pip
	pip install -r requirement.txt
	```

## 4. scripts
- fetch_data.py: to fetch all the products data


