#!/usr/bin/env python3
import argparse
from datetime import datetime
import json
from os import remove, rmdir
import re
from sys import argv
import time

def sub(tag_id, entry, body):
    tag_string = f"{{- {tag_id} -}}"
    return re.sub(tag_string, entry, body)

def modify_readme_content(content, args):
    content = sub("name", args.name, content)
    content = sub("license", args.license, content)
    if args.readme.startswith("cent"):
        content = sub("image_alignment", "center", content)
        content = re.sub(
            r"{- header:center:start -}\n?([\s\S]*?)\n?{- header:center:end -}",
            r"\1",
            content,
            re.DOTALL | re.MULTILINE,
        )
    else:
        content = sub("image_alignment", args.readme, content)
        content = re.sub(
            r"{- header:left_or_right:start -}\n?([\s\S]*?)\n?{- header:left_or_right:end -}",
            r"\1",
            content,
            re.DOTALL | re.MULTILINE,
        )
    content = re.sub(
        r"{- header[\s\S]*? -}[\s\S]*?{- header[\s\S]*? -}",
        "",
        content,
        re.DOTALL | re.MULTILINE,
    )
    return content.lstrip("\n")


def modify_license_content(content, args):
    content = sub("author", args.author, content)
    content = sub("year", str(datetime.now().year), content)
    content = sub("program", args.name, content)
    if args.license == "MIT":
        content = re.sub(
            r"{- license:MIT:start -}\n?([\s\S]*?)\n?{- license:MIT:end -}",
            r"\1",
            content,
            re.DOTALL | re.MULTILINE,
        )
    elif args.license == "Apache 2.0":
        content = re.sub(
            r"{- license:apache2:start -}\n?([\s\S]*?)\n?{- license:apache2:end -}",
            r"\1",
            content,
            re.DOTALL | re.MULTILINE,
        )
    elif args.license == "GPLv3":
        content = re.sub(
            r"{- license:GPLv3:start -}\n?([\s\S]*?)\n?{- license:GPLv3:end -}",
            r"\1",
            content,
            re.DOTALL | re.MULTILINE,
        )
    elif args.license == "GPLv2":
        content = re.sub(
            r"{- license:GPLv2:start -}\n?([\s\S]*?)\n?{- license:GPLv2:end -}",
            r"\1",
            content,
            re.DOTALL | re.MULTILINE,
        )
    elif args.license == "Empty":
        content = re.sub(
            r"{- license:Empty:start -}\n?([\s\S]*?)\n?{- license:Empty:end -}",
            r"\1",
            content,
            re.DOTALL | re.MULTILINE,
        )
    content = re.sub(
        r"{- license[\s\S]*? -}[\s\S]*?{- license[\s\S]*? -}",
        "",
        content,
        re.DOTALL | re.MULTILINE,
    )
    return content.lstrip("\n")


def print_warning():
    print("WARNING: This script will delete itself after the generation!!!")
    print("3", end=" ", flush=True)
    time.sleep(1)
    print("2", end=" ", flush=True)
    time.sleep(1)
    print("1...")
    time.sleep(1)


def main():
    with open("config.kickstart", "r") as f:
        config = json.load(f)
    licenses, readmes = config["license"], config["readmes"]
    parser = argparse.ArgumentParser(description="Kickstart your GitHub project!")
    parser.add_argument(
        "--name",
        "-n",
        dest="name",
        metavar="name",
        help="your project name",
        required=True,
    )
    parser.add_argument(
        "--author",
        "-a",
        dest="author",
        metavar="author",
        help="your name",
        required=True,
    )
    parser.add_argument(
        "--license",
        "-l",
        dest="license",
        metavar="name",
        help="license to be used",
        required=True,
        choices=licenses,
    )
    parser.add_argument(
        "--readme",
        "-r",
        dest="readme",
        metavar="type",
        help="type of README.md to be used",
        required=True,
        choices=readmes,
    )
    parser.add_argument(
        "-q",
        dest="quiet",
        metavar="quiet",
        help="suppress warning",
    )
    args = parser.parse_args()
    if not args.quiet:
        print_warning()
    with open("./readme.kickstart", "r") as f:
        readme_content = f.read()
    with open("./license.kickstart", "r") as f:
        license_content = f.read()
    readme_content = modify_readme_content(readme_content, args)
    license_content = modify_license_content(license_content, args)
    with open("./README.md", "w") as f:
        f.write(readme_content)
    with open("./LICENSE", "w") as f:
        f.write(license_content)
    # remove templates, and the generator
    remove("./readme.kickstart")
    remove("./license.kickstart")
    remove("./config.kickstart")
    remove("./.github/workflows/release.yml")
    rmdir("./.github/workflows")
    remove(argv[0])


if __name__ == "__main__":
    main()
