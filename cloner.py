import requests

url = input("url: ")
name = input("name for your index file: ")
def check():
    if "." in name:
        return name
    else :
        return name+".html"
def request(url):
    try:
        re = requests.get(url)
    except requests.exceptions.MissingSchema as e:
        print("use full website url without www example : https://example.com")
        exit()
    file = re.text
    te = open("templates/"+check(),'w',encoding="utf-8")
    te.write(file)
    te.close()
if __name__ == '__main__':
    request(url)