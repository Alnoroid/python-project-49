install:
	uv sync

build:
	uv build

brain-games:
	uv run brain-games

package-install:
	uv tool install dist/*.whl

package-reinstall:
	uv tool install --reinstall dist/*.whl

lint:
	uv run ruff check brain_games

lint_fix:
	uv run ruff check brain_games --fix