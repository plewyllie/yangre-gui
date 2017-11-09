import os
os.environ['LD_LIBRARY_PATH'] = "/home/pilewyll/libyang-prod/build"

YANGGRE_PATH = "/home/pilewyll/libyang-prod/build/yangre"
#W3CGREP_PATH = "/Users/pilewyll/yangre-gui/w3cgrep"
W3CGREP_PATH = "/home/pilewyll/w3cgrep"
PREFIX = "/yangre"  # changing this will break things, as it is also used in ajax calls
APIPREFIX = "/yangre/v1"
