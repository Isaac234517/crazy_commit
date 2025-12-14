import os
import json 
from datetime import datetime
from dotenv import load_dotenv
import git



if __name__ == '__main__':

    if os.path.exists('.env'):
        load_dotenv('.env')
    
    token = os.getenv('TOKEN')

    if not (os.path.exists('./update.json')):
        with open('./update.json', 'w', encoding='utf-8') as f:
            json.dump({'commit':0, 'update_datetime': datetime.now().strftime('%Y-%m-%d %H:%M:%S')}, f,ensure_ascii=False, indent=4)


    with open('./update.json', 'r', encoding='utf-8') as f:
        data  = json.load(f)
        data['commit'] = data['commit'] + 1
        data['update_datetime'] = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    
    with open('./update.json', 'w', encoding='utf-8') as f:
        f.write(json.dumps(data, ensure_ascii=False, indent=4))
    print(f"Update complete: {data}")

    repo = git.Repo(os.getcwd())
