#  ------------------------------------------------------------------------------------------
#  Copyright (c) Microsoft Corporation. All rights reserved.
#  Licensed under the MIT License (MIT). See LICENSE in the repo root for license information.
#  ------------------------------------------------------------------------------------------

"""A setuptools based setup module.

See:
https://packaging.python.org/guides/distributing-packages-using-setuptools/
"""

import os
import pathlib
from setuptools import setup, find_packages  # type: ignore


here = pathlib.Path(__file__).parent.resolve()

# Get the long description from the README file
long_description = (here / 'README.md').read_text(encoding='utf-8')

version = ''

# If running from a GitHub Action then a standard set of environment variables will be
# populated (https://docs.github.com/en/actions/reference/environment-variables#default-environment-variables).
# In particular, GITHUB_REF is the branch or tag ref that triggered the workflow.
# If this was triggered by a tagged commit then GITHUB_REF will be: 'ref/tags/new_tag'.
# Extract this tag and use it as a version string
# See also:
# https://packaging.python.org/guides/publishing-package-distribution-releases-using-github-actions-ci-cd-workflows/
# https://github.com/pypa/gh-action-pypi-publish
GITHUB_REF_TAG_COMMIT = 'refs/tags/'

github_ref = os.getenv('GITHUB_REF')
if github_ref and github_ref.startswith(GITHUB_REF_TAG_COMMIT):
    version = github_ref[len(GITHUB_REF_TAG_COMMIT):]

# Otherwise, if running from a GitHub Action, but not a tagged commit then GITHUB_RUN_NUMBER will be populated.
# Use this as a post release number. For example if GITHUB_RUN_NUMBER = 124 then the version string will be
# '0.1.2.post124'. Although this is discouraged, see:
# https://www.python.org/dev/peps/pep-0440/#post-releases
# it is necessary here to avoid duplicate packages in Test.PyPI. 
if not version:
    build_number = os.getenv('GITHUB_RUN_NUMBER', "1")
    version = '0.1.2.post' + build_number

setup(
    name='InnerEye-DICOM-RT',
    version=version,
    description='InnerEye DICOM to Nifti conversion functions',
    long_description=long_description,
    long_description_content_type='text/markdown',
    url='https://github.com/microsoft/InnerEye-DICOM-RT',
    author="Microsoft Research Cambridge InnerEye Team ",
    author_email="innereyedev@microsoft.com",
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Science/Research',
        "Topic :: Scientific/Engineering :: Medical Science Apps.",
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3.7'
    ],
    keywords='InnerEye, DICOM-RT, Nifti',
    license='MIT License',
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    include_package_data=True,
    install_requires=[
        'dotnetcore2'
    ],
)
