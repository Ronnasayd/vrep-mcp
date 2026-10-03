import shutil

import pytest

from vrep_mcp import catalog


@pytest.fixture
def data_dir(tmp_path, monkeypatch):
    for f in catalog._FILES:
        shutil.copy(catalog._data_dir() / f, tmp_path / f)
    monkeypatch.setenv("VREP_DATA_DIR", str(tmp_path))
    return tmp_path
