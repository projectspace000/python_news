def emailed_results(data):
    for i, document in enumerate(data):
        return data['results']

def parsed_mailed(data):
    mailed = []
    for b in data:
        dic = {}
        dic['sub-title'] = b['abstract']
        dic['byline'] = b['byline']
        dic['column'] = b['column']
        dic['type'] = b['des_facet']
        dic['date'] =b['published_date']
        dic['section'] = b['section']
        dic['title'] = b['title']
        dic['url'] = b['url']
        
        mailed.append(dic)
    return mailed

def title(data):
    for i, title in enumerate(d['title'] for d in data): 
            print i,title
          
def url(data):
    for i, url in enumerate(d['url'] for d in data): 
            print i,url


def most_mailed(days, api):
    import urllib
    import json
    bucket = 'http://api.nytimes.com/svc/mostpopular/v2/mostemailed/all-sections/'
    string = bucket+days+api
    
    response_string = urllib.urlopen(string).read()
    response_dictionary = json.loads(response_string)
    
    results = emailed_results(response_dictionary)
    parsed_results = parsed_mailed(results)
    
    titles = title(parsed_results)
    urls = url(parsed_results)
    return titles, urls
    
    

#past seven days
days='7?'
api='api-key=6166b3347690479eb293da918c613e03'

#call the function
most_mailed(days, api)
