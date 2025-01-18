import argparse
import requests

def download_file(url, local_filename):

  

    with requests.get(url ,stream=True) as r:
        r.raise_for_status()
        with open (local_filename ,"wb")as f:
            for chunk in r.iter_content(chunk_size=8192):

                f.write(chunk)

    return local_filename            


parser =argparse.ArgumentParser()

#add a command line argument
parser.add_argument("url", help="URL of the file to be downloaded")
parser.add_argument("output", help="Name to save the downloaded file as")


#parse the argument 
args= parser.parse_args()


download_file(args.url, args.output)
