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
import atexit
import os

"""Singleton configuration for k8s client"""

#: API server URL
api_server = "https://kubernetes.default.svc.cluster.local"
#: API token
api_token = ""
#: API certificate
cert = None
#: Should the client verify the servers SSL certificates?
verify_ssl = True
#: Enable debugging
debug = False
#: Default timeout for most operations
timeout = 20
#: Default timeout for streaming operations
stream_timeout = 3600
#: Default size of Watcher cache
watcher_cache_size = 1000


""" Implementation of load from kubeconfig"""

TEMP_CERTS = []

def load(path, context='current-context'):

    import yaml
    from dotmap import DotMap
    import base64
    import tempfile

    if not os.path.isfile(path):
        return

    with open(path, 'r') as f:
        config = DotMap(yaml.safe_load(f))

    ctx_name = config[context]
    ctx = next(c for c in config.contexts if c.name == ctx_name)
    cluster = next(c for c in config.clusters if c.name == ctx.context.cluster).cluster

    global api_server 
    api_server = cluster['server']

    global verify_ssl
    if 'certificate-authority' in cluster:
        verify_ssl = cluster['certificate-authority']
    elif 'certificate-authority-data' in cluster:
        verify_ssl = write_temp_cert(cluster['certificate-authority-data'])

    if ctx.context.user:
        user = next(u for u in config.users if u.name == ctx.context.user).user
        global api_token 
        api_token = user['auth-provider']['config']['access-token']


def write_temp_cert(encoded_data):
    temp_handle, temp_path = tempfile.mkstemp('k8s-cert', text=True)
    with os.fdopen(temp_handle, 'wb') as fout:
            fout.write(base64.b64decode(encoded_data))
            fout.close()

    TEMP_CERTS.append(temp_path)

    return temp_path


def cleanup_temp_certs():
    for cert in TEMP_CERTS:
        os.unlink(cert)

atexit.register(cleanup_temp_certs)