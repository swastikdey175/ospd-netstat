# -*- coding: utf-8 -*-
# Description:
# Setup for the OSP netstat Server
#
# Authors:
# Jan-Oliver Wagner <Jan-Oliver.Wagner@greenbone.net>
#
# Copyright:
# Copyright (C) 2015 Greenbone Networks GmbH
#
# This program is free software; you can redistribute it and/or
# modify it under the terms of the GNU General Public License
# as published by the Free Software Foundation; either version 2
# of the License, or (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software
# Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA.

from setuptools import setup

from ospd_netstat import __version__

setup(
    name='ospd-netstat',
    version=__version__,

    packages=['ospd_netstat'],

    url='http://www.openvas.org',
    author='Greenbone Networks GmbH',
    author_email='info@greenbone.net',

    license='GPLV2+',
    install_requires=['ospd>=1.3.0', 'ospd<2.0', 'paramiko'],

    entry_points={
        'console_scripts': ['ospd-netstat=ospd_netstat.wrapper:main'],
    },
)
