from unittest import TestCase
import os
import re
from collections import Counter
import json
# DDD, deployable, upd=grade, multiple deply, Integration test

class TestFileService(TestCase):

    def test_list_files(self):
        res ={"data":[]}
        folder = os.getcwd() + '/file_directory'
        dir_list = os.listdir(folder)
        pattern = r"\.js$"
        for f in dir_list:
            match = re.search(pattern, f)
            if match:
                res["data"].append(f)
        self.assertEqual(res["data"], ["main.js"])
    
    def test_frequent_words(self):
        d1 = {'test': 2, 'work': 2, 'case': 1, 'should': 1, 'or': 1, 'not': 1, 'it': 1, 'is': 1, 'depend': 1, 'upon': 1}
        
        s1 = "test case should work or not work, it is depend upon test cases"
        words = re.findall(r'\w+', s1)
        words = [word for word in words if len(word) > 1]
        counts = Counter(words)
        top_freq = counts.most_common(10)
        rs = json.dumps(dict(top_freq))
        rs1 = json.loads(rs)
        self.assertEqual(rs1, d1)

    def test_longest_words(self):
        s1 = "test case should work or not work, it is depend upon test cases"
        words = re.findall(r'\w+', s1)
        words = [word for word in words if len(word) > 1]

        counts = Counter(words)
        all_freq = {**counts}
        all_freq = all_freq.keys()
        s1 = sorted(all_freq,key = len)
        self.assertEqual(s1[-2:], ['should', 'depend'])