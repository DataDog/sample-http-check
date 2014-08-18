from setuptools import setup

setup(
    name='sample-http-check',
    version='0.0.1',
    author='Alexis Le-Quoc',
    author_email='alq@datadoghq.com',
    scripts=['sample.py'],
    description='Quick http check with Datadog',
    install_requires=[
        'pycurl',
    ],
)
