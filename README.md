# yangre-gui

The yangre-gui was built for the [IETF 99 Hackathon](https://www.ietf.org/hackathon/99-hackathon.html)

The idea behind yangre-gui is to build a GUI on top of W3C-compliant regex validators like w3cgrep and yangre (one of the tools from the [libyang](https://github.com/CESNET/libyang)) so that one can be sure their regexs will work in YANG models.

For context, this was a major issue that Openconfig had. While there were a number of POSIX/Perl validators like regex101.com, there wasn't a W3C one.
