import logging
import os

import six
import yaml

from obdocs import exceptions


log = logging.getLogger('obdocs.config')


class ValidationError(Exception):
    """Raised during the validation process of the config on errors."""


class Config(six.moves.UserDict):


    def __init__(self, schema):
       

        self._schema = schema
        self._schema_keys = set(dict(schema).keys())
        self.data = {}

        self.user_configs = []
        self.set_defaults()

    def set_defaults(self):
       

        for key, config_option in self._schema:
            self[key] = config_option.default

    def _validate(self):

        failed, warnings = [], []

        for key, config_option in self._schema:
            try:
                value = self.get(key)
                self[key] = config_option.validate(value)
                warnings.extend([(key, w) for w in config_option.warnings])
            except ValidationError as e:
                failed.append((key, e))

        for key in (set(self.keys()) - self._schema_keys):
            warnings.append((
                key, "Unrecognised configuration name: {0}".format(key)
            ))

        return failed, warnings

    def _pre_validate(self):

        for key, config_option in self._schema:
            config_option.pre_validation(self, key_name=key)

    def _post_validate(self):

        for key, config_option in self._schema:
            config_option.post_validation(self, key_name=key)

    def validate(self):

        self._pre_validate()

        failed, warnings = self._validate()

        self._post_validate()

        return failed, warnings

    def load_dict(self, patch):

        if not isinstance(patch, dict):
            raise exceptions.ConfigurationError(
                "The configuration is invalid. The expected type was a key "
                "value mapping (a python dict) but we got an object of type: "
                "{0}".format(type(patch)))

        self.user_configs.append(patch)
        self.data.update(patch)

    def load_file(self, config_file):
        return self.load_dict(yaml.load(config_file))


def _open_config_file(config_file):

    # Default to the standard config filename.
    if config_file is None:
        config_file = os.path.abspath('obdocs.yml')

    log.debug("Loading configuration file: %s", config_file)

    # If it is a string, we can assume it is a path and attempt to open it.
    if isinstance(config_file, six.string_types):
        if os.path.exists(config_file):
            config_file = open(config_file, 'rb')
        else:
            raise exceptions.ConfigurationError(
                "Config file '{0}' does not exist.".format(config_file))

    return config_file


def load_config(config_file=None, **kwargs):
  
    options = kwargs.copy()

    # Filter None values from the options. This usually happens with optional
    # parameters from Click.
    for key, value in options.copy().items():
        if value is None:
            options.pop(key)

    config_file = _open_config_file(config_file)
    options['config_file_path'] = getattr(config_file, 'name', '')

    # Initialise the config with the default schema .
    from obdocs import config
    cfg = Config(schema=config.DEFAULT_SCHEMA)
    # First load the config file
    cfg.load_file(config_file)
    # Then load the options to overwrite anything in the config.
    cfg.load_dict(options)

    errors, warnings = cfg.validate()

    for config_name, warning in warnings:
        log.warning("Config value: '%s'. Warning: %s", config_name, warning)

    for config_name, error in errors:
        log.error("Config value: '%s'. Error: %s", config_name, error)

    for key, value in cfg.items():
        log.debug("Config value: '%s' = %r", key, value)

    if len(errors) > 0:
        raise exceptions.ConfigurationError(
            "Aborted with {0} Configuration Errors!".format(len(errors))
        )
    elif cfg['strict'] and len(warnings) > 0:
        raise exceptions.ConfigurationError(
            "Aborted with {0} Configuration Warnings in 'strict' mode!".format(len(warnings))
        )

    return cfg
