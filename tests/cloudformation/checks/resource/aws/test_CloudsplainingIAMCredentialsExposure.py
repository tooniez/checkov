import os
import unittest

from checkov.cloudformation.checks.resource.aws.IAMCredentialsExposure import check
from checkov.cloudformation.runner import Runner
from checkov.runner_filter import RunnerFilter

class TestCloudsplainingIAMCredentialsExposure(unittest.TestCase):

    def test_summary(self):
        runner = Runner()
        current_dir = os.path.dirname(os.path.realpath(__file__))

        test_files_dir = current_dir + "/Cloudsplaining_IAMCredentialsExposure"
        report = runner.run(root_folder=test_files_dir,runner_filter=RunnerFilter(checks=[check.id]))
        summary = report.get_summary()
        self.assertEqual(report.failed_checks[0].check_id, check.id)
        self.assertEqual(summary['passed'], 1)
        self.assertEqual(summary['failed'], 1)
        self.assertEqual(summary['skipped'], 0)
        self.assertEqual(summary['parsing_errors'], 0)
        self.assertIn('Properties/PolicyDocument/Statement/[0]/Action/[0]/', report.failed_checks[0].check_result.get('evaluated_keys'))
        self.assertIn('Properties/PolicyDocument/Statement/[0]/Action/[2]/', report.failed_checks[0].check_result.get('evaluated_keys'))


if __name__ == '__main__':
    unittest.main()
