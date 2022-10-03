import json

import requests


class ConfigProvider:
    __config: dict = {}

    def __init__(self):
        config_file = open("config.json", encoding="utf-8")

        self.__config = json.loads(config_file.read())

        config_file.close()

    def verify_project_key(self, project: str, key):
        try:
            return self.__config["project-keys"][project] == key
        except:
            return False

    def get_gitlab_feature_flags(self, project: str):
        gitlab_http_protocol = self.__config['gitlab-http-protocol']
        gitlab_base_url = self.__config['gitlab-base-url']

        gitlab_api_url = f"{gitlab_http_protocol}://{gitlab_base_url}/api/v4/projects/{project}/feature_flags"

        return requests.get(gitlab_api_url, headers={
            "PRIVATE-TOKEN": self.__config['gitlab-access-token']
        }).json()

    def get_feature_flag(self, project: str, flag: str):
        return list(filter(lambda x: x["name"] == flag, self.get_gitlab_feature_flags(project)))[0]