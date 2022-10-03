# 🔑 Gitlab feature-flags proxy

Simple proxy to access gitlab feature flags without disclosure
personal access token and only with access to specific project.

This proxy will be useful for accessing gitlab feature flags
from various web applications and services whose code is
in the public domain.

Before you start using the script, you must create and fill out a configuration file.
The file must be named config.json and be in the same directory as script.

Example configuration file (config.json):

```json
{
    "gitlab-access-token": "GITLAB_PERSONAL_ACCESS_TOKEN",
    "gitlab-base-url": "gitlab.example.com",
    "gitlab-http-protocol": "https",

    "project-keys": {
        "PROJECT_ID": "PROJECT_ACCESS_KEY"
    }
}
```

After configuration is complete, the web service can be started.
You can access gitlab feature flags with following requests:

```http request
# Get all feature flags for specific project
GET /feature_flags/project_id

# Get specific feature flag (case-sensetive)
GET /feature_flag/project_id/feature_flag_name
```

knownout - https://github.com/knownout/
<br>knownout@hotmail.com