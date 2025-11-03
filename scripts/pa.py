import os
from pprint import pprint
from typing import Any, Optional
from urllib.parse import urljoin

import click
import requests

USERNAME = "KushS"  # update to match your USERNAME!
PYTHONANYWHERE_HOST = "eu.pythonanywhere.com"  # or "eu.pythonanywhere.com" if your account is hosted on our EU servers
PYTHONANYWHERE_DOMAIN = "eu.pythonanywhere.com"  # or "eu.pythonanywhere.com"
DOMAIN_NAME = f"{USERNAME}.{PYTHONANYWHERE_DOMAIN}"


def run_command(command: str) -> None:
    api_request(
        request_type="POST",
        json_data={
            "domain_name": DOMAIN_NAME,
            "enabled": True,
            "webapp": {"command": command},
        },
    )


def api_request(
    *,
    request_link: str = "websites",
    request_type: str = "GET",
    domain_action: str = "",
    json_data: Optional[dict[str, Any]] = None,
) -> None:
    api_token = os.environ["PYTHONANYWHERE_API"]
    headers = {"Authorization": f"Token {api_token}"}
    api_base = f"https://{PYTHONANYWHERE_HOST}/api/v1/user/{USERNAME}/"
    response = requests.request(
        method=request_type,
        url=urljoin(api_base, f"{request_link}/{domain_action}/"),
        headers=headers,
        json=json_data,
    )
    pprint(response.json())


@click.group()
def main():
    pass


@main.command()
def create_app():
    app_dir = f"/home/{USERNAME}/ksing.github.io"
    command = (
        f"{app_dir}/.venv/bin/uvicorn "
        f"--app-dir {app_dir}/app "
        "--uds ${DOMAIN_SOCKET} "
        "main:app"
    )
    run_command(command)


@main.command()
def list_apps():
    api_request(request_type="GET")


@main.command()
def reload_app():
    api_request(request_type="POST", domain_action=f"{DOMAIN_NAME}/reload")


@main.command()
def encrypt_app():
    api_request(
        request_link="domains",
        domain_action=f"{DOMAIN_NAME}/ssl",
        json_data={"cert_type": "letsencrypt-auto-renew"},
    )


@main.command()
def get_app():
    api_request(request_type="GET", domain_action=DOMAIN_NAME)


@main.command()
def disable_app():
    api_request(request_type="POST", domain_action=DOMAIN_NAME, json_data={"disable": True})


@main.command()
def enable_app():
    api_request(request_type="POST", domain_action=DOMAIN_NAME, json_data={"enable": True})


@main.command()
def delete_app():
    api_request(request_type="DELETE", domain_action=DOMAIN_NAME)


if __name__ == "__main__":
    main()
