from click.testing import CliRunner
from hello import search

def test_search():
    runner = CliRunner()
    res = runner.invoke(search, ["--path", ".", "--ftype", "py"])
    assert res.exit_code == 0
    assert ".py" in res.output