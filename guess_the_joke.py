'''
import numpy as np
import pandas as pd
from numpy import random
# Load the dataset
df = pd.read_csv("guess_the_joke/datasource/dataset.csv")
df.dropna(inplace = True)

df.describe()

data = df.loc[df['text'].str.contains('Why') | df['text'].str.contains('What')]
data.groupby(['humor']).count()

new_array = data.to_numpy()
true_array = []
false_array = []
my_array = []
for i in new_array:
    if i[-1] == True:
        true_array.append(i[0])
    else:
        false_array.append(i[0])
        
my_array.append(true_array)
my_array.append(false_array)

my_joke = random.choice(random.choice(my_array, p=[len(true_array)/len(new_array), 1 - (len(true_array)/len(new_array))]))
if my_joke in true_array:
    print(f'{my_joke} IS HUMOROUS')
else:
    print(f'{my_joke} is NOT HUMOROUS')'''


import numpy as np
import pandas as pd
from numpy import random
import gradio as gr

# Load the dataset
df = pd.read_csv("datasource/dataset.csv")
df.dropna(inplace=True)

data = df.loc[df['text'].str.contains('Why') | df['text'].str.contains('What')]

def predict_my_joke(text):
    true_array = data[data['humor'] == True]['text'].tolist()
    false_array = data[data['humor'] == False]['text'].tolist()
    
    my_array = []
    my_array.append(true_array)
    my_array.append(false_array)
    
    my_joke = random.choice(random.choice(my_array, p=[len(true_array)/len(data), 1 - (len(true_array)/len(data))]))
    
    if my_joke in true_array:
        return f'{my_joke} IS HUMOROUS'
    else:
        return f'{my_joke} is NOT HUMOROUS'

# Create a Gradio interface
#iface = gr.Interface(fn=predict_my_joke, inputs=gr.inputs.Textbox(label="Joke Text"), outputs="text", title="Guess My Joke")
html_template = """
<div class="input-container">
    <textarea id="input" class="textbox" placeholder="{{placeholder}}"></textarea>
    <button id="submit-button" class="custom-button" type="submit">{{button_label}}</button>
</div>
"""

# Create a Gradio interface with the custom HTML template
iface = gr.Interface(
    fn=predict_my_joke, 
    inputs=gr.inputs.Textbox(label="Joke Text", placeholder="Enter a joke here...", lines=1), 
    outputs="text", 
    title="Guess My Joke",
    layout="vertical",
    allow_flagging=False,
    theme="compact",
    template=html_template,
    examples=[
        ["Why was the math book sad? Because it had too many problems."],
        ["What did one wall say to the other wall? I'll meet you at the corner."],
        ["How do you catch a squirrel? Climb up a tree and act like a nut!"]
    ]
)

# Launch the interface
iface.launch(share=True)
