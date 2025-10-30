# Scenarios for Coding Agent Evaluation

Use these ready-to-run scenarios to evaluate refactoring, tests, bug fixes, docs, hygiene, and more.

---

## Scenario A — Refactor & Modernize
**Issue title:** Refactor deprecated_sum to a modern implementation and rename to sum_ints  
**Acceptance criteria:**
- Replace manual loop with built-in `sum`.
- Rename function and update all references.
- Add/adjust tests.
- Pass CI and keep style consistent.

---

## Scenario B — Add Unit Tests for `models` and `cli`
**Issue title:** Increase unit test coverage for models.py and cli.py  
**Acceptance criteria:**
- New tests for `User.display()` and CLI `--help` / basic run.
- Keep tests isolated and fast.
- Pass CI.

---

## Scenario C — Fix Bug: input validation in process_data
**Issue title:** process_data(None) should raise ValueError with a helpful message  
**Acceptance criteria:**
- Validate input type in `process_data`.
- Raise `ValueError` with message when `values` is None.
- Add/update tests accordingly.

---

## Scenario D — Add logging
**Issue title:** Add structured logging to app.py and cli.py  
**Acceptance criteria:**
- Use Python `logging` (INFO default).
- Include timestamps and module name.
- Replace `print` calls.

---

## Scenario E — Retries & Backoff
**Issue title:** Add retries with exponential backoff to ApiClient.get_json  
**Acceptance criteria:**
- Configurable attempts & jitter.
- Retry on connection/timeouts/5xx.
- Unit tests using monkeypatch.
- Update README with usage example.

---

## Scenario F — Code hygiene
**Issue title:** Remove unused imports, add ruff, and enforce style  
**Acceptance criteria:**
- Ensure ruff config is respected.
- Clean imports and formatting.
- CI remains green.
