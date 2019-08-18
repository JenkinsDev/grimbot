from os import path
from dotenv import dotenv_values


class Config:
    """The configuration class wrapper used throughout the application to
    receive necessary config values.

    Properties:
        _data (dict): The underlying configuration object.
    """

    def __init__(self):
        self._data = None

    def __getitem__(self, name):
        if self._data is None or not name in self._data:
            return None

        return self._data[name]

    def merge_config(self, conf_dict):
        """Merges `conf_dict` with `self._data` if `self._data` contains
        configuration values.

        Parameters:
            conf_dict (dict): Configuration dictionary to merge with our data.
        """
        if self._data is None:
            self._data = conf_dict
        else:
            for k, v in conf_dict.items():
                self._data[k] = v

    def load_file(self, config_file):
        """Merges configuration values found within
        the `config_file`.

        Parameters:
            config_file (str): Path to the configuration file.
        """
        if not path.exists(config_file) or not path.isfile(config_file):
            raise FileNotFoundError("file does not exist: {}".format(
                config_file))

        data = self._parse_config_file(config_file)
        self.merge_config(data)

    @staticmethod
    def _parse_config_file(config_file):
        """Wrapper around loading configuration values from a file. We wrap
        the functionality so we may be able to extend it later with other
        file formats. Currently supports .env files.

        Returns:
            Dictionary with loaded configuration values.
        """
        return dotenv_values(config_file)
