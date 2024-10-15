# Trip-Planner-CrewAI
This is my first project in crewai by creating a trip planner which i followe from this tutorial: <br>
[codewithbrandon video](https://www.youtube.com/watch?v=sPzc6hMg7So)
<br>
## How to run it
clone my repository
```
git clone https://github.com/KomangAndika/Trip-Planner-CrewAI.git
```
<br>

cd into the folder
```{bash}
cd starter_template
```
<br>

open it in vscode with
```
code .
```
<br>

Because we will be installing library from the pyproject.toml we need poetry to run it<br>
To run poetry you need pipx
```
brew install pipx
pipex ensurepath
```
<br>

Install poetry
```
pipx install poetry
```
<br>

To check if poetry installed or checking poetry version
```
poetry --version
```
<br>

Installing the libraries from pyproject.toml
```
poetry --no-root
```
<br>

Checking the environment list
```
poetry env list
```
<br>

Running the virtual environment
```
poetry shell
```
<br>

Don't forget to install streamlit
```
pip install streamlit
```
<br>

To start the code
```
streamlit run app.py
```





