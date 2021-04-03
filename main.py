import dropbox

class TransferData:
    def __init__(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dbx = dropbox.Dropbox(self.access_token)

        f = open(file_from, 'rb')
        dbx.files_upload(f.read(), file_to)

def main():
    access_token = 'sl.AuQGlzLviwZYDin8t87e0ZlnM36U1RA-youMM3aGnJtTJoqqtIJGLvgFr-BEzNXNwzTybBegzE3BC1DaVGoDvudxRBhSagNueJHTTdMxe0Jd73WgYGej6qeaSrVktXpFjWs0KAu7pCI'
    transferData = TransferData(access_token)

    file_from = input("ENTER THE FILE NAME-")
    file_to = input("enter the full path to upload the folder to dropbox:")

    transferData.upload_file(file_from, file_to)
    print("FILE HAS BEEN UPLOADED BY mr.bean")

main()