#-----
# Description   : Setup for mvps studio
# Author        : Berkan Lafci
# E-mail        : lafciberkan@gmail.com
#-----

from setuptools import setup, find_packages

packages = find_packages(exclude=('mvps.tests*', 'mvps.*.tests*'))

setup(
	name="mvpsstudio",
	version="1.0.0",
	description = "Multiview photometric stereo (MVPS) studio hardware and software",
	author = "Berkan Lafci",
	author_email = "lafciberkan@gmail.com",
	url = "https://github.com/berkanlafci/mvpsstudio",
	keywords = ["multiview photometric stereo", "3D reconstruction", "scanner"],
	classifiers = [],
	install_requires = [],
	provides = ["mvps"],
	packages = packages,
	include_package_data=True,
	extras_require = {},
	entry_points = {},
	)