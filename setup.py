from setuptools import setup, find_packages
import os

version = '0.1a3'

setup(name='acentoweb.insurance',
      version=version,
      description="A framework for insurance companies to manage their policies.",
      long_description=open("README.txt").read() + "\n" +
                       open(os.path.join("docs", "HISTORY.txt")).read(),
      # Get more strings from
      # http://pypi.python.org/pypi?%3Aaction=list_classifiers
      classifiers=[
        "Framework :: Plone",
        "Programming Language :: Python",
        ],
      keywords='',
      author='',
      author_email='',
      url='http://svn.plone.org/svn/collective/',
      license='GPL',
      packages=find_packages(exclude=['ez_setup']),
      namespace_packages=['acentoweb'],
      include_package_data=True,
      zip_safe=False,
      install_requires=[
          'setuptools',
          # -*- Extra requirements: -*-
          'Plone',
          'plone.app.dexterity',
          'plone.namedfile [blobs]',
          'plone.formwidget.namedfile',
          'collective.wtf',
          'collective.dnifield',
      ],
      extras_require={
          'test': [
              'plone.app.testing',
              ]
          },
      entry_points="""
      # -*- Entry points: -*-

      [z3c.autoinclude.plugin]
      target = plone
      """,
      )
