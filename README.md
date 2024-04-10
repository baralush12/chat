# LLMs/RAG/Chat-Bots Playground

## What is this?
This repo will be used to learn about LLMs, RAG and Chat-Bots.

## Setting up working environment (one-time setup)

### Installing pyenv (Windows only)
1. Open PowerShell
2. `Invoke-WebRequest -UseBasicParsing -Uri "https://raw.githubusercontent.com/pyenv-win/pyenv-win/master/pyenv-win/install-pyenv-win.ps1" -OutFile "./install-pyenv-win.ps1"; &"./install-pyenv-win.ps1"`

### Installing and setting Python 3.11.6 to pyenv (Windows only)
1. Open cmd
2. `pyenv install 3.11.6`
3. `pyenv global 3.11.6`
4. Verify - `python --version`

### Set and activate virtual env
1. Update pip - `python -m pip install --upgrade pip`
2. Install virtualenv - `pip install virtualenv`
3. `python -m virtualenv .venv`
4. Activate virtual env
   1. Windows - `.venv\Scripts\activate.bat`
   2. Linux - `.venv/bin/activate`
5. Deactivate virtual env
   1. Windows - `.venv\Scripts\deactivate.bat`
   2. Linux - `.venv/bin/deactivate`

## Installing packages and Running

### Install requirements
`pip install -r requirements.txt`

### Run Chat-Bot
`python main.py`
