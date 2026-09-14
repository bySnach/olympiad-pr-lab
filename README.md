# Olympiad PR Lab

`Olympiad PR Lab` is a tiny, dependency-free study-planner project for practicing an honest GitHub contribution workflow.

It contains a few isolated, safe functional defects on purpose. They are not security exercises and do not touch networks, files outside the project, credentials, or third-party services. The goal is to choose one scoped problem, prove it with a regression test, fix it, and submit a focused pull request.

## Quick start

Python 3.9 or newer is enough.

```bash
python -m unittest discover -s tests -v
python -m study_planner summary
```

No packages need to be installed.

## For an olympiad participant

1. Read the public product rules in [docs/behavior.md](docs/behavior.md).
2. Choose one open GitHub issue or one card in [docs/task-cards.md](docs/task-cards.md).
3. Fork the repository and create one branch for one problem.
4. Add a regression test that exposes the current behavior.
5. Make the smallest fix that makes the new test pass.
6. Run the test suite and open a pull request that links the issue.

Please keep one issue per pull request. A concise series of independent contributions is more valuable here than one large rewrite.

## Repository map

- `study_planner/` — the deliberately small library and command-line demo.
- `tests/` — green baseline tests; contributors extend these with regression coverage.
- `docs/behavior.md` — expected product behavior.
- `docs/task-cards.md` — scoped contribution ideas without implementation spoilers.
- `CONTRIBUTING.md` — contribution and pull-request rules.

## License

Released under the [MIT License](LICENSE).
