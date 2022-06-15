# MapUp REST services

Services to support MapUp application.

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

### Prerequisites

Requirements for the software and other tools to build, test and push.

- [Python 3](https://www.python.org/downloads/)
- [Pip](https://pypi.org/project/pip/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)

## Installing

The project uses a Pipfile to define dependencies.

```console
pipenv install
```

## Running

The project can be run locally with the included shell file.

```console
  ./bootstrap.sh 
```

## Deployment

### Development deploy to PythonAnywhere

[PythonAnywhere](https://www.pythonanywhere.com/)is a service that provides an easy means to host, run and code Python in the Cloud.

1. Set up an account and add a new web app.
2. Using a bash console within PythonAnywhere git clone this solution to pull down the latest code.
3. Edit the default wsgi file for your application to be the following (ensure you edit the project directory path)

```python
import sys
import os
from dotenv import load_dotenv

project_folder = os.path.expanduser('~/mapup-rest')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

# add your project directory to the sys.path
project_home = '/home/youraccountname/mapup-rest/mapup' 
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# import flask app but need to call it "application" for WSGI to work
from index import app as application  # noqa
```

4. Add the required environment variables to your app

```console
cd ~/mapup-rest
echo "export os_api_key=your_os_api_key" >> .env
```

More information is available in the 'Using a code sharing site like GitHub or BitBucket' section at [How to get your code in and out of PythonAnywhere](https://help.pythonanywhere.com/pages/UploadingAndDownloadingFiles/).


## Authors

See the list of
[contributors](https://github.com/Geovation/mapup-rest/contributors)
who participated in this project.

## License

This project is licensed under the [MIT](LICENSE)
License - see the [LICENSE](LICENSE) file for
details

## Acknowledgments

  - [Developing RESTful APIs with Python and Flask](https://auth0.com/blog/developing-restful-apis-with-python-and-flask/)
  - [How to get your code in and out of PythonAnywhere](https://help.pythonanywhere.com/pages/UploadingAndDownloadingFiles/)
