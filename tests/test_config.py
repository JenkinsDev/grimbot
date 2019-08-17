import pytest

from bot.config import Config


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

    def test_load_file_loads_data_into__data(self):
        pass

    def test_load_file_merges_configuration_with__data(self):
        pass

    def test_load_file_raises_an_exception_if_path_does_not_exist(self, monkeypatch):
        with monkeypatch.context() as m:
            m.setattr("bot.config.path.exists", lambda path: False)
            with pytest.raises(FileNotFoundError):
                self.config.load_file(self.faux_config_path)

    def test_load_file_raises_an_exception_if_path_is_not_a_file(self, monkeypatch):
        with monkeypatch.context() as m:
            m.setattr("bot.config.path.isfile", lambda path: False)
            with pytest.raises(FileNotFoundError):
                self.config.load_file(self.faux_config_path)

