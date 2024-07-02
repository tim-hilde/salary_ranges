from setuptools import find_packages
from setuptools import setup

with open("requirements.txt") as f:
    content = f.readlines()
requirements = [x.strip() for x in content if "git+" not in x]

setup(name="salary_ranges",
      version="0.0.2",
      description="Predicting salary ranges of data science jobs based on their job posting.",
      license="MIT",
      author="Tim Hildebrandt",
      author_email="tim.hildebrandt@me.com",
      url="github.com/tim-hilde/salary_ranges",
      install_requires=requirements,
      packages=find_packages(),
    #   test_suite="tests",
      # include_package_data: to install data from MANIFEST.in
      include_package_data=True,
      zip_safe=False)
