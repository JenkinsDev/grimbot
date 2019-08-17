import pytest

from unittest.mock import MagicMock
from bot.config import Config


faux_configuration_str = """
ENVIRONMENT=unknown
SECRET=xyz
RANDOM=101
"""

faux_configuration_dict = {
    "ENVIRONMENT": "unknown",
    "SECRET": "xyz",
    "RANDOM": "101"
}

@pytest.fixture()
def faux_config_file(tmpdir):
    p = tmpdir.mkdir("grimbot").join(".env.testing")
    p.write(faux_configuration_str)
    return p.strpath


def mock_config_values(config_path):
    return {"mock_key": "mock_value", "path": config_path}


class TestConfig:

    def setup(self):
        self.faux_config_path = "/opt/grimbot/.env"
        self.config = Config()

    def test_initializes_with_empty_data(self):
        assert self.config._data is None

    def test__parse_config_file_calls_dotenv_values(self, monkeypatch):
        with monkeypatch.context() as m:
            m.setattr("bot.config.dotenv_values", mock_config_values)
            data = self.config._parse_config_file(self.faux_config_path)
            assert "mock_key" in data
            assert data.get("path") is self.faux_config_path

    def test_load_file_raises_an_exception_if_path_does_not_exist(self, monkeypatch):
        with monkeypatch.context() as m:
            m.setattr("bot.config.path.exists", lambda path: False)
            with pytest.raises(FileNotFoundError):
                self.config.load_file(self.faux_config_path)

    def test_load_file_raises_an_exception_if_path_is_not_file(self, monkeypatch):
        with monkeypatch.context() as m:
            m.setattr("bot.config.path.isfile", lambda path: False)
            with pytest.raises(FileNotFoundError):
                self.config.load_file(self.faux_config_path)

    def test_load_file_calls__parse_config_file(self, faux_config_file):
        self.config._parse_config_file = MagicMock()
        self.config.load_file(faux_config_file)
        self.config._parse_config_file.assert_called_once_with(faux_config_file)

    def test_merge_config_replaces_config_if__data_is_none(self):
        config = {'secret': '$3(r37'}
        assert self.config._data is None
        self.config.merge_config(config)
        assert self.config._data is config

    def test_merge_config_merges_supplied_dict_with__data(self):
        # We load our _data object with some starting data. We expect NEW to
        # be unchanged and ENVIRONMENT to be changed from production to
        # 'unknown'.
        expected = [
            ('ENVIRONMENT', 'unknown'),
            ('SECRET', 'xyz'),
            ('RANDOM', '101'),
            ('NEW', True)
        ]
        self.config._data = {'ENVIRONMENT': 'production', 'NEW': True}
        self.config.merge_config(faux_configuration_dict)
        for key, value in expected:
            assert key in self.config._data
            assert value == self.config._data[key]
