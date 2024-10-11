# weather_project web app

A web app to view weather data for a location using weatherAPI.com. 

### Getting Started

To get started, let's clone the repo <br>

1. Clone the repo in a folder on your system
```
git clone git@github.com:EbenFuentes/weather_project.git
```
2. Next, open the terminal and cd into weather_project. We have to create a virtual environment to install the project's dependencies. Let's create a virtual environment called "env_weather_proj". In the directory of weather_project, run the following command:
```
python -m venv env_weather_proj
```
3. Next, we need to activate the environment. You can either do this manually or [automatically with VSCode](https://code.visualstudio.com/docs/python/environments#_working-with-python-interpreters). You can set up the python interpreter to activate the virtual environment automatically in VSCode later with the link above. To get started, let's activate the environment manually. In the directory of env_weather_proj, run the following command: <br>

On unix or macOS:

> source bin/activate

On Windows:
> Scripts\activate

4. Now with the virtual environment actiavted, you should see ```(env_weather_proj) (base)``` in your terminal. Let's install the dependencies now. You can cd into the root of the project, weather_project, but the command can be run from anywhere:


```
python -m pip install -r requirements.txt
```

5. To run the project, cd into weather_project/weather_proj_django. Then run:

```
python manage.py runserver
```

The development server runs at http://127.0.0.1:8000/. Currently, the la_view/ endpoind returns the location, current temperature, and current condition for Los Angeles using weatherAPI.





