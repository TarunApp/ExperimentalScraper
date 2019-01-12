import numpy as np
import matplotlib.pyplot as plt
import time, random





							#Function to distribute data points throughout graph

url = "https://jasonduongism.weebly.com/"
request = requests.get(url)  # <---------- Move this into a seperate function
html_content = request.text
soup = BeautifulSoup(html_content, "html.parser")

def checktext():
    para = soup.body.findAll(text=re.compile('The purpose'))
    para2 = soup.body.findAll(text=re.compile('Click on the tabs'))
    paracombine = para + para2
    list(para)
    print(para)
    if "The purpose" in para or paracombine:
        print("True1")
        return True
        if "Click on" in para or para2:
            print("True2")
            return True
        else:
            print("False")
            return False
    else:
        print("False else")
        return False


import matplotlib.pyplot as plt
import numpy as np

# Fixing random state for reproducibility
np.random.seed(19680801)


plt.rcdefaults()
fig, ax = plt.subplots()

# Example data
people = ('Tom', 'Dick', 'Harry', 'Slim', 'Jim')
y_pos = np.arange(len(people))
performance = 3 + 10 * np.random.rand(len(people))
error = np.random.rand(len(people))

ax.barh(y_pos, performance, xerr=error, align='center',
        color='green', ecolor='black')
ax.set_yticks(y_pos)
ax.set_yticklabels(people)
ax.invert_yaxis()  # labels read top-to-bottom
ax.set_xlabel('Performance')
ax.set_title('How fast do you want to go today?')

plt.show()
