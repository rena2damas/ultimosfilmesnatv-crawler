class Movie:

    def __str__(self):
        return \
            '\n' + \
            '### ' + self.id_sapo.encode('utf8') + ' ###\n' + \
            'Title_pt: ' + self.title_pt.encode('utf8') + '\n' + \
            'Description_pt: ' + self.description_sapo.encode('utf8') + '\n' + \
            'Duration: ' + self.duration.encode('utf8') + '\n'

