# DSCI Slack Bot

Simple Slack notifications for the Data Science Team.

## Setup

Install [uv](https://docs.astral.sh/uv/getting-started/installation/), then:
```bash
git clone <your-repo-url>
cd <your-repo-name>
uv sync
uv run pre-commit install
```

This code needs the following environment variables to run:

```
SLACK_BOT_TOKEN=""
```

## Development

**Run code:**
```bash
uv run python your_script.py
uv run jupyter lab
uv run marimo edit notebook.py
```

**Code quality:**
```bash
uv run ruff check . --fix  # Lint and auto-fix
uv run ruff format .       # Format code
```

**Add dependencies:**
```bash
uv add package-name        # Runtime
uv add --dev package-name  # Development
```