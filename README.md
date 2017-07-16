# yangre-gui

The yangre-gui was built for the [IETF 99 Hackathon](https://www.ietf.org/hackathon/99-hackathon.html)

The idea behind yangre-gui is to build a GUI on top of W3C-compliant regex validators like w3cgrep and yangre (one of the tools from  [libyang](https://github.com/CESNET/libyang)) so that one can be sure their regexs will work in YANG models.

For context, this was a major issue that Openconfig had. While there were a number of POSIX/Perl validators like regex101.com, there wasn't a W3C one.

## Getting Started

After cloning the project, configure `config.py` with the appropriate paths for the yangre and w3cgrep executables. I had some issues with yangre not finding the right library files, so I included an explicit path to the library, feel free to remove or customize this as needed.

you can launch it directly using python with
```
python run.py
```

Note that running it like this is not ideal for production, this should be done using something like nginx.

### Prerequisites

* Have w3cgrep and yangre installed on the local machine
* Python 3.5
* Flask
