#!/usr/bin/env python
# -*- coding: utf-8

# Copyright 2017-2019 The FIAAS Authors
# 
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
# 
#      http://www.apache.org/licenses/LICENSE-2.0
# 
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.


import os

import vcr


def get_vcr(filepath):
    return vcr.VCR(
        path_transformer=vcr.VCR.ensure_suffix('.yaml'),
        match_on=("method", "scheme", "host", "port", "path", "query", "body"),
        cassette_library_dir=os.path.splitext(filepath)[0]
    )
