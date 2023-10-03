# (c) 2012, Jeroen Hoekx <jeroen@hoekx.be>
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)

# Make coding more python3-ish
from __future__ import (absolute_import, division, print_function)
__metaclass__ = type

import base64
import glob
import hashlib
import json
import ntpath
import os.path
import re
import shlex
import sys
import time
import uuid
import yaml
import datetime

from collections.abc import Mapping
from functools import partial
from random import Random, SystemRandom, shuffle

from jinja2.filters import pass_environment

from ansible.errors import AnsibleError, AnsibleFilterError, AnsibleFilterTypeError
from ansible.module_utils.six import string_types, integer_types, reraise, text_type
from ansible.module_utils.common.text.converters import to_bytes, to_native, to_text
from ansible.module_utils.common.collections import is_sequence
from ansible.module_utils.common.yaml import yaml_load, yaml_load_all
from ansible.parsing.ajson import AnsibleJSONEncoder
from ansible.parsing.yaml.dumper import AnsibleDumper
from ansible.template import recursive_check_defined
from ansible.utils.display import Display
from ansible.utils.encrypt import do_encrypt, PASSLIB_AVAILABLE
from ansible.utils.hashing import md5s, checksum_s
from ansible.utils.unicode import unicode_wrap
from ansible.utils.vars import merge_hash

display = Display()

UUID_NAMESPACE_ANSIBLE = uuid.UUID('361E6D51-FAEC-444A-9079-341386DA8E2E')




def return_upper(string):
    """Escape all regular expressions special characters from STRING."""
    return string[::-1].upper()



class FilterModule(object):
    ''' Ansible core jinja2 filters '''

    def filters(self):
        return {
            # regex
            'return_upper': return_upper
        }