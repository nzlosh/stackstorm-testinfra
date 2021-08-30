# coding=utf-8
from st2common import log as logging
from st2common.runners.base_action import Action

LOG = logging.getLogger(__name__)

class TestInfraAction(Action):
    def __init__(self, config, timeout=5):
        super().__init__(config)

    def run(self, profile_name):
        super().run()
        raise NotImplementedError
