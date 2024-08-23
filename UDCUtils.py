#This file will be used to read the environment variables to get secret keys of different tech platforms 
# like Deep Learning, Open AI, Unstructured and Pinecone. It will also have definition of commonly used operations.
import os
import sys
from dotenv import load_dotenv, find_dotenv
import panel as pn
pn.extension()

class UDCUtils:
    def __init__(self):
        _ = load_dotenv(find_dotenv())

    def get_openai_api_key(self):
        return (os.getenv('OPENAI_API_KEY'))
        
    def get_dlapi_key(self):
        return (os.getenv('DLAI_API_KEY'))
        
    def get_dlapi_url(self):
        return (os.getenv('DLAI_API_URL'))
        
    def get_unstructured_api_key(self):
        return (os.getenv('UNSTRUCTURED_API_KEY'))
        
    def get_unstructured_api_url(self):
        return (os.getenv('UNSTRUCTURED_API_URL'))
        
    def get_pinecone_api_key(self):
        return (os.getenv('PINECONE_API_KEY'))
        
    def create_dlai_index_name(self, index_name):
        dlai_api_key = os.getenv("DLAI_API_KEY")
        index_name = f'{index_name}-{dlai_api_key[-36:].lower().replace("_", "-")}'
        return index_name[:-3]
        
    def is_colab(self):
        return 'google.colab' in sys.modules

class upld_file():
    def __init__(self):
        self.widget_file_upload = pn.widgets.FileInput(accept='.pdf,.png,.html,.ppt', multiple=False)
        self.widget_file_upload.param.watch(self.save_filename,'filename')

    def save_filename(self, _):
        if(len(self.widget_file_upload.value) > 2e6):
            print("File is too large. Maximum size allowed is 2MB")
        else:
            print("inside else...")
            self.widget_file_upload.save('example_files/' + self.widget_file_upload.filename)
            #self.widget_file_upload.save('./example_files/' + self.widget_file_upload.filename)