from lib.base import TestInfraAction


class RunTest(TestInfraAction):
    """
    Run testinfra tests against the host.
    """

    def run(self, host):
        super().run()

        raise NotImplementedError
