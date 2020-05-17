import requests
import json
import os

class Main:
    def __init__(self):
        print("WIP")


class Vivo:

    def __init__(self, vivotoken):
        self.vivotoken = vivotoken

    def Login(self):
        headers = {
            'Content-Type': 'application/json',
            'X-AUTH': self.vivotoken,
        }

        response = requests.get('https://vivo.sx/api/v1/account', headers=headers)

        return response


    def AccInfo(self):
        headers = {
            'Content-Type': 'application/json',
            'X-AUTH': self.vivotoken,
        }

        response = requests.get('https://vivo.sx/api/v1/account', headers=headers)
        json_data = json.loads(response.text)

        return json_data


    def Upload(self, file):
        try: 
            filesize = str(os.stat(file).st_size)
            #print('Filesize: ' + filesize)
        except: 
            exit()

        headers = {
            'Content-Type': 'application/json',
            'X-AUTH': self.vivotoken,
        }

        response = requests.get('https://vivo.sx/api/v1/upload/' + filesize, headers=headers)
        json_data = json.loads(response.text)
        status = json_data['status']
        upload_url = json_data['upload_url']
        #print(status)
        if status == True:
            #print(upload_url)

            files = {
                'file': open(file, 'rb'),
            }
            
            data = {
                'action': ('push'),
                'session': (self.vivotoken),
            }

            response_post = requests.post(upload_url, data=data, files=files)
            
            return response_post.text

        else:
            print('Something is wrong')
            exit()

    def FileInfo(self, url):
        headers = {
            'Content-Type': 'application/json',
            'X-AUTH': self.vivotoken,
        }

        s = url.split('https://vivo.sx/')[1]
        api_url = 'https://vivo.sx/api/v1/files/' + s


        response = requests.get(api_url, headers=headers)
        json_data = json.loads(response.text)

        video_url = json_data['result'][s]['video_url']
        embed_url = json_data['result'][s]['embed_url']
        video_id = s

        return json_data, video_url, embed_url, video_id

    def Clone(self, url):
        headers = {
            'Content-Type': 'application/json',
            'X-AUTH': self.vivotoken,
        }

        s = url.split('https://vivo.sx/')[1]
        api_url = 'https://vivo.sx/api/v1/files/' + s

        response = requests.put(api_url, headers=headers)
        json_data = json.loads(response.text)
        return json_data

class Mediafire:
    def __init__(self, mediafiretoken):
        self.mediafiretoken = mediafiretoken

    def Login(self, mediafiretoken):
        print('WIP')
class Anon:
    def __init__(self, anontoken):
        self.anontoken = anontoken
    
    def Upload(self, file):
        files = {
                'file': open(file, 'rb'),
            }

        if self.anontoken == None:
            response = requests.post('https://api.anonfile.com/upload', files=files)
        else:
            response = requests.post('https://api.anonfile.com/upload?token=' + self.anontoken, files=files)
        json_data = json.loads(response.text)
        short_url = json_data['data']['file']['url']['short']
        full_url = json_data['data']['file']['url']['full']
        return json_data, short_url, full_url

    def FileInfo(self, id):
        response = requests.get('https://api.anonfile.com/v2/file/' + id + '/info')
        json_data = json.loads(response.text)
        name = json_data['data']['file']['metadata']['name']
        size_read = json_data['data']['file']['metadata']['size']['readable']
        return json_data, name, size_read

class Vidoza:
    def __init__(self, vidozatoken):
        self.vidozatoken = vidozatoken

    def Upload(self, file):
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + self.vidozatoken,
            'cache-control': 'no-cache',
        }

        response = requests.get('https://api.vidoza.net/v1/upload/http/server', headers=headers)
        json_data = json.loads(response.text)
        upload_url = json_data['data']['upload_url']
        session = json_data['data']['upload_params']['sess_id']
        
        headers_post = {
            'cache-control': 'no-cache',
        }

        files = {
            'is_xhr': (None, 'true'),
            'sess_id': (None, session),
            'file': open(file, 'rb'),
        }

        response = requests.post(upload_url, headers=headers_post, files=files)
        json_data = json.loads(response.text)
        url = 'https://vidoza.net/' + json_data['code']
        return json_data, url

    def AdvancedUpload(self, file, file_title, file_descr, fld_id, cat_id, tags):
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + self.vidozatoken,
            'cache-control': 'no-cache',
        }

        response = requests.get('https://api.vidoza.net/v1/upload/http/server', headers=headers)
        json_data = json.loads(response.text)
        upload_url = json_data['data']['upload_url']
        session = json_data['data']['upload_params']['sess_id']
        
        headers_post = {
            'cache-control': 'no-cache',
        }

        files = {
            'is_xhr': (None, 'true'),
            'sess_id': (None, session),
            'file_title': (None, file_title),
            'file_descr': (None, file_descr),
            'fld_id': (None, fld_id),
            'cat_id': (None, cat_id),
            'tags': (None, tags),
            'file': open(file, 'rb'),
        }

        response = requests.post(upload_url, headers=headers_post, files=files)
        json_data = json.loads(response.text)
        url = 'https://vidoza.net/' + json_data['code']
        return url

    def FileStatus(self, url):
        s = url.split('https://vidoza.net/')[1]
        a = s.split('.html')[0]
        
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + self.vidozatoken,
            'cache-control': 'no-cache',
        }

        params = (
            ('f[]', [a]),
        )

        response = requests.get('https://api.vidoza.net/v1/files/check', headers=headers, params=params)

        json_data = json.loads(response.text)

        status = json_data['data']['status']

        return status

    def FileInfo(self, url):
        s = url.split('https://vidoza.net/')[1]
        a = s.split('.html')[0]
        
        headers = {
            'Accept': 'application/json',
            'Authorization': 'Bearer ' + self.vidozatoken,
            'cache-control': 'no-cache',
        }

        params = (
            ('f[]', [a]),
        )

        response = requests.get('https://api.vidoza.net/v1/files/check', headers=headers, params=params)

        json_data = json.loads(response.text)

        status = json_data['data'][0]['status']
        name = json_data['data'][0]['name']
        title = json_data['data'][0]['title']
        desc = json_data['data'][0]['descr']
        down = json_data['data'][0]['downloads']
        views_paid = json_data['data'][0]['views_paid']
        category = json_data['data'][0]['category']
        size = json_data['data'][0]['size']
        created = json_data['data'][0]['created']
        streamable = json_data['data'][0]['streamable']

        return json_data, status, name, title, desc, down, views_paid, category, size, created, streamable


