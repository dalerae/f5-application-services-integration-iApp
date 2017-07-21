#!/usr/bin/env python

import pytest

from src.appservices.BIPClient import BIPClient
from src.appservices.TestTools import get_test_config
from src.appservices.TestTools import prepare_payloads_functional_test
from src.appservices.tools import setup_logging as _setup_logging


def pytest_addoption(parser):
    parser.addoption("--host", action='store',
                     help="IP address of the BigIP")
    parser.addoption("--policy_host", action='store',
                     help="IP address of the policy host")
    parser.addoption("--scale_size", action='store',
                     help="Size of scale test",
                     default=20, type=int)


@pytest.fixture(scope='module')
def host(request):
    return request.config.getoption("--host")


@pytest.fixture(scope='module')
def policy_host(request):
    return request.config.getoption("--policy_host")


@pytest.fixture(scope='module')
def scale_size(request):
    return request.config.getoption("--scale_size")


@pytest.fixture(scope='module')
def get_config(host, policy_host):
    return get_test_config(host, policy_host)


@pytest.fixture(scope='module')
def prepare_tests(bip_client, get_config):

    prepare_payloads_functional_test(bip_client, get_config)


@pytest.fixture(scope='module')
def bip_client(host):
    return BIPClient(host)


@pytest.fixture(scope='module')
def setup_logging():
    _setup_logging()
