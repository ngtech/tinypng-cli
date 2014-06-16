#!/usr/bin/env python
#
# name     : tinypng-cli, cli for tinypng
# author   : Xu Xiaodong <xxdlhy@gmail.com>
# license  : GPL
# created  : 2014 Jun 15
# modified : 2014 Jun 16
#

import requests
import json
import sys


def shrink(image):
    url = 'https://api.tinypng.com/shrink'
    auth = requests.auth.HTTPBasicAuth('api', 'oBu_epefiJ9XJNKF5iiNO5kOZluIWrzg')
    data = open(image, 'rb')

    r = requests.post(url, data=data, auth=auth)

    if r.status_code == 201:
        result = json.loads(r.text)
        input_size = result['input']['size'] / 1024
        output_size = result['output']['size'] / 1024
        output_ratio = result['output']['ratio']
        output_url = result['output']['url']
        print('input size: %s kb\noutput size: %s kb\noutput ratio: %s\noutput url: %s' % (input_size, output_size, output_ratio, output_url))

        save(output_url, 'output.png')
    else:
        print('Compression failed :(')


def save(url, image):
    data = open(image, 'wb')
    r = requests.get(url)

    if r.status_code == 200:
        data.write(r.content)
    else:
        print('Save image failed :(')


if __name__ == '__main__':
    for image in sys.argv[1:]:
        shrink(image)
