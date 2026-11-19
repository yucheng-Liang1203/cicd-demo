"""Print the latest pipeline runs of a repository using the GitHub REST API.

Usage:
    export GITHUB_TOKEN=github_pat_...     # fine-grained token, Actions: read
    python scripts/list_runs.py <owner>/<repo>
"""

import os
import sys

import requests

API = "https://api.github.com"


def list_runs(repo: str, token: str, n: int = 5) -> list[dict]:
    headers = {
        "Authorization": f"Bearer {token}",
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    r = requests.get(
        f"{API}/repos/{repo}/actions/runs",
        headers=headers,
        params={"per_page": n},
        timeout=10,
    )
    r.raise_for_status()
    return r.json()["workflow_runs"]


if __name__ == "__main__":
    repo = sys.argv[1] if len(sys.argv) > 1 else "octocat/Hello-World"
    for run in list_runs(repo, os.environ["GITHUB_TOKEN"]):
        print(run["head_sha"][:7], run["event"], run["status"], run["conclusion"])
