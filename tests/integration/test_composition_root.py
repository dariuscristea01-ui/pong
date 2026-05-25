import unittest

from pong.main import build_application


class CompositionRootTest(unittest.TestCase):
    def test_build_application_returns_service(self) -> None:
        application = build_application()
        self.assertIsNotNone(application)


if __name__ == "__main__":
    unittest.main()
