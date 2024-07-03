from setuptools import setup
import os

class CustomInstallCommand(install):
    """Customized setuptools install command - prints a friendly greeting."""
    def run(self):
        install.run(self)
        os.system('pip install flash-attn --no-build-isolation')

setup(
    name='your_package',
    version='0.1',
    install_requires=[],
    cmdclass={
        'install': CustomInstallCommand,
    }
)
