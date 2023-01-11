# Backend - Techsemester Suggestions API

### Install Dependencies

1. **Python 3.7** - Follow instructions to install the latest version of python for your platform in the [python docs](https://docs.python.org/3/using/unix.html#getting-and-installing-the-latest-version-of-python)

2. **Virtual Environment** - We recommend working within a virtual environment whenever using Python for projects. This keeps your dependencies for each project separate and organized. Instructions for setting up a virual environment for your platform can be found in the [python docs](https://packaging.python.org/guides/installing-using-pip-and-virtual-environments/)

3. **PIP Dependencies** - Once your virtual environment is setup and running, install the required dependencies by navigating to the base directory and running:

Django 3.2 is being used to accomodate deployment on render

```bash
pip install -r requirements.txt
```

### Run the Server

From within the base directory first ensure you are working using your created virtual environment.

To run the server, execute:

```bash
python3 manage.py runserver
```

The `--reload` flag will detect file changes and restart the server automatically.

## Testing

To deploy the tests, run

```bash
python3 manage.py test
```

# API Reference

### Getting Started

- Base URL: At present this app can only be run locally and is not hosted as a base URL. The backend app is hosted at the default, `http://127.0.0.1:8000/`, locally. And on render at https://techsemester-suggestions.onrender.com
- API Documention Url Swagger: `https://techsemester-suggestions.onrender.com/api/v1/docs`
- Authentication: This version of the application does not require authentication or API keys.

### Endpoints

#### GET api/v1/suggestions

- General:
  - Fectches a list of suggestions that match the query q and returns a score is longitude and latitude queries are present. The score is base on how close the suggestion is close to the entered longitude and latitude.
- Sample: `curl http://127.0.0.1:8000/api/v1/suggestions?q=port-au&latitude=32&longitude=20`

```json
{
  "message": "2 Cities",
  "suggestions": [
    {
      "name": "Port-au-Prince, HT",
      "longitude": -72.33881,
      "latitude": 18.54349,
      "score": 0.99
    },
    {
      "name": "Port-aux-Français, TF",
      "longitude": 70.21937,
      "latitude": -49.34916,
      "score": -0.01
    }
  ],
  "status": true
}
```
