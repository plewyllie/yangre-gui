# yangre-gui

The yangre-gui was built for the [IETF 99 Hackathon](https://www.ietf.org/hackathon/99-hackathon.html)

The idea behind yangre-gui is to build a GUI on top of W3C-compliant regex validators like w3cgrep and yangre (one of the tools from  [libyang](https://github.com/CESNET/libyang)) so that one can be sure their regexs will work in YANG models.

For context, this was a major issue that Openconfig had. While there were a number of POSIX/Perl validators like regex101.com, there wasn't a W3C one.

## Getting Started

After cloning the project, configure `config.py` with the appropriate paths for the yangre and w3cgrep executables. I had some issues with yangre not finding the right library files, so I included an explicit path to the library. Feel free to remove or customize this as needed.

Once configured, launch the web GUI simply with
```
python run.py
```

Note that this is not ideal for production. For use in a production environment, please use nginx or similar.

### Prerequisites

* Have w3cgrep and yangre installed on the local machine
* Python 3.5
* Flask

## Acknowledgments

Thanks to Joe Clarke, Radek Krejci, all the testers from IETF and especially Benoit Claise for allowing me to participate! :)
