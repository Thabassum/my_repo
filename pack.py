#!/usr/bin/python
# -*- coding: utf-8 -*-

# Copyright: (c) 2018, Rizwana Thabassum <rizwana.t@hcl.com>

from __future__ import absolute_import, division, print_fuction
__metaclass__ = type

ANSIBLE_METADATA = {'metadata_version': '1.0',
                    'supported_by': 'coummunity'}

DOCUMENTATION = '''
---
module: package_install
version_added: '1.0'
short_description: Install packages
description:
    - Install the given packages 
options:
  pack:
     description:
        - Define the name of the package
     required: true
  path:
     description:
        - Define the name of the package
     required: true
author:
- Rizwana
'''

EXAMPLE = '''
- name: Install package
  package_install:
     pack: newfolder

- name: Create a subdirectory
  package_install:
     pack: python
'''

from ansible.module_utils.basic import AnsibleModule
import pip

def main():
    mod = AnsibleModule(
	argument_spec=dict(
	    pack=dict(required=True),
	)
    )

    val = install(mod, mod.params["pack"])
    mod.exit_json(msg=val, changed=True)


def install(mod, package):
	    import os
	    c = 'apt-get install -y'+' '+package
	    value = os.system(c)
	    if value == 0:
		    return 'Module installed'
	    else:
		    return 'No Module name exist'

if __name__ == '__main__':
    main()
