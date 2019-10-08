#!/usr/bin/python3
# Copyright (c) 2019 R. Tohid
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)

import os
import json

from yaml import safe_load, dump
from collections import defaultdict


class DockerBuilder:
    """Build a docker images based on the given parameters."""

    def __init__(self, **kwargs):
        self.config(**kwargs)
        print(self.tag)

    def config(self,
               path=None,
               tag=None,
               quiet=False,
               fileobj=None,
               nocache=False,
               rm=False,
               timeout=None,
               custom_context=False,
               encoding=None,
               pull=False,
               forcerm=False,
               dockerfile=None,
               container_limits=None,
               decode=False,
               buildargs=None,
               gzip=False,
               shmsize=None,
               labels=None,
               cache_from=None,
               target=None,
               network_mode=None,
               squash=None,
               extra_hosts=None,
               platform=None,
               isolation=None):

        self.path = path
        self.tag = tag
        self.quiet = quiet
        self.fileobj = fileobj
        self.nocache = nocache
        self.rm = rm
        self.timeout = timeout
        self.custom_context = custom_context
        self.encoding = encoding
        self.pull = pull
        self.forcerm = forcerm
        self.dockerfile = dockerfile
        self.container_limits = container_limits
        self.decode = decode
        self.buildargs = buildargs
        self.gzip = gzip
        self.shmsize = shmsize
        self.labels = labels
        self.cache_from = cache_from
        self.target = target
        self.network_mode = network_mode
        self.squash = squash
        self.extra_hosts = extra_hosts
        self.platform = platform
        self.isolation = isolation


class DockerCompose:
    def __init__(self, file=None):
        """`docker-compose.yml` file parser."""

        with open(file, 'r') as f:
            self.compose_file = safe_load(f)
#            print(compose_file)
#        self.parser(compose_file)

    def parser(self, docker_config):
        self.config = defaultdict(lambda: None)
        for k, v in docker_config.items():
            self.config[k] = v
        with open('out.json', 'w') as json_file:
            json.dump(docker_config, json_file, indent=2)

    def __repr__(self):
        for k, v in self.config.items():
            print(k, ':')
            print(v, '\n')
        return ''


current_dir = os.path.dirname(os.path.abspath(__file__))
file_relative_path = '/../../docker/docker-compose.yml'
a = DockerCompose(current_dir + file_relative_path)
print('a:\n', a.compose_file)
dock = DockerBuilder(**a.compose_file['services']['flecsi']['build'])
