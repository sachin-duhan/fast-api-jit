# auth_jit
Just-in-Time (JIT) authentication using tokens for backend APIs

## Poetry
This project uses poetry. It's a modern dependency management tool.

To run the project use this set of commands:

```bash
# optional -> virtual env
cp .env.example .env
make install
make run
```

This will start the server on the configured host.

You can find swagger documentation at `/api/docs`.

You can read more about poetry here: https://python-poetry.org/

## Docker

You can start the project with docker using this command:

```bash
docker-compose -f docker/docker-compose.yml --project-directory . up --build
```

If you want to develop in docker with autoreload add `-f docker/docker-compose.dev.yml` to your docker command.
Like this:

```bash
docker-compose -f docker/docker-compose.yml -f docker/docker-compose.dev.yml --project-directory . up --build
```

This command exposes the web application on port 8000, mounts current directory and enables autoreload.

But you have to rebuild image every time you modify `poetry.lock` or `pyproject.toml` with this command:

```bash
docker-compose -f docker/docker-compose.yml --project-directory . build
```

## Project structure

```bash
$ tree "auth_jit"
auth_jit
├── conftest.py  # Fixtures for all tests.
├── __main__.py  # Startup script. Starts uvicorn.
├── services  # Package for different external services such as rabbit or redis etc.
├── settings.py  # Main configuration settings for project.
├── static  # Static content.
├── tests  # Tests for project.
└── web  # Package contains web server. Handlers, startup config.
    ├── api  # Package with all handlers.
    │   └── router.py  # Main router.
    ├── application.py  # FastAPI application configuration.
    └── lifetime.py  # Contains actions to perform on startup and shutdown.
```

## Configuration

This application can be configured with environment variables.

You can create `.env` file in the root directory and place all
environment variables here.

All environment variables should start with "AUTH_JIT_" prefix.

For example if you see in your "auth_jit/settings.py" a variable named like
`random_parameter`, you should provide the "AUTH_JIT_RANDOM_PARAMETER"
variable to configure the value. This behaviour can be changed by overriding `env_prefix` property
in `auth_jit.settings.Settings.Config`.

An example of .env file:
```bash
AUTH_JIT_RELOAD="True"
AUTH_JIT_PORT="8000"
AUTH_JIT_ENVIRONMENT="dev"
```

You can read more about BaseSettings class here: https://pydantic-docs.helpmanual.io/usage/settings/
## OpenTelemetry

If you want to start your project with OpenTelemetry collector
you can add `-f ./docker/docker-compose.otlp.yml` to your docker command.

Like this:

```bash
docker-compose -f docker/docker-compose.yml -f docker/docker-compose.otlp.yml --project-directory . up
```

This command will start OpenTelemetry collector and jaeger.
After sending a requests you can see traces in jaeger's UI
at http://localhost:16686/.

This docker configuration is not supposed to be used in production.
It's only for demo purpose.

You can read more about OpenTelemetry here: https://opentelemetry.io/

## Pre-commit

To install pre-commit simply run inside the shell:
```bash
pre-commit install
```

pre-commit is very useful to check your code before publishing it.
It's configured using .pre-commit-config.yaml file.

By default it runs:
* black (formats your code);
* mypy (validates types);
* isort (sorts imports in all files);
* flake8 (spots possible bugs);


You can read more about pre-commit here: https://pre-commit.com/


## Running tests

If you want to run it in docker, simply run:

```bash
docker-compose -f docker/docker-compose.yml -f docker/docker-compose.dev.yml --project-directory . run --build --rm api pytest -vv .
docker-compose -f docker/docker-compose.yml -f docker/docker-compose.dev.yml --project-directory . down
```

For running tests on your local machine.


2. Run the pytest.
```bash
pytest -vv .
```
