from setuptools import setup, find_packages
import re

VERSIONFILE="jdiotclient/_version.py"
verstrline = open(VERSIONFILE, "rt").read()
VSRE = r"^__version__ = ['\"]([^'\"]*)['\"]"
mo = re.search(VSRE, verstrline, re.M)
if mo:
    verstr = mo.group(1)
else:
    raise RuntimeError("Unable to find version string in %s." % (VERSIONFILE,))

setup(
	# Application name:
	name="jdiotclient",

	# Version number (initial):
	version=verstr,

	# Application author details:
	author="Tamas Jos",
	author_email="info@skelsecprojects.com",

	# Packages
	packages=find_packages(),

	# Include additional files into the package
	include_package_data=True,


	# Details
	url="https://github.com/skelsec/jdiotclient",

	zip_safe = False,
	#
	# license="LICENSE.txt",
	description="JDIoT client library",

	# long_description=open("README.txt").read(),
	python_requires='>=3.7',
	install_requires=[
		'websockets',
		'protobuf==3.19.1'
	],
	
	classifiers=[
		"Programming Language :: Python :: 3.7",
		"License :: OSI Approved :: MIT License",
		"Operating System :: OS Independent",
	],
	#entry_points={
	#	'console_scripts': [
	#		'asmbclient = aiosmb.examples.smbclient:main',
	#	],
	#
	#}
)