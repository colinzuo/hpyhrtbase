from typing import Any

from hpyhrtbase import hpyhrt_context


class ConfigUtil:
    @staticmethod
    def decode_invisible_config(orig_value: str, must_exist: bool = True) -> Any:
        """Decode a config value that may be redirected to hide sensitive information.

        If the value starts with the invisible_config_prefix, the actual value
        is stored under the redirected key in config.
        """
        config_inst = hpyhrt_context.get_config_inst()
        invisible_config_prefix = config_inst.invisible_config_prefix

        if orig_value.startswith(invisible_config_prefix):
            to_value = None

            prefix_len = len(invisible_config_prefix)

            config_key = orig_value[prefix_len:]

            if config_key != "" and hasattr(config_inst, config_key):
                to_value = config_inst[config_key]
            elif must_exist:
                raise Exception(f"{config_key} was not configured")

            return to_value
        else:
            return orig_value

    @staticmethod
    def override_config(config: Any, orig_value: str, key_prefix: str) -> tuple[str | None, Any]:
        """Override a config value that may be redirected to hide sensitive information.

        If the value starts with key_prefix, the actual value is stored under
        the redirected key in config.
        """
        if orig_value.startswith(key_prefix):
            to_value = None

            prefix_len = len(key_prefix)

            config_key = orig_value[prefix_len:]

            if config_key != "" and hasattr(config, config_key):
                to_value = config[config_key]

            return config_key, to_value
        else:
            return None, orig_value
