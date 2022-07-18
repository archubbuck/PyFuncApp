import json
import logging
import os

import azure.functions as func


def settings():
    settings_file_path = os.path.join(os.path.dirname(__file__), '..', 'appsettings.json')
    print(f'Reading application settings from {settings_file_path}')
    with open(settings_file_path, 'r') as fh:
        return json.load(fh)

app_settings = settings()
print(app_settings)

def main(req: func.HttpRequest) -> func.HttpResponse:
    logging.info('Python HTTP trigger function processed a request.')

    name = req.params.get('name')
    if not name:
        try:
            req_body = req.get_json()
        except ValueError:
            pass
        else:
            name = req_body.get('name')

    if name:
        return func.HttpResponse(f"Hello, {name}. This HTTP triggered function executed successfully. {app_settings['test']}")
    else:
        return func.HttpResponse(
             "This HTTP triggered function executed successfully. Pass a name in the query string or in the request body for a personalized response.",
             status_code=200
        )
