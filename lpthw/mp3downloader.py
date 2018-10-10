import requests
mp3_url = "http://thevaaram.org/isai/11/11004"
  
# URL of the image to be downloaded is defined as image_url 
#r = requests.get(image_url) # create HTTP response object 
  
# send a HTTP request to the server and save 
# the HTTP response in a response object called r

for i in range (1,102):
    media_url=mp3_url+str(i).zfill(3)+".mp3"
    filename=str(i).zfill(4)+".mp3"
    #print mp3_url
    print (filename)
    print (media_url)
    r = requests.get(media_url) 
    with open(filename,'wb') as f: 
    
        # Saving received content as a png file in 
        # binary format 
    
        # write the contents of the response (r.content) 
        # to a new file in binary mode. 
        f.write(r.content) 
        f.close
