# -*- coding: utf-8 -*-
#
# Copyright (c) 2021 -- All rights reserved.
# Author: Uday Kumar <udkumar@hotmail.com>
#
# This file is part of the IKEA test assignment.
#
# All file related resources
#
###############################################################################

from flask import Flask, request, json, make_response
from flask_restful import Resource, reqparse
from datetime import datetime
from ikea_app import app
import werkzeug
import os

from ikea_app.services.file_service import FileService

"""
  resource for file
"""

class FilesFromDirectory(Resource):
  #["f1", "f2"]
  def get(self, pattern):
    app.logger.info("IKEA::FilesFromDirectory::get:: pattern {}".format(pattern))
    return FileService().list_files(pattern)

class FrequentWords(Resource):
  def post(self):
    try:
      parser = reqparse.RequestParser()
      parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files', required=True)
      parser.add_argument('freq', type=int)
      parser.add_argument('camelCase', type=int)
      args = parser.parse_args()

      if not args['file']:
        return {'err': 'File missing !!', 'status': 0, 'data': []}, 400
      if not args['freq']:
        args['freq'] = 10

      app.logger.info("IKEA::FrequentWords::post:: {}".format(args))
      return FileService().frequent_words(args['file'], args['freq'], args['camelCase'])
    except Exception as e:
      app.logger.error("IKEA:FrequentWords:: error {}".format(str(e)))
      return {'err': str(e), 'status': 0, 'data': {}}, 500


class LongestWords(Resource):
  def post(self):
    parser = reqparse.RequestParser()
    parser.add_argument('file', type=werkzeug.datastructures.FileStorage, location='files', required=True)
    args = parser.parse_args()

    app.logger.info("IKEA::LongestWords::post:: {}".format(args))
    return FileService().longest_words(args['file'])