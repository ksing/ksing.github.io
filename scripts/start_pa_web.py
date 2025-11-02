from pprint import pprint
from urllib.parse import urljoin

import os
import requests


if __name__ == "__main__":
    api_token = os.environ["PYTHONANYWHERE_API"]
    headers = {"Authorization": f"Token {api_token}"}
    username = "KushS"  # update to match your username!

    pythonanywhere_host = "eu.pythonanywhere.com"  # or "eu.pythonanywhere.com" if your account is hosted on our EU servers
    pythonanywhere_domain = "eu.pythonanywhere.com"  # or "eu.pythonanywhere.com"
    # make sure you don't use this domain already!
    domain_name = f"{username}.{pythonanywhere_domain}"

    api_base = f"https://{pythonanywhere_host}/api/v1/user/{username}/"
    app_dir = f"/home/{username}/ksing.github.io"
    command = (
        f"{app_dir}/.venv/bin/uvicorn "
        f"--app-dir {app_dir}/app "
        "--uds ${DOMAIN_SOCKET} "
        "main:app"
    )

    response = requests.post(
        urljoin(api_base, "websites/"),
        headers=headers,
        json={
            "domain_name": domain_name,
            "enabled": True,
            "webapp": {"command": command}
        },
    )
    pprint(response.json())
