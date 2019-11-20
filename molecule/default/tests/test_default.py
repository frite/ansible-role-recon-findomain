import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']
).get_hosts('all')


def test_findomain(host):
    f = host.file('/usr/local/bin/findomain')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0o755'


def test_findomain_tokens_file(host):
    f = host.file('/root/.findomain_tokens')

    assert f.exists
    assert f.user == 'root'
    assert f.group == 'root'
    assert oct(f.mode) == '0o600'
