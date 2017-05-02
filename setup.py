from distutils.core import setup
from setuptools import find_packages

pkgs = find_packages()

setup(name='arcpy',
      version='1.3',
      description='ArcPy - ArcGIS Pro Python API',
      author='Clinton Dow',
      author_email='cdow@esri.com',
      url='http://www.arcgis.com',
      packages=pkgs,
      include_package_data=True,
      license='ESRI')
