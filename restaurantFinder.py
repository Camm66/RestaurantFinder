from flask import Flask, render_template, request, redirect, url_for
import httplib2
import json
import sys
import codecs
import requests
import threading
sem = threading.Semaphore()

sys.stdout = codecs.getwriter('utf8')(sys.stdout)
sys.stderr = codecs.getwriter('utf8')(sys.stderr)

app = Flask(__name__)

foursquare_client_id = "Get an id from foursquare"
foursquare_client_secret = "Get a secret from foursquare"
google_api_key = "Get an api key from google"


def getGeocodeLocation(inputString):
    locationString = inputString.replace(" ", "+")
    url = ('''https://maps.googleapis.com/maps/api/geocode/json?address=%s&key=%s''' % (locationString, google_api_key))
    h = httplib2.Http()
    response, content = h.request(url, 'GET')
    result = json.loads(content)
    latitude = result['results'][0]['geometry']['location']['lat']
    longitude = result['results'][0]['geometry']['location']['lng']
    return (latitude, longitude)


def findRestaurant(location, food):
    latitude, longitude = getGeocodeLocation(location)
    url = ('https://api.foursquare.com/v2/venues/search?client_id=%s&client_secret=%s&v=20130815&ll=%s,%s&query=%s' % (foursquare_client_id, foursquare_client_secret, latitude, longitude, food))
    h = httplib2.Http()
    result = json.loads(h.request(url, 'GET')[1])
    if result['response']['venues']:
        restaurant = result['response']['venues'][0]
        venue_id = restaurant['id']
        restaurant_name = restaurant['name']
        restaurant_address = restaurant['location']['formattedAddress']
        address = ""
        for i in restaurant_address:
            address += i + " "
        restaurant_address = address
        # 4. Get a 300x300 picture of the restaurant using the venue_id (you can change this by altering the 300x300 value in the URL or replacing it with 'orginal' to get the original picture
        url = ('https://api.foursquare.com/v2/venues/%s/photos?client_id=%s&v=20150603&client_secret=%s' % ((venue_id, foursquare_client_id, foursquare_client_secret)))
        result = json.loads(h.request(url, 'GET')[1])
        # 5. Grab the first image
        if result['response']['photos']['items']:
            firstpic = result['response']['photos']['items'][0]
            prefix = firstpic['prefix']
            suffix = firstpic['suffix']
            imageURL = prefix + "300x300" + suffix
        else:
            # 6. if no image available, insert default image url
            imageURL = "http://pixabay.com/get/8926af5eb597ca51ca4c/1433440765/cheeseburger-34314_1280.png?direct"
            # 7. return a dictionary containing the restaurant name, address, and image url
        restaurantInfo = {'name': restaurant_name, 'address': restaurant_address, 'image': imageURL}
        print "Restaurant Name: %s" % restaurantInfo['name']
        print "Restaurant Address: %s" % restaurantInfo['address']
        print "Image: %s \n" % restaurantInfo['image']
        return restaurantInfo
    else:
        return "No Restaurant found!"


@app.route('/', methods = ['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def showHome():
    if request.method == 'POST':
        if request.form['location']:
            location = request.form['location']
            if request.form['food']:
                food = request.form['food']
                restaurant = findRestaurant(location, food)
                return render_template("results.html", restaurantInfo = restaurant)
    else:
        return render_template("homepage.html")



if __name__ == '__main__':
    app.secret_key = 'secretkey'
    app.debug = True
    app.run(host='0.0.0.0', port=5000)
