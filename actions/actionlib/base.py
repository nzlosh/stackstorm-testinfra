# coding=utf-8
from st2common import log as logging
from st2common.runners.base_action import Action


LOG = logging.getLogger(__name__)

class TestInfraAction(Action):
    def __init__(self, config, timeout=5):
        super().__init__(config)
        self.config = config

    def run(self, profile_name=None):
        super().run()

        if not profile_name:
            profile_name = self.config.get("default_profile")
            if not profile_name:
                raise ValueError(f"No profile in pack configuration or supplied in action.")

        for profile in self.config.get("profiles", {}):
            if profile["name"] == profile_name:
                break
        else:
            raise ValueError(f"Profile '{profile_name}' can't be found in pack configuration.")
