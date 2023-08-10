python

import json


try:
    # importing required module 
    from urllib3.exceptions import InsecureRequestWarning

    # disabling warnings for insecure connection  
    requests.packages.urllib3.disable_warnings(category=InsecureRequestWarning)
    
    url = "https://alu-intranet.hbtn.io/status"
  
    headers={
        'User-Agent': 'Mozilla/5.0'
      }
      
    
  # sending get request and saving the response as response object 
      r =requests.get(url,headers=headers,verify=False) 
  
  
  if 200 <=r.status_code<=299 :
      data =json.loads(r.text)["data"]

      print("Status Code:",str(r.status_code))
      print("-"*40,"\n")
      i=-1
      while True:
          try:
              temp=[]
              title="Project "+ str((i+1))+":\t"+"\n" 

              project={}
              
            
          
            for key, value in sorted(data[list(data)[i]].items()):
                k="\t{:<6}".format(key)+":"+"{}".format(value)+"\n" 
                temp.append(k)
                
            
            text=""
            j=-1 
            length=len([*temp])

            while len(title)>length or sum([(max(map(lambda x:len(x), [j["project"],j['description'],j['deadline']])))]*(sum(range(-int((-7)//8)*8,-1)))+(min(abs(leng//8)-1,(leng%8))))>=(leng):

                leng+=1



            max_width=[None]*leng 


            



            break
        
        
        except Exception as e:
            pass

        finally:
            del data[-1]

