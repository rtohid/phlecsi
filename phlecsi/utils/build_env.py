#!/usr/bin/python3
# Copyright (c) 2019 R. Tohid
#
# Distributed under the Boost Software License, Version 1.0. (See accompanying
# file LICENSE_1_0.txt or copy at http://www.boost.org/LICENSE_1_0.txt)


import os
import docker
import argparse
import datetime

cwd = os.getcwd()
dockerfile_path = os.path.dirname(
    os.path.realpath(__file__)) + "/../../docker/"

arg_parser = argparse.ArgumentParser(description="Builds FleCSI environments.")

# Set the Linux distro of the Docker image.
distro = arg_parser.add_mutually_exclusive_group()
distro.add_argument(
    "--distro",
    choices=['fedora', 'ubuntu'],
    default='fedora',
    help="builds the docker image based the selected distro. Default: fedora.")

# Set the build/install type.
build_type = arg_parser.add_mutually_exclusive_group()
build_type.add_argument(
    '-b',
    "--build",
    choices=['debug', 'release'],
    default='debug',
    help=
    "builds flecsi and all it's dependencies in 'debug', or 'release' mode. Default: debug"
)
build_type.add_argument(
    '-i',
    "--install",
    default='debug',
    choices=['debug', 'release'],
    help=
    "installs flecsi and all it's dependencies in 'debug', or 'release' mode. Default: debug"
)

args = arg_parser.parse_args()

docker_client = docker.DockerClient(base_url='unix://var/run/docker.sock')
#docker_client = docker.from_env()
image_tag = args.distro + '-' + args.build
image_name = "{image_name}:{tag}".format(image_name='flecsi', tag=image_tag)
img, js = docker_client.images.build(path=dockerfile_path, tag=image_name)
print(img.tags)
