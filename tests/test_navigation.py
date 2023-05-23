"""
Unittests for navigation/
"""

from unittest import TestCase
from .mock_csv_manager import CSVMock


class StarttimeNowTest(TestCase):
    """Test for starttimenow"""

    def setUp(self) -> None:
        self.success_mock = CSVMock()
        self.error_mock = CSVMock(-1, -1, -1)
        return super().setUp()
