# Sample Recommendation engine with pgvector and langchain

## Deploy via Git

Create an application on https://scalingo.com, then:

```
scalingo --app my-app git-setup
git push scalingo master
```

And that's it!

## Running Locally

Install uv (if not already installed):

```shell
cp .env.example .env
uv sync
uv run uvicorn main:app --host 0.0.0.0 --port 8080
```
