"""
    Intergration tests for the BlobModule.py file
"""

import pytest
from BlobModule import BlobModule
from dotenv import dotenv_values
import os, uuid
from azure.storage.blob import BlobServiceClient, __version__

def test_upload_blob():
    # Connection string
    config = dotenv_values(".env")
    connectionstring = config["CONNECTIONSTRING"]
    
    # make file
    local_path = "./project/data"
    local_file_name = str(uuid.uuid4()) + ".txt"
    upload_file_path = os.path.join(local_path, local_file_name)
    download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt'))
        
    # write to file
    file = open(upload_file_path, 'w')
    file.write("Hello, World!")
    file.close()  

    
    # create container
    blob_service_client = BlobServiceClient.from_connection_string(connectionstring)
    container_name = str(uuid.uuid4())
    container_client = blob_service_client.create_container(container_name)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
    
    result = BlobModule.upload_blob(local_file_name, upload_file_path, blob_client)
    assert result == True
    BlobModule.delete_blob(container_client, upload_file_path, download_file_path, local_path)
    
def test_list_blobs():
    # Connection string
    config = dotenv_values(".env")
    connectionstring = config["CONNECTIONSTRING"]
    # make file
    local_path = "./project/data"
    local_file_name = str(uuid.uuid4()) + ".txt"
    upload_file_path = os.path.join(local_path, local_file_name)
    download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt'))
        
    # write to file
    file = open(upload_file_path, 'w')
    file.write("Hello, World!")
    file.close()  

    
    # create container
    blob_service_client = BlobServiceClient.from_connection_string(connectionstring)
    container_name = str(uuid.uuid4())
    container_client = blob_service_client.create_container(container_name)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
    
    BlobModule.upload_blob(local_file_name, upload_file_path, blob_client)
    result = BlobModule.list_blobs(container_client)
    assert result == True
    BlobModule.delete_blob(container_client, upload_file_path, download_file_path, local_path)
    
    
def test_download_blob():
    # Connection string
    config = dotenv_values(".env")
    connectionstring = config["CONNECTIONSTRING"]
    # make file
    local_path = "./project/data"
    local_file_name = str(uuid.uuid4()) + ".txt"
    upload_file_path = os.path.join(local_path, local_file_name)
    download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt'))
        
    # write to file
    file = open(upload_file_path, 'w')
    file.write("Hello, World!")
    file.close()  

    
    # create container
    blob_service_client = BlobServiceClient.from_connection_string(connectionstring)
    container_name = str(uuid.uuid4())
    container_client = blob_service_client.create_container(container_name)
    blob_client = blob_service_client.get_blob_client(container=container_name, blob=local_file_name)
    
    BlobModule.upload_blob(local_file_name, upload_file_path, blob_client)
    result = BlobModule.download_blob(local_path, local_file_name, container_client)
    assert result == True
    BlobModule.delete_blob(container_client, upload_file_path, download_file_path, local_path)