import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self,file_from,file_to):
        dbx = dropbox.Dropbox(self.access_token)
        f=open(file_from,"rb")
        dbx.files_upload(f.read(), file_to)

def main():
    access_token="dU7RdSluCFsAAAAAAAAAAXse-A6ffTSLKyAvY1-KlIoFlZcHvbHnNlEqu6SXBQ_f"
    transferData=TransferData(access_token)
   
    file_from=input("enter the file path to transfer : ")
    name=input("enter the file path of dropbox : ")
    file_to="/project-101/"+(name)
    transferData.upload_file(file_from,file_to)
    print( "moved")

main()
