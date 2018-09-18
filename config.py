import os
os.environ['LD_LIBRARY_PATH'] = "/usr/local/lib64:/home/libyang/build"

YANGGRE_PATH = "/home/libyang/build/yangre"
W3CGREP_PATH = "/home/w3cgrep/w3cgrep"
PREFIX = "/yangre"  # changing this will break things, as it is also used in ajax calls
APIPREFIX = "/yangre/v1"
