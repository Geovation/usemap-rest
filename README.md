# UseMap REST services

Services to support UseMap application, deployed as a Python Flask API.

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

### Prerequisites

Requirements for the software and other tools to build, test and push. These should be installed on your local computer.

- [Python 3](https://www.python.org/downloads/)
- [Pip](https://pypi.org/project/pip/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)
- [Flask](https://flask.palletsprojects.com/en/2.1.x/)

## Installing

The project uses a Pipfile to define dependencies. Before running, ensure the required dependencies are installed for your virtual environment.

```console
pipenv install
```

## Running

The project can be run locally with the included shell file.

```console
  ./bootstrap.sh
```

Ensure you set your OS API key within your local environment. A copy of `.env.sample` can be taken and named `.env` - the API key should be entered in that file in the `os_api_key` line.

## API documentation

### Endpoint: /places/<search>

Returns place search results

`/places/<search>`

| URL parameter | Description                          |
| ------------- | ------------------------------------ |
| search        | An address search term e.g. SO16 0AS |

The returned data is an array of places that match the search term, currently limited to 30 results.

```json
[
  {
    "ADDRESS": "ORDNANCE SURVEY, 4, ADANAC DRIVE, NURSLING, SOUTHAMPTON, SO16 0AS",
    "BLPU_STATE_CODE": "2",
    "BLPU_STATE_CODE_DESCRIPTION": "In use",
    "BLPU_STATE_DATE": "01/09/2010",
    "BUILDING_NUMBER": "4",
    "CLASSIFICATION_CODE": "CO01GV",
    "CLASSIFICATION_CODE_DESCRIPTION": "Central Government Service",
    "COUNTRY_CODE": "E",
    "COUNTRY_CODE_DESCRIPTION": "This record is within England",
    "DELIVERY_POINT_SUFFIX": "1A",
    "DEPENDENT_LOCALITY": "NURSLING",
    "ENTRY_DATE": "01/09/2010",
    "LANGUAGE": "EN",
    "LAST_UPDATE_DATE": "31/03/2020",
    "LOCAL_CUSTODIAN_CODE": 1760,
    "LOCAL_CUSTODIAN_CODE_DESCRIPTION": "TEST VALLEY",
    "LOGICAL_STATUS_CODE": "1",
    "MATCH": 1.0,
    "MATCH_DESCRIPTION": "EXACT",
    "ORGANISATION_NAME": "ORDNANCE SURVEY",
    "POSTAL_ADDRESS_CODE": "D",
    "POSTAL_ADDRESS_CODE_DESCRIPTION": "A record which is linked to PAF",
    "POSTCODE": "SO16 0AS",
    "POST_TOWN": "SOUTHAMPTON",
    "RPC": "2",
    "STATUS": "APPROVED",
    "THOROUGHFARE_NAME": "ADANAC DRIVE",
    "TOPOGRAPHY_LAYER_TOID": "osgb1000002682081995",
    "UDPRN": "52126562",
    "UPRN": "200010019924",
    "X_COORDINATE": 437292.43,
    "Y_COORDINATE": 115541.95
  }
]
```

## Deployment

### Development deploy to PythonAnywhere

[PythonAnywhere](https://www.pythonanywhere.com/) is a service that provides easy means to host Python in the Cloud.

1. Set up an account and add a new web app.
2. Using a bash console within PythonAnywhere, `git clone` this solution to pull down the latest code.
3. Edit the default wsgi file for your application to be the following (ensure you edit the project directory path)

```python
import sys
import os
from dotenv import load_dotenv

project_folder = os.path.expanduser('~/usemap-rest')  # adjust as appropriate
load_dotenv(os.path.join(project_folder, '.env'))

# add your project directory to the sys.path
project_home = '/home/youraccountname/usemap-rest'
if project_home not in sys.path:
    sys.path = [project_home] + sys.path

# import flask app but need to call it "application" for WSGI to work
from app import app as application  # noqa
```

4. Add the required environment variables to your app (replace `your_os_api_key` with your OS API key!)

```console
cd ~/usemap-rest
echo "os_api_key=your_os_api_key" >> .env
```

More information is available in the 'Using a code sharing site like GitHub or BitBucket' section at [How to get your code in and out of PythonAnywhere](https://help.pythonanywhere.com/pages/UploadingAndDownloadingFiles/).

### Production deploy to AWS

This solution is set up to use [Zappa](https://github.com/zappa/Zappa) to automate deployment to AWS. Zappa maintains:

- The API deployed as an [AWS Lambda](https://aws.amazon.com/lambda/) function
- An [AWS API Gateway](https://aws.amazon.com/api-gateway/) to trigger the Lamda function and provide URL security

On commit to the main branch (e.g. from a Pull Request), the Zappa CLI will run an update to make updates to the production deployment. This is configured with a GitHub action.

## Authors

See the list of
[contributors](https://github.com/Geovation/usemap-rest/contributors)
who participated in this project.

## License

This project is licensed under the [MIT](LICENSE)
License - see the [LICENSE](LICENSE) file for
details

## Acknowledgments

- [Developing RESTful APIs with Python and Flask](https://auth0.com/blog/developing-restful-apis-with-python-and-flask/)
- [How to get your code in and out of PythonAnywhere](https://help.pythonanywhere.com/pages/UploadingAndDownloadingFiles/)
