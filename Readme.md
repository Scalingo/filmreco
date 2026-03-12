# Sample Recommendation engine with pgvector and langchain

## Deploy via Git

Create an application on https://scalingo.com, then:

```
scalingo --app my-app git-setup
git push scalingo master
```

And that's it!

## Deploy in One Click

[![Deploy to Scalingo](https://cdn.scalingo.com/deploy/button.svg)](https://my.osc-fr1.scalingo.com/deploy?source=https://github.com/Scalingo/filmreco)

## Running Locally

```shell
docker compose up --build
```
The app listens by default on the port 8080