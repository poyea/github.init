<img align="left" width="150" height="150" src="https://user-images.githubusercontent.com/24757020/150645295-bc73557c-4aa3-4546-8f3b-47b94d24efe5.png" alt="github.(init|new)?!">

# github.init

Generate a new GitHub repository in 3 seconds (literally). There are a lot of customizations to do for a new repository, and this tool just solves the first problem for you.

## Supported licenses
* empty license
* Apache 2.0
* MIT
* GPLv2
* GPLv3
* BSD2
* BSD3
* CC0
* Unlicense

## To generate

The script and the templates themselves are self-deleting, but I assure you that this is very safe.

```console
$ git clone https://github.com/poyea/github.init.git
$ cd github.init
$ python --version
Python 3.9.0
$ ./kickstart.py -h
usage: kickstart.py [-h] --name name --author author --license name --readme type [-q quiet]

Kickstart your GitHub project!

optional arguments:
  -h, --help            show this help message and exit
  --name name, -n name  your project name
  --author author, -a author
                        your name
  --license name, -l name
                        license to be used
  --readme type, -r type
                        type of README.md to be used
  -q quiet              suppress warning
$ ./kickstart.py --license "Apache 2.0" -r "left" -n "your cool project" -a "your name" -r "left"
$ cd ..
$ mv -T github.init your_cool_project
```

and it's ready to gooooo!

## If you like this, please
* Star
* Fork
* Contribute

## License
This repository is licensed under MIT. See also [LICENSE](LICENSE) for details.
