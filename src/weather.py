from aerisweather.aerisweather import AerisWeather
from aerisweather.requests.ParameterType import ParameterType
from aerisweather.requests.RequestLocation import RequestLocation
from aerisweather.requests.RequestAction import RequestAction
from aerisweather.requests.RequestFilter import RequestFilter

client_id = "HKouDNEXElsJMcbI5gGXi"
client_secret = "8uRZ6dlswv5nBder0OIdyhBoFexV6yj4y6fhs5NE"
app_id = "localhost"

def get_weather(city,state):

    if city == "zetland":
        city = "waterloo"
    if city == "rosebery":
        city = "waterloo"

    if city == "kingsford":
        city = "kensington"

    location_str = city + ","+state+",au"

    # instantiate our aerisweather object
    aeris = AerisWeather(client_id=client_id, client_secret=client_secret, app_id=app_id)

    # create a RequestLocation object to be used with any endpoint requests
    #loc = RequestLocation(city="perth", state="wa")
    # create a simple observations request with no options
    obs_list = aeris.observations(action=RequestAction.OBSERVATIONS.CLOSEST,
                                  filter_=[RequestFilter.OBSERVATIONS.ALL_STATIONS],
                                  params={ParameterType.OBSERVATIONS.P: location_str,
                                          ParameterType.OBSERVATIONS.FIELDS: "place, ob.tempC,ob.weather"})
    ob = obs_list[0].ob
    tempC = ob.tempC
    weather = ob.weather
    return (weather,tempC)



city = "maroubra"
state = "nsw"

weather,temp = get_weather(city,state)
print("city: " + city + "  state: " + state)
print("Conditions are currently " + weather + " with a temp of " + str(temp) + "°C")