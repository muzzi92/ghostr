import argparse
import os
import sys
import unittest


def fixup_paths(path):
    try:
        import google
        google.__path__.append("{0}/google".format(path))
    except ImportError:
        pass

    sys.path.insert(0, path)


def main(sdk_path, test_path, test_pattern):
    if os.path.exists(os.path.join(sdk_path, 'platform/google_appengine')):
        sdk_path = os.path.join(sdk_path, 'platform/google_appengine')

    fixup_paths(sdk_path)

    import dev_appserver
    dev_appserver.fix_sys_path()

    try:
        import appengine_config
        (appengine_config)
    except ImportError:
        print('Note: unable to import appengine_config.')

    suite = unittest.loader.TestLoader().discover(test_path, test_pattern)
    return unittest.TextTestRunner(verbosity=2).run(suite)


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description=__doc__,
        formatter_class=argparse.RawDescriptionHelpFormatter)
    parser.add_argument(
        'sdk_path',
        help='The path to the Google App Engine SDK or the Google Cloud SDK.')
    parser.add_argument(
        '--test-path',
        help='The path to look for tests, defaults to the current directory.',
        default="{}/tests".format(os.getcwd()))
    parser.add_argument(
        '--test-pattern',
        help='The file pattern for test modules, defaults to *_test.py.',
        default='*_test.py')

    args = parser.parse_args()

    result = main(args.sdk_path, args.test_path, args.test_pattern)

    if not result.wasSuccessful():
        sys.exit(1)
