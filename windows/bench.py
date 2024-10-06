#!/usr/bin/env python
import os
import keras
import keras_nlp
from keras_nlp.models import GemmaBackbone, BertBackbone
from keras.models import load_model
from keras import backend as K
import tensorflow
from IPython.display import Markdown, display
import textwrap
import json
import pandas as pd
import gc
from dotenv import load_dotenv
import datetime

# set up KERAS parameters recommended by Google
os.environ["KERAS_BACKEND"] = "jax"  # Or "torch" or "tensorflow".
os.environ["XLA_PYTHON_CLIENT_MEM_FRACTION"]="1.00" # Avoid memory fragmentation on JAX backend.

# integrate KAGGLE API secret key
load_dotenv() # Make sure there is a file named ".env" with the key/value pairs in the "current" directory
os.environ["KAGGLE_USERNAME"] = os.getenv('KAGGLE_USERNAME') # Link to KAGGLE API secret key
os.environ["KAGGLE_KEY"] = os.getenv('KAGGLE_KEY') # Link to KAGGLE API secret key

# Load the model
st_time = datetime.datetime.now()
gemma_lm = keras_nlp.models.GemmaCausalLM.from_preset("gemma2_2b_en")
end_time = datetime.datetime.now()
print("\nModel Load Time:", end_time - st_time)
print()

# Run a prompt
template = "Instruction:\n{question}\n\nResponse:\n{answer}"
prompt = template.format( \
    question="What should I eat in when I visit Blahlabhlah?", \
    answer="")
print("\nPrompt:\n", prompt)
st_time = datetime.datetime.now()
completion = gemma_lm.generate(prompt, max_length=1024)
end_time = datetime.datetime.now()
response = completion.replace(prompt, "")
print("Response:\n", response)
print("\nInference time:", end_time - st_time)
print()
