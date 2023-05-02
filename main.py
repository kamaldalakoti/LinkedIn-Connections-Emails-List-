from linkedinScp import LinkedIn 
import pandas as pd

# email = "kamaldalakoti90@gmail.com" #set username
   
# password = "Kamal@1551" #set password

email = "rpanchal3101@gmail.com" #set username
   
password = "e_mc.square" #set password

# target_profile = "https://www.linkedin.com/in/tufayel-ahmed-cse/" #set target profile url
target_profile = f"https://www.linkedin.com/in/"

df = pd.read_csv("linkedinConList.csv")

client = LinkedIn()
if client.login(email, password):
    profile_list = []
    for row in df.values:
        # print(row[-1])
        try:
            url = target_profile + row[-1]
            email, phone = client.singleScan(url)
            print(email[-1])
            profile_list.append({
                    'email':email[-1]})
        # print(phone[-18])
        except Exception as e:
            print(e)
            profile_list.append({
                    'email':None})

    # df = pd.DataFrame(profile_list)
    df['email'] = profile_list
    df.to_csv('linkedinConList_email.csv',index=False)    
else:
    print("Login Failed, please recheck login credentials")

