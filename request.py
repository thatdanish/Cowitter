import requests

url = 'http://127.0.0.1:5000/predict'
r = requests.post(url,json={'text':"Corona cases increases exponentially in india"}).json()

if r['success']:
    out_list = r['Prediction']
    #print(out_list)
    if out_list[0] == "1":
        print("The News is about Covid-19 and it's sentiment is")

        if out_list[1] == '1':
            print("Positive!! YEAH! :D")

        else:
            print("Sorry but it's Negative :(" )

    else:
        print("News is isn't about Covid-19, Try-Checking for another news")

else:
    print('POST request failed!! :(. Check Server and try again.')
