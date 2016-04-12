import simplejson, urllib

GEOCODE_BASE_URL = 'https://maps.googleapis.com/maps/api/distancematrix/json?units=imperial&origins=39.361074%2C22.945674&destinations=39.3637331%2C22.958886&key=AIzaSyCGgniz20Kwu0majbIase5rk-Q-QH92cuk'

def geocode(adress):

    url = adress
    result = simplejson.load(urllib.urlopen(url))
    dist = result['rows'][0]['elements'][0]['distance']
    print "text is : " + dist['text']
    print "value is : " + str(dist['value'])

if __name__ == '__main__':
    geocode(GEOCODE_BASE_URL)

    # dist = result['rows'][0]['elements']
    
    # for curr in dist:
    #     curr['distance']['text']
