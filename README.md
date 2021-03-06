# yangre-gui

Yangre-gui is the idea of Benoit Claise and was built by myself for the [IETF 99 Hackathon](https://www.ietf.org/hackathon/99-hackathon.html)

It is a GUI on top of W3C-compliant regex validators like w3cgrep and yangre (one of the tools from  [libyang](https://github.com/CESNET/libyang)) so that one can be sure their regexs will work in YANG models.

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

## Docker
The application can also be run using docker. In the docker folder, run
```
docker-compose build
docker-compose up
```
Yangre is now available at http://localhost/yangre

## Resources
* See [RFC 7950 section 9.4.5](https://tools.ietf.org/html/rfc7950#section-9.4.5) for details on the YANG regular expressions.
* See [RFC 7950 section 6.1.3](https://tools.ietf.org/html/rfc7950#section-6.1.3) for information on quoting


## Acknowledgments

Thanks to Joe Clarke, Radek Krejci, all the testers from IETF and especially Benoit Claise for allowing me to participate! :)
