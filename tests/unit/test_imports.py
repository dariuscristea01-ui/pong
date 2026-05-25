import unittest


class ImportSmokeTest(unittest.TestCase):
    def test_package_imports(self) -> None:
        import pong  # noqa: F401
        import pong.main  # noqa: F401


if __name__ == "__main__":
    unittest.main()
