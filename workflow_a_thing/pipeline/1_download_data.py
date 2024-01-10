from requests import get
import os
import tarfile
import argparse
""" 
$ wget http://vis-www.cs.umass.edu/lfw/lfw-funneled.tgz
$ tar -zxvf lfw-funneled.tgz
 """

def download_faces(url, file_name):
    if os.path.exists(file_name):
        print("File already exists!")
        return

    with open(file_name, "wb") as file:
        response = get(url)
        file.write(response.content)
    
    print("Download complete!")


def extract_faces(file_name):
    if os.path.exists("lfw_funneled"):
        print("File already exists!")
        return

    with tarfile.open(file_name) as tar:
        tar.extractall()


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download and extract faces")
    parser.add_argument("--url", type=str, default="http://vis-www.cs.umass.edu/lfw/lfw-funneled.tgz")
    parser.add_argument("--file_name", type=str, default="lfw-funneled.tgz")
    args = parser.parse_args()
    download_faces(args.url, args.file_name)
    extract_faces(args.file_name)