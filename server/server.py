from bottle import run, route

@route('/routeRobot/<package>/<delivery>', is_xhr=True)
def routeRobot(package, delivery):
    print('Message recieved: ' + package + " -> " + delivery)
    # send request to Davids code
    return


if __name__ == '__main__':
    run(debug=True, reloader=True)