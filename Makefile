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