# cicd-demo

My first CI/CD pipeline built with GitHub Actions, Docker, and Flask.

## Quickstart

```bash
# Create virtual environment
python -m venv .venv
.venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt -r requirements-dev.txt

# Run lint and tests
ruff check .
pytest -v
```
