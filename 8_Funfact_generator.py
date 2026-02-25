# This program creates a small website that shows a random fun fact every time you click a button.

import json
import requests
from pywebio.input import *
from pywebio.output import *
from pywebio.session import *

def get_fun_fact(_):
    clear()
    
    put_html(
        '<p align="left">'
        '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
        '</p>'
    )
    
    url = "https://uselessfacts.jsph.pl/random.json?language=en" # website that gives random facts in JSON format.
    
    response = requests.get(url)  #sends req to website
    data = json.loads(response.text) # The website sends data in JSON format.
                                     # We converted into Python dictionary.
    
    useless_fact = data['text']
    style(put_text(useless_fact), 'color:Red; font-size: 35px')
    
    put_buttons(
        [dict(label='Click Here', value='outline-success', color='outline-success')],
        onclick=get_fun_fact
    )

if __name__ == '__main__':
    put_html(
        '<p align="left">'
        '<h2><img src="https://media.geeksforgeeks.org/wp-content/uploads/20210720224119/MessagingHappyicon.png" width="7%"> Fun Fact Generator</h2>'
        '</p>'
    )
    
    put_buttons(
        [dict(label='Click me', value='outline-success', color='outline-success')],
        onclick=get_fun_fact
    )
    
    hold()