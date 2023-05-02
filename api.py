import json
import requests
import pandas as pd
# Define the API endpoint and headers
url = 'https://www.linkedin.com/voyager/api/relationships/dash/connections?decorationId=com.linkedin.voyager.dash.deco.web.mynetwork.ConnectionListWithProfile-16&count=454&q=search&sortType=RECENTLY_ADDED'#change with your profile url
headers = { 'Content-Type': 'application/json', 
           'cookie': 'li_sugr=6ff4b9cc-a031-4b82-9f05-c372ff1a4ee7; bcookie="v=2&a43fef57-11b2-420f-8c21-a613f66050f4"; bscookie="v=1&202302131640073ac2a7c8-d1bf-4a70-8921-e21a2ceabcceAQEgi3PgM5N8CUvQw7zQkW16nheCbd8e"; G_ENABLED_IDPS=google; liap=true; JSESSIONID="ajax:0313898894319977257"; li_theme=light; li_theme_set=app; guid=14aeec12-a06b-4eda-9003-7308398f6a54; _gcl_au=1.1.589849460.1677817337; timezone=Asia/Calcutta; lang=v=2&lang=en-us; li_at=AQEDARal7GMCBmXwAAABhltMdbMAAAGH6rwv7U4AQw4h0UaqDz3vnDrmUtQFjPcPrj6umuZmjk9PEytYuA1arlj9HYz2fQjag2d_0To9YVH2jfWRTCUKeW7AzUq-KJfOPVl-3wvqRgLyLL6EiuKpjemW; AnalyticsSyncHistory=AQKW9HgMqApiBgAAAYfGr8IrQfOC6TOSerwIk0ejROD06wh2j1rriqMHkt-hzDqrL6-uYr4McCO-lva0gzdj4g; lms_ads=AQEY4SugloSxtwAAAYfGr8P6hU0UbqQgRBYzfRifG5IvkatCBg_6zx0VGZ4Fbaof2vdT1oefZh82SwbWJKfAM5T6FbvNoGk; lms_analytics=AQEY4SugloSxtwAAAYfGr8P6hU0UbqQgRBYzfRifG5IvkatCBg_6zx0VGZ4Fbaof2vdT1oefZh82SwbWJKfAM5T6FbvNoGk_; aam_uuid=20012439835529894160150245208851378973; AMCVS_14215E3D5995C57C0A495C55%40AdobeOrg=1; AMCV_14215E3D5995C57C0A495C55%40AdobeOrg=-637568504%7CMCIDTS%7C19476%7CMCMID%7C19486424008408911710205731837181984982%7CMCAAMLH-1683270422%7C12%7CMCAAMB-1683270422%7CRKhpRz8krg2tLO6pguXWp5olkAcUniQYPHaMWWgdJ3xzPWQmdj0y%7CMCOPTOUT-1682672822s%7CNONE%7CMCCIDH%7C-393071235%7CvVersion%7C5.1.1; UserMatchHistory=AQJe1WyG5ySqGAAAAYfGsIBAdTEU3SXjzJ1gqSbkQAKpyD_9rV5ZH3vxAuDxQOtZSBF6NHGaa0MnYo3qSHMTJ3ge5X63-CoaVbCioGLfALO_a4ZSLBXKurugeZ1UceMH16TRhl1ED6SH4HZo29vNRbtOi3rCsl1Vio0tMtzDwQ3tFaqhRKgT8rKpb4-e7HU3gkjkiq6QHOQqxPTKzgE58FDI6Kn7R16dGDAB7n8T23mbMSNluDgOFWnenBH8vu7kTdkoIdhjt6-JLo3fSXeJkdAUL7gF1Uv7p1sG7leC-D-41oIWJF8Rm71Uv79OJAny3cjuoZY6NsXXoiVYFxu515U6zXe3FZ8; lidc="b=OB07:s=O:r=O:a=O:p=O:g=3982:u=906:x=1:i=1682665671:t=1682666898:v=2:sig=AQHlp4hnUuVGrJ6G34RJbJDsY-6y87y7"'
,'csrf-token': 'ajax:0313898894319977257'#take csrf from network api payload headers 
           }


# Make the API request
response = requests.get(url, headers=headers)


# This code will make a list of all of your Connections  

# Check if the request was successful
if response.status_code == 200:
    # Get the data from the response
    data = response.json()
    # data["elements"]
    # Process the data as needed
    print(len(data['elements']))
    with open('dataKamal.json', 'w') as f:
        json.dump(data, f)
    
    profile_list = []
    for profile in data['elements']:
        try:
            connectedMember = profile['connectedMember'].split("fsd_profile:")[1]
            firstName = profile['connectedMemberResolutionResult']['firstName']
            lastName = profile['connectedMemberResolutionResult']['lastName']
            headline = profile['connectedMemberResolutionResult']['headline']
            publicIdentifier = profile['connectedMemberResolutionResult']['publicIdentifier']

            profile_list.append({
                'connectedMember':connectedMember,
                'firstName':firstName,
                'lastName':lastName,
                'headline':headline,
                'publicIdentifier':publicIdentifier
            })
        except Exception as e:
            profile_list.append({
                'connectedMember':None,
                'firstName':None,
                'lastName':None,
                'headline':None,
                'publicIdentifier':None
            })
    df = pd.DataFrame(profile_list)
    df.to_csv('/data/linkedinConList.csv',index=False)
else:
    # If the request was not successful, print the error message
    print('Error: ' + response.text)




