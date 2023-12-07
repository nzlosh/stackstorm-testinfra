from actionlib.base import TestInfraAction

import pytest

class RunTest(TestInfraAction):
    """
    Run testinfra tests against the host.
    """

    def run(self, hosts, test_path, profile_name):
        super().run()

        retcode = pytest.main()
