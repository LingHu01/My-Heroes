import dropbox
from dropbox.exceptions import AuthError

def main():
    app_key = 'h2wew5v2tc2d01h'
    app_secret = 'hm17fuzxiahzefs'
    refresh_token = '9X-1fL1VcCgAAAAAAAAAASyurmqmObig3D3Dc_PYD6VRioZHYtskhT_UvzVKd7Ok'
    try:
        dbx = dropbox.Dropbox(app_key=app_key, app_secret=app_secret, oauth2_refresh_token=refresh_token)
        return dbx
    except AuthError as e:
        print('Error connecting to Dropbox API:', e)

if __name__ == '__main__':
    dbx1 = main()
    result = dbx1.files_list_folder(path='')
    print(result)



