from setuptools import setup

setup(name='rwsp',
	version='1.0.0',
	description='A Python package to interact with ServerPilot API.',
	author="Rehmat",
	author_email="contact@rehmat.works",
	url="https://github.com/rehmatworks/serverpilot-python",
	license="MIT",
	packages=[
		'serverpilot'
	],
	install_requires=[
		'requests'
	]
)
