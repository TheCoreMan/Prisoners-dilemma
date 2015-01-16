import os
import argparse
import shutil


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--upgrade", action="store_true", help="Replace existing env.")
    return parser.parse_args()


def create_virtual_env():
    os.system("virtualenv env")
    os.system(r"env\Scripts\activate.bat && pip install -r requirements.txt")


def main():
    args = get_args()
    if os.path.exists(os.path.join(os.path.curdir, "env")):
        if args.upgrade:
            shutil.rmtree("env")
        else:
            raise Exception("Error! 'env' directory already exists! run with -h for usage.")
    create_virtual_env()


if __name__ == "__main__":
    main()
