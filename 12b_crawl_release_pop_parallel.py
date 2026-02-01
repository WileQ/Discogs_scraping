import discogs_client, time, gzip, sys, requests
import pandas as pd
from lxml import etree

#client.get_authorize_url()
#code = "cJCXKxTxSE"
#client.get_access_token('cJCXKxTxSE')

client = discogs_client.Client(
   "",
   consumer_key = "",
   consumer_secret = "",
   token = u"",
   secret = u""
)

already_done = set(pd.read_csv("releases_have_want.tsv", sep = '\t')["release"])

with open("ids_todo", 'r') as fin, open(f"releases_have_want.tsv", 'a') as fout:
   for line in fin:
      release_id = int(line.strip())
      if not release_id in already_done:
		   try:
		      release = client.release(release_id).community
		      fout.write(f"{release_id}\t{release.have}\t{release.want}\n")
		      fout.flush()
		   except ValueError:
		      fout.write(f"{release_id}\t0\t0\n")
		      fout.flush()
		   except discogs_client.exceptions.HTTPError:
		      fout.write(f"{release_id}\t0\t0\n")
		      fout.flush()
		   except requests.exceptions.ConnectionError:
		      time.sleep(10)
		      continue
		   time.sleep(1)
