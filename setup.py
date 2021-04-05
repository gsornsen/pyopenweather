from setuptools import find_packages, setup
from pyopenweather import __version__

with open("README.md", "r") as f:
    readme = f.read()

setup(
    name="pyopenweather",
    version=__version__,
    license="MIT",
    author="Gerald Sornsen",
    author_email="gerald@sornsen.io",
    description="Python wrapper for OpenWeather API",
    long_description=readme,
    long_description_content_type="text/markdown",
    url="https://github.com/gsornsen/pyopenweather",
    packages=find_packages(),
    # package_dir={"": "pyopenweather"},
    install_requires=[
        "requests-async>=0.6.2"
    ],
    python_requires=">=3.7",
    classifiers=[
      "License :: OSI Approved :: MIT License",
      "Programming Language :: Python",
      "Programming Language :: Python :: 3.7",
      "Programming Language :: Python :: 3.8",
      "Programming Language :: Python :: 3.9",
      "Natural Language :: English",
      "Operating System :: OS Independent",
      "Development Status :: 5 - Production/Stable",
      "Intended Audience :: Developers",
      "Topic :: Software Development :: Libraries"],
    keywords="openweathermap libary web api wrapper client wind temperature humidity",
    include_package_data=True,
    platforms="Posix; MacOS X; Windows"
)
