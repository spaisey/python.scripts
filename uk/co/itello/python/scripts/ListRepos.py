import os
import requests
from pathlib import Path
from requests.auth import HTTPBasicAuth


def main():
    home = Path(os.environ['HOME'])
    credentials_file = home / '.stashcreds'
    credentials = open(credentials_file, encoding='utf-8').read().rstrip().split(':')
    response = requests.get('https://stash.paypoint.net/rest/api/1.0/projects', auth=HTTPBasicAuth(credentials[0], credentials[1]), verify=False)
    print(response.text)


if __name__ == "__main__":
    main()
