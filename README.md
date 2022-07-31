# AzureBlobStoragePython
In this example I am using python and `pipenv` to work with Azure Blob Storage. I've used the `azure-storage-blob`, `python-dotenv`, `pytest` and `pytest-dotenv`.

### Module
In the underlying code blocks, I create, list, download an delete blobs in a storage account. 
Blob client
```python
blob_client.upload_blob(open(upload_file_path, "rb"))
```

Container client
```python
blob_list = container_client.list_blobs()
for blob in blob_list:
  print(blob.name)
```

container client
```python
download_file = open(download_file_path, "wb")
download_file.write(container_client.download_blob(local_file_name).readall())
```

```python
container_client.delete_container()

os.remove(upload_file_path)
os.remove(download_file_path)
os.rmdir(local_path)
```
