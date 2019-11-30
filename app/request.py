import urllib, json
from .models import Quote

quote_url = 'http://quotes.stormconsultancy.co.uk/random.json'

# def configure_request(app):

     


def get_quote():
    '''
    Method that fetches and returns the quotes from the quote uri

    returns:
        The quote object
    '''
    
    with urllib.request.urlopen(quote_url) as url:
        response_data = url.read()
        response = json.loads(response_data)

        id = response['id']
        author = response['author']
        quote = response['quote']

        quote_object = Quote(id, author, quote)

    return quote_object

