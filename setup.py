import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="rightsignature",
	install_requires=[
          'requests>=2.21.0',
		  'datetime>=4.3'
      ],
    version="1.2",
    author='Anton Kaiser',
    author_email='kaiser@kaiser.ovh',
    description="RightSignature API written in python",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/kaiseranton/RightSignature",
    packages=['rightsignature'],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
)