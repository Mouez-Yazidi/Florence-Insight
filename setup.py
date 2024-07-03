from setuptools import setup
import os
from setuptools.command.install import install  # Import the install class

class CustomInstallCommand(install):
    """Customized setuptools install command - installs flash-attn with --no-build-isolation."""
    def run(self):
        install.run(self)
        os.system('pip install flash-attn --no-build-isolation')

setup(
    name='your_package',
    version='0.1',
    install_requires=[],
    cmdclass={
        'install': CustomInstallCommand,
    },
)
