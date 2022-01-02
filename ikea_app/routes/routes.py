from ikea_app import api

from ikea_app.controllers.file_controller import FilesFromDirectory, FrequentWords, LongestWords

api.add_resource(FilesFromDirectory, "/api/v1/<pattern>")
api.add_resource(FrequentWords, "/api/v1/frequent_words")
api.add_resource(LongestWords, "/api/v1/longest_words")