import io
import pandas
import requests
import zipfile

print("Downloading citibike tripdata...")
data = requests.get("https://s3.amazonaws.com/tripdata/201307-201402-citibike-tripdata.zip")

print("Merging data...")
#zf = zipfile.ZipFile("201307-201402-citibike-tripdata.zip")
zf = zipfile.ZipFile(io.BytesIO(data.content))
df = pandas.concat((pandas.read_csv(zf.open(f.filename)) for f in zf.infolist()))

print("Saving CSV...")
df.to_csv("data.csv")
print("Complete!")