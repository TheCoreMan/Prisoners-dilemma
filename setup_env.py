import os
import argparse
import shutil


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("-u", "--upgrade", action="store_true", help="If the env exists, replace existing env.")
    parser.add_argument("-a", "--activate", action="store_true", help="If the env exists, activate it.")
    return parser.parse_args()


def create_virtual_env():
    os.system("virtualenv env")


def activate_virtual_env():
    from subprocess import Popen
    p = Popen(r"cmd /k title virutalenv activated! && env\Scripts\activate.bat && pip install -r requirements.txt")


def main():
    args = get_args()
    if os.path.exists(os.path.join(os.path.curdir, "env")):
        if args.activate:
            activate_virtual_env()
        elif args.upgrade:
            shutil.rmtree("env")
            create_virtual_env()
            activate_virtual_env()
        else:
            raise Exception("Error! 'env' directory already exists! run with -h for usage.")
    else:
        create_virtual_env()
        activate_virtual_env()
    print("Done!")


if __name__ == "__main__":
    main()
