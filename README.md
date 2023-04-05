# UseMap REST services

Services to support UseMap application, deployed as a Python Flask API.

## Getting Started

These instructions will give you a copy of the project up and running on
your local machine for development and testing purposes. See deployment
for notes on deploying the project on a live system.

## Prerequisites

Requirements for the software and other tools to build, test and push. These should be installed on your local computer.

- [Python 3](https://www.python.org/downloads/)
- [Pip](https://pypi.org/project/pip/)
- [Pipenv](https://pipenv.pypa.io/en/latest/)

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

Ensure you set your OS API key within your local environment. A copy of `.env.sample` can be taken and renamed to `.env` - the API key should be entered in that file in the `os_api_key` line.

The environment file also allows for cross origin resource sharing to be configured. Enter the value you require (e.g. `*` or `http://localhost:3000`) for the `cors_origin` variable.

## API documentation

### Endpoint: /features/toid/<toid>

Returns building information based on the Topographic Identifier (TOID)

`/features/toid/<toid>`

| URL parameter | Description                                       |
| ------------- | ------------------------------------------------- |
| toid          | An Ordnance Survey TOID e.g. osgb0000045763621288 |

The returned data is a set of information about a specific building, including its geometry (shape on a map) and area in square meters

```json
{
  "type": "FeatureCollection",
  "crs": {
    "type": "name",
    "properties": {
      "name": "EPSG:4326"
    }
  },
  "features": [
    {
      "type": "Feature",
      "geometry": {
        "type": "MultiPolygon",
        "coordinates": [
          [
            [
              [50.93857733, -1.47089411],
              [50.9385768, -1.4708944]
            ]
          ]
        ]
      },
      "properties": {
        "GmlID": "Topography_TopographicArea.61885403",
        "OBJECTID": 61885403,
        "TOID": "osgb1000002682081995",
        "Theme": "Buildings",
        "CalculatedAreaValue": 6871.498608,
        "ChangeDate": "5/10/2022",
        "DescriptiveGroup": "Building"
      }
    }
  ]
}
```

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

### Endpoint: /places/toid/<toid>

Returns place information for a building by passing its Topographic Identifier (TOID)

`/places/toid/<toid>`

| URL parameter | Description                                       |
| ------------- | ------------------------------------------------- |
| toid          | An Ordnance Survey TOID e.g. osgb0000045763621288 |

Returns a format identical to the search endpoint, but uses a building's unique TOID instead of a query. To be used if a building is already known (e.g. when clicked on the map)

```json
[
  {
    "UPRN": "200010019924",
    "UDPRN": "52126562",
    "ADDRESS": "ORDNANCE SURVEY, 4, ADANAC DRIVE, NURSLING, SOUTHAMPTON, SO16 0AS",
    "ORGANISATION_NAME": "ORDNANCE SURVEY",
    "BUILDING_NUMBER": "4",
    "THOROUGHFARE_NAME": "ADANAC DRIVE",
    "DEPENDENT_LOCALITY": "NURSLING",
    "POST_TOWN": "SOUTHAMPTON",
    "POSTCODE": "SO16 0AS",
    "RPC": "2",
    "X_COORDINATE": 437292.43,
    "Y_COORDINATE": 115541.95,
    "STATUS": "APPROVED",
    "LOGICAL_STATUS_CODE": "1",
    "CLASSIFICATION_CODE": "CO01GV",
    "CLASSIFICATION_CODE_DESCRIPTION": "Central Government Service",
    "LOCAL_CUSTODIAN_CODE": 1760,
    "LOCAL_CUSTODIAN_CODE_DESCRIPTION": "TEST VALLEY",
    "COUNTRY_CODE": "E",
    "COUNTRY_CODE_DESCRIPTION": "This record is within England",
    "POSTAL_ADDRESS_CODE": "D",
    "POSTAL_ADDRESS_CODE_DESCRIPTION": "A record which is linked to PAF",
    "BLPU_STATE_CODE": "2",
    "BLPU_STATE_CODE_DESCRIPTION": "In use",
    "TOPOGRAPHY_LAYER_TOID": "osgb1000002682081995",
    "LAST_UPDATE_DATE": "31/03/2020",
    "ENTRY_DATE": "01/09/2010",
    "BLPU_STATE_DATE": "01/09/2010",
    "LANGUAGE": "EN",
    "MATCH": 1.0,
    "MATCH_DESCRIPTION": "EXACT",
    "DELIVERY_POINT_SUFFIX": "1A"
  }
]
```

### Endpoint: /linkedids/uprn/<uprn>

Returns linked ID information for a Unique Property Reference Number (UPRN)

`/features/toid/<toid>`

| URL parameter | Description                                         |
| ------------- | --------------------------------------------------- |
| urpn          | A Unique Property Reference Number e.g. 10094608166 |

The returned data is a set of correlated IDs for the property

```json
{
  "correlations": [
    {
      "correlatedFeatureType": "Street",
      "correlatedIdentifierType": "USRN",
      "correlatedIdentifiers": [
        {
          "confidence": "Version information is correct",
          "correlationIdentifier": "BLPU_10094608166_Street_21604971_11",
          "identifier": "21604971",
          "versionDate": "2016-02-10"
        }
      ],
      "correlationMethodIdentifier": "BLPU_UPRN_Street_USRN_11",
      "searchedIdentifierVersionDate": "2019-01-31"
    },
    {
      "correlatedFeatureType": "RoadLink",
      "correlatedIdentifierType": "TOID",
      "correlatedIdentifiers": [
        {
          "confidence": "Version information is correct",
          "correlationIdentifier": "BLPU_10094608166_RoadLink_osgb4000000030239787_9",
          "identifier": "osgb4000000030239787",
          "versionDate": "2017-04-15"
        }
      ],
      "correlationMethodIdentifier": "BLPU_UPRN_RoadLink_TOID_9",
      "searchedIdentifierVersionDate": "2019-01-31"
    },
    {
      "correlatedFeatureType": "TopographicArea",
      "correlatedIdentifierType": "TOID",
      "correlatedIdentifiers": [
        {
          "confidence": "Version information is correct",
          "correlationIdentifier": "BLPU_10094608166_TopographicArea_osgb1000005736182_5",
          "identifier": "osgb1000005736182",
          "versionDate": "2019-12-09",
          "versionNumber": 7
        }
      ],
      "correlationMethodIdentifier": "BLPU_UPRN_TopographicArea_TOID_5",
      "searchedIdentifierVersionDate": "2019-01-31"
    }
  ],
  "linkedIdentifier": {
    "featureType": "BLPU",
    "identifier": "10094608166",
    "identifierType": "UPRN"
  }
}
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
[contributors](https://github.com/geovation/usemap-rest/contributors)
who participated in this project.

## License

This project is licensed under the [MIT](LICENSE)
License - see the [LICENSE](LICENSE) file for
details

## Acknowledgments

- [Developing RESTful APIs with Python and Flask](https://auth0.com/blog/developing-restful-apis-with-python-and-flask/)
- [How to get your code in and out of PythonAnywhere](https://help.pythonanywhere.com/pages/UploadingAndDownloadingFiles/)
