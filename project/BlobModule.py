import os

class BlobModule:
    def upload_blob(local_file_name, upload_file_path, blob_client):
        """
        Take a local file and uplaod it to a container with the blob_client

        Args:
            local_file_name (_type_): name of the created local file
            upload_file_path (_type_): complete path fot he file to upload
            blob_client (_type_): blobclient
            
        Returns:
            boolean: return True if the operation was succeful, otherwise returns false
        """
        print(f"Uploading to Azure Storage as blob: {local_file_name}")
        try:
            with open(upload_file_path, "rb") as data:
                blob_client.upload_blob(data)
            return True
        except Exception as ex:
            print(ex)
            return False
        
    def list_blobs(container_client):
        """
        List the exsisting blobs form the container_client

        Args:
            container_client (_type_): containerclient
        
        Returns:
            boolean: return True if the operation was succeful, otherwise returns false
        """
        print("Listing blobs...")
        try:
            blob_list = container_client.list_blobs()
            for blob in blob_list:
                print(blob.name)
            return True
        except Exception as ex:
            print(ex)
            return False
            
    def download_blob(local_path, local_file_name, container_client):
        """
        download a blob from the storage account
        
        Args:
            local_path (_type_): local path for the download
            local_file_name (_type_): name of the file to fetch
            container_client (_type_): containerclient
        """
        download_file_path = os.path.join(local_path, str.replace(local_file_name ,'.txt', 'DOWNLOAD.txt'))
        print(f"Downloading blob to {download_file_path}")

        try:
            with open(download_file_path, "wb") as download_file:
                download_file.write(container_client.download_blob(local_file_name).readall())
            return True
        except Exception as ex:
            print(ex)
            return False
            
    def delete_blob(container_client, upload_file_path, download_file_path, local_path):
        """
        Clean up the blobs

        Args:
            upload_file_path (_type_): path of the uploaded file
            download_file_path (_type_): path of the downloaded file 
            local_path (_type_): path of the data folder
        """
        try:
            print("Deleting blob container...")
            container_client.delete_container()

            print("Deleting the local source and downloaded files...")
            os.remove(upload_file_path)
            os.remove(download_file_path)
            os.rmdir(local_path)

            print("Done")
            return True
        except Exception as ex:
            print(ex)
            return False