import uuid
from azure.storage.blob import BlobServiceClient

AZURE_BLOB_KEY = "J4SiB0qPWqKwlft7WJ5YhoTVWGlxd5RtL9/c4WheCG7YVx4UNufnYXOt5QI5XqM4cvqI6k3AjuQA+AStl45qfA=="  #偽物だけど
connection_string = "DefaultEndpointsProtocol=https;AccountName=ismktest;AccountKey=" + AZURE_BLOB_KEY + ";EndpointSuffix=core.windows.net"
container_name = "test"
local_file_path = "ismk.jpg"
blob_name = str(uuid.uuid1())+".png" 


blob_service_client = BlobServiceClient.from_connection_string(connection_string)
container_client = blob_service_client.get_container_client(container_name)
blob_client = blob_service_client.get_blob_client(container=container_name, blob=blob_name)
with open(local_file_path, "rb") as data:
    blob_client.upload_blob(data)
