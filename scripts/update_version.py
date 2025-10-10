# Copyright 2025 The casbin Authors. All Rights Reserved.
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

import sys  
import re  
import os  
import argparse
  
def update_version():  
    """Update version in all relevant files"""  
    parser = argparse.ArgumentParser()
    parser.add_argument('--next-version', help='next release version(x.x.x)')
    args = parser.parse_args()
      
    new_version = args.next_version
    try:
        from importlib.metadata import version

        pycasbin_version = version("pycasbin")
    except ImportError:
        try:
            from importlib_metadata import version

            pycasbin_version = version("pycasbin")
        except (ImportError, Exception):
            pycasbin_version = "unknown"
    # Create __version__.py  
    version_py_path = "casbin_cli/__version__.py"  
    with open(version_py_path, 'w') as f:  
        f.write(f'__version__ = "{new_version}"\n')  
        f.write(f'__pycasbin_version__ = "{pycasbin_version}"\n')
      
    print(f"Updated version to {new_version}")  
  
if __name__ == "__main__": 
    update_version()