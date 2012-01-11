#!/usr/bin/python
#
# Copyright 2011 Google Inc. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Example script for how to download a CSV file.  

Download a Top Search Queries CSV file and write it to disk.  The email,
password, and website values used here must be replaced with real values.
See wiki document on its use.
"""

# Import the downloader
from downloader import Downloader

# Email address and password used to sign-in to Webmaster Tools
email = 'user@example.com'
password = '********'
# Specify the website and the type of data to download
website = 'http://www.example.com/'
selected_downloads = ['TOP_QUERIES']

# Instantiate the downloader object
downloader = Downloader()
# Authenticate with your Webmaster Tools sign-in info
downloader.LogIn(email, password)
# Initiate the download
downloader.DoDownload(website, selected_downloads)
