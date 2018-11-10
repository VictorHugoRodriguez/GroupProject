# Group project flask server repository

Sample file showing how to configure and run development server used to connect to plant via websockets and flask

## 1. Python Installation v3

### Windows
 
 - Install python 3 from <a href="https://www.python.org/downloads/windows/" target="_blank">Download page for windows at python.org</a>.  
 - Run the installer.


### Linux

- First check current installed python version.  If version lower than 3.5.6, then install it. 

```shell
sudo apt-get update
sudo apt-get install python3.6
```

## 2. Virtual Environment

- Used to manage dependencies for project and unify python versions for production and development.

### Create environment

- Create a project folder and a venv folder inside.

```shell
mkdir groupproject
cd groupproject
python3 -m venv venv
```

- On Windows: 

```shell
py -3 -m venv venv
```

### Activate Environment

- Before working, activate and start the virtual environment, so any changes and package installs will take effect inside here ( avoid package interference )

```shell
venv/bin/activate
```

- On Windows

```shell
venv\Scripts\activate
```

You should see a different console prompt to know we're now working insive virtual environment

```shell
(venv) groupproject youruser$ ...
```

## 3. Install Libraries and Packages

- While on the virtual environment run following command to install all necessary packages that are included inside the *requirements.txt* file.

```shell
pip install -r requirements.txt
```

## 4. Run project

- First need to inform terminal of app to work with by exporting `FLASK_APP` environment variable.

```shell
export FLASK_APP=hello.py
flask run
    * Running on http://127.0.0.1:5000
```
 - On Windows Command Prompt

 ```shell
C:\path\to\app> set FLASK_APP = "hello.py"
```

- Server should be now running in <a href="127.0.0.1:5000">http://127.0.0.1:5000</a>, or whichever port flask used to run app to see it running.

