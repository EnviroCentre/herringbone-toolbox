# -*- coding: utf-8 -*-

# Copyright 2015 EnviroCentre
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#    http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


from distutils.core import setup

setup(
    name='herringbone-toolbox',
    version='0.1.0',
    packages=['herringbone-toolbox'],
    package_dir={'herringbone-toolbox': 'herringbone-toolbox'},
    package_data={'herringbone-toolbox': ['esri/toolboxes/*.*']},
    license='Apache v2.0',
    author='Florenz A. P. Hollebrandse',
    author_email='fhollebrandse@envirocentre.co.uk',
    description='ArcGIS toolbox to create a herringbone pattern'
)
