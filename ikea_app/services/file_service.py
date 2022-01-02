# -*- coding: utf-8 -*-
"""
Created on < Dec-2021 >

Author: Uday Kumar

This file is part of the IKEA assigment.

"""

from datetime import datetime
from ikea_app import app
import os
import re
from collections import Counter
import json

class FileService():

    def frequent_words(self, file, freq, camelCase):
        try:
            res= {'status':0, 'err': '', 'data':[], 'message':''}
            status_code = 200

            txtFile = file.readlines()
            for l, w in enumerate(txtFile):
                words = re.findall(r'\w+', w.decode("utf-8"))
                if words:
                    if camelCase:
                        words = [word for word in words if len(word) > 1]
                        counts = Counter(words)
                        top_freq = counts.most_common(freq)
                        rs = json.dumps(dict(top_freq))
                        rs1 = json.loads(rs)
                        res["data"].append(rs1)
                        res["status"] = 1
                        res["message"] = "{} Most frequent words".format(freq)
                    else:
                        cap_words = [word.lower() for word in words if len(word)>1]
                        counts = Counter(cap_words)
                        top_freq = counts.most_common(freq)
                        rs = json.dumps(dict(top_freq))
                        rs1 = json.loads(rs)
                        res["data"].append(rs1)
                        res["status"] = 1
                        res["message"] = "{} Most frequent words".format(freq)

        except Exception as e:
            app.logger.error('FileService:frequent_words::error:{}'.format(str(e)))
            res['err'] = 'Upload file: something went wrong !'
            status_code = 500

        return res, status_code
    
    def list_files(self, pattern):
        try:
            res= {'status':0, 'err': '', 'data':[], 'message':''}
            status_code = 200
            flag = False

            app.logger.info("FileService:list_files:: pattern: {}".format(str(pattern)))
            if not pattern:
              res['err'] = 'Pattern is missing !!'
              return res, 400
            
            folder = os.getcwd() + '/file_directory'
            dir_list = os.listdir(folder)
            if dir_list:
                data = []
                for f in dir_list:
                    match = re.search(pattern, f)
                    if match:
                        flag = True
                        res["data"].append(f)
                if flag:
                    res["status"] = 1
                    res["message"] = "File listed successfully !"
                else:
                    res['err'] = "File is not found !"
                    status_code = 400

        except Exception as e:
            app.logger.error("FileService:list_files::get:: {}".format(e))
            return {'err': 'Something went wrong', 'status': 0, 'data': {}}, 500
        
        return res, status_code

    def longest_words(self, file):
        res= {'status':0, 'err': '', 'data':[], 'message':''}
        status_code = 200

        txtFile = file.readlines()
        longest = {}
        count = 0

        lines = (line.rstrip() for line in txtFile) # All lines including the blank ones
        lines = (line for line in lines if line)
        for l, w in enumerate(lines):
            words = re.findall(r'\w+', w.decode("utf-8"))
            if words:
                words = [word for word in words if len(word) > 1]
                counts = Counter(words)
                all_freq = {**counts}
                all_freq = all_freq.keys()
                s1 = sorted(all_freq,key = len)
                longest["line "+str(l+1)] = s1[-2:]

        res["data"].append(longest)
        res["status"] = 1
        res["message"] = "Longest two words !!"

        return res, status_code
    
    def _largestWord(self, s):
        # Sort the words in increasing
        # order of their lengths
        s = sorted(s, key = len)

        return s[-2:]