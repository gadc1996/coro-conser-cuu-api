# Django Workspace
The main objetive of this repository is to serve as a fullstack django workspace, with integration with Google Cloud services, and powered by dev containers for development

## Development setup
- Create a `.env.dev` file using example
```
cp .env.example .env.dev
```

- Open dev container:

  - For the first time se1tup, you need to rebuild and reopen in a container:
    1. Press `F1` to open the command palette.
    2. Type `Remote-Containers: Rebuild and Reopen in Container` and select it from the dropdown list.

  - For subsequent times, you just need to reopen in a container:
    1. Press `F1` to open the command palette.
    2. Type `Remote-Containers: Reopen in Container` and select it from the dropdown list.

## Interacting with google cloud
The workspace has comes with [Google Cloud Cli](https://cloud.google.com/sdk/docs?hl=es-419), [Cloud SQl Proxy](https://cloud.google.com/sql/docs/mysql/sql-proxy?hl=es-419), and some convenience scripts that can be run using [django-manage](https://docs.djangoproject.com/en/5.0/ref/django-admin/)

### Setting up
- Define GCLOUD env variables, check [.env.example](.env.example) for more information.
- Run setup script
```
manage gcsetup
```


### Setting remote env variables
A set of env variables are required when deploying to google cloud, define all of them in a .env.gcloud file, then run
`manage gcsetenv`