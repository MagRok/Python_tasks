
#Create a function that:
#  reads the file given as an argument.
# pulls a list of all the unique IP addresses and domains in the file.
# pulls out a list of all the unique status of HTTP requests.
#returns a tuple consisting of both letters.






def parse_log(filename):
    import re
        with open('filename') as m:
    content = m.read()
    domeny = re.findall(r'(\S+)\s-\s-', content)
    myset=set(domeny)
    domeny_uniq=list(myset)
    http = re.findall(r'\s(\d\d\d)\s', content)
    myset2=set(http)
    http_uniq=list(myset2)
    return wynik = (domeny_uniq, http_uniq)
