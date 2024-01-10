from requests import get
import os
import tarfile
import argparse

""" 
$ wget http://vis-www.cs.umass.edu/lfw/lfw-funneled.tgz
$ tar -zxvf lfw-funneled.tgz
 """
dir_path = os.path.dirname(os.path.realpath(__file__))
os.makedirs(os.path.join(dir_path, "data"), exist_ok=True)

def download_faces(url, filename):
    if os.path.exists(filename):
        print("File already exists!")
        return

    with open(filename, "wb") as file:
        response = get(url)
        file.write(response.content)
    
    print("Download complete!")


def extract_faces(filename):
    if os.path.exists("lfw_funneled"):
        print("File already exists!")
        return

    with tarfile.open(filename) as tar:
        tar.extractall()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download and extract faces")
    parser.add_argument("--url", type=str, default="http://vis-www.cs.umass.edu/lfw/lfw-funneled.tgz")
    parser.add_argument("--filename", type=str, default="lfw-funneled.tgz")
    args = parser.parse_args()


    filename = os.path.join(dir_path, "data", args.filename)
    download_faces(args.url, filename)
    extract_faces(filename)