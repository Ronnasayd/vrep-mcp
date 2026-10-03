import pytest

from vrep_mcp import index

pytestmark = pytest.mark.model

TOP_N = 5
EXPECTED = "sim.setJointTargetPosition"


@pytest.fixture(autouse=True)
def real_index(tmp_path, monkeypatch):
    monkeypatch.setenv("VREP_CACHE_DIR", str(tmp_path))
    index._vectors_for.cache_clear()
    yield
    index._vectors_for.cache_clear()


@pytest.mark.parametrize(
    "query",
    [
        pytest.param("set joint target position", id="srch04_english"),
        pytest.param("posição alvo da junta", id="srch05_portuguese"),
    ],
)
def test_search_ranks_set_joint_target_position_in_top_5(query):
    names = [r["name"] for r in index.search(query, max_results=TOP_N)]

    assert EXPECTED in names
