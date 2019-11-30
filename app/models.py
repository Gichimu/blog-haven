
class Quote:
    '''
    Class that defines the default template for the quote object
    '''

    def __init__(self, id, author, quote):
        self.id = id
        self.author = author
        self.quote = quote


class Comment:
    '''
    Class that defines the default template for the comment object
    '''

    def __init__(self, id, comment, name, email):
        self.id = id
        self.comment = comment
        self.name = name
        self.email = email

    



