#!/usr/bin/env python

import os

Nodes = {'eaaa00ed-c1a0-44d3-abe9-e9fbcff86f03':'HGST-S3-DC01-R01-SE01',
         '33a9bf11-c154-42f7-a411-f5d20c073818':'HGST-S3-DC01-R01-SE02',
         '193682bb-ebf5-4919-8013-85545a89fc6b':'HGST-S3-DC01-R01-SE03',
         'ce34bd95-311c-49c9-a3e7-fb3cdd9a4ad8':'HGST-S3-DC01-R01-SE04',
         'f680b2e6-e9d5-45d5-ab1f-6bb2479d8af4':'HGST-S3-DC01-R01-SE05',
         'd1823390-fd6f-498a-b316-ee3f39f3bfa5':'HGST-S3-DC01-R01-SE06',
         '125b2c65-7dc2-489b-9211-f4d02152aa1a':'HGST-S3-DC02-R01-SE01',
         '0236b8d7-8ba6-48d0-b1f4-842e711bd107':'HGST-S3-DC02-R01-SE02',
         'f8979516-ee09-4580-8d1a-b8490d8c5111':'HGST-S3-DC02-R01-SE03',
         'fcd86cac-9a62-4c38-b866-50f850d4495d':'HGST-S3-DC02-R01-SE04',
         'fc2d1d7b-ca11-4f7b-90ee-79f2460ffd40':'HGST-S3-DC02-R01-SE05',
         '66f88851-5133-47d8-8562-a234155569ff':'HGST-S3-DC02-R01-SE06',
         '81bf1c57-6641-4d3a-beb9-d4b1d4e2b0a6':'HGST-S3-DC03-R01-SE01',
         'bfbf13b6-f4fa-4a75-99dd-0dd1c718a160':'HGST-S3-DC03-R01-SE02',
         '825d93c7-c242-415a-a52a-165fbbd03238':'HGST-S3-DC03-R01-SE03',
         '8547b34a-c833-4154-b266-961fa127b564':'HGST-S3-DC03-R01-SE04',
         'f15f019a-6a21-4544-8db2-36ca1f63a680':'HGST-S3-DC03-R01-SE05',
         '522276cc-cc23-41da-9af3-0cee2edc940b':'HGST-S3-DC03-R01-SE06',
         '4e5a6494-d373-4c03-b158-7f7ee0bb32dc':'HGST-S3-DC01-R01-SG01',
         '5b9e37d1-16a1-4807-be45-ceb456983e29':'HGST-S3-DC02-R01-SG01',
         '1e0d08a6-8355-42e0-9838-0ce74e6005c7':'HGST-S3-DC03-R01-SG01'}

dirNames = ['e752e5bd-16a1-4c60-91a2-c7331f80b656_f8979516-ee09-4580-8d1a-b8490d8c5111',
            'e752e5bd-16a1-4c60-91a2-c7331f80b656_f15f019a-6a21-4544-8db2-36ca1f63a680',
            'e752e5bd-16a1-4c60-91a2-c7331f80b656_522276cc-cc23-41da-9af3-0cee2edc940b',
            'e752e5bd-16a1-4c60-91a2-c7331f80b656_ce34bd95-311c-49c9-a3e7-fb3cdd9a4ad8',
            '46694943-6f2b-405b-a26c-22d4b8dfea70_4e5a6494-d373-4c03-b158-7f7ee0bb32dc',
            'e752e5bd-16a1-4c60-91a2-c7331f80b656_33a9bf11-c154-42f7-a411-f5d20c073818',
            'e752e5bd-16a1-4c60-91a2-c7331f80b656_66f88851-5133-47d8-8562-a234155569ff',
            'e752e5bd-16a1-4c60-91a2-c7331f80b656_193682bb-ebf5-4919-8013-85545a89fc6b',
            'e752e5bd-16a1-4c60-91a2-c7331f80b656_f680b2e6-e9d5-45d5-ab1f-6bb2479d8af4',
            'e752e5bd-16a1-4c60-91a2-c7331f80b656_fc2d1d7b-ca11-4f7b-90ee-79f2460ffd40',
            'e752e5bd-16a1-4c60-91a2-c7331f80b656_bfbf13b6-f4fa-4a75-99dd-0dd1c718a160',
            'e752e5bd-16a1-4c60-91a2-c7331f80b656_825d93c7-c242-415a-a52a-165fbbd03238',
            '46694943-6f2b-405b-a26c-22d4b8dfea70_5b9e37d1-16a1-4807-be45-ceb456983e29',
            'e752e5bd-16a1-4c60-91a2-c7331f80b656_fcd86cac-9a62-4c38-b866-50f850d4495d',
            'e752e5bd-16a1-4c60-91a2-c7331f80b656_d1823390-fd6f-498a-b316-ee3f39f3bfa5',
            'e752e5bd-16a1-4c60-91a2-c7331f80b656_eaaa00ed-c1a0-44d3-abe9-e9fbcff86f03',
            'e752e5bd-16a1-4c60-91a2-c7331f80b656_81bf1c57-6641-4d3a-beb9-d4b1d4e2b0a6',
            '46694943-6f2b-405b-a26c-22d4b8dfea70_1e0d08a6-8355-42e0-9838-0ce74e6005c7',
            'e752e5bd-16a1-4c60-91a2-c7331f80b656_125b2c65-7dc2-489b-9211-f4d02152aa1a',
            'e752e5bd-16a1-4c60-91a2-c7331f80b656_0236b8d7-8ba6-48d0-b1f4-842e711bd107',
            'e752e5bd-16a1-4c60-91a2-c7331f80b656_8547b34a-c833-4154-b266-961fa127b564']

for d in dirNames:
    if d.split('_')[1] in Nodes.keys():
      os.symlink(d, Nodes[d.split('_')[1]])
        
