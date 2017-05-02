from distutils.core import setup
from setuptools import find_packages

pkgs = find_packages()

setup(name='dataset-extent-to-features',
      version='0.1',
      description='ArcGIS python (arcpy) tool which creates a feature class'
                  ' representing the collective extent of input data sets.',
      author='Esri Geoprocessing',
      author_email='cdow@esri.com',
      url='http://www.arcgis.com',
      packages=pkgs,
      include_package_data=True,
      license='Apache')
