step 1 "pip install -r req.txt"

step 2 "run api.py" don't forgot to change url ADDED'#change with your profile url
headers = { 'Content-Type': 'application/json', 
           'cookie': '' #take cookie from network api payload headers
,'csrf-token': 'ajax:0313898894319977257'#take csrf from network api payload headers 
           }

step 3 'run main.py'