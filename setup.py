from setuptools import find_packages, setup
from setuptools.command.test import test as TestCommand


class PyTest(TestCommand):

    def finalize_options(self):
        TestCommand.finalize_options(self)
        self.test_args = []
        self.test_suite = True

    def run_tests(self):
        # import here, cause outside the eggs aren't loaded
        import pytest
        pytest.main(self.test_args)

setup(
    name="gevent-socketio-redux",
    version="0.4.0rc0",
    description=("SocketIO server based on the Gevent pywsgi server, "
                 "a Python network library"),
    author="Jeffrey Gelens",
    author_email="jeffrey@noppo.pro",
    maintainer="Saurabh Kumar",
    maintainer_email="saurabh@saurabh-kumar.com",
    license="BSD",
    url="https://github.com/theskumar/gevent-socketio",
    download_url="https://github.com/theskumar/gevent-socketio",
    install_requires=("gevent-websocket", "gevent", ),
    setup_requires=('versiontools >= 1.7'),
    cmdclass={'test': PyTest},
    tests_require=['pytest', 'mock>=1.0.1', "coverage"],
    packages=find_packages(exclude=["examples", "tests"]),
    classifiers=[
        "Development Status :: 4 - Beta",
        "License :: OSI Approved :: BSD License",
        "Programming Language :: Python",
        "Operating System :: MacOS :: MacOS X",
        "Operating System :: POSIX",
        "Topic :: Internet",
        "Topic :: Software Development :: Libraries :: Python Modules",
        "Intended Audience :: Developers",
    ],
    entry_points="""

    [paste.server_runner]
    paster = socketio.server:serve_paste

    """,
)
