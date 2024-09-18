
import keras
import keras_nlp
from keras_nlp.models import GemmaBackbone
from keras.models import load_model
import kagglehub

kagglehub.login()

gemma_lm = keras_nlp.models.GemmaCausalLM.from_preset("gemma2_2b_en")
#gemma_lm = GemmaBackbone.from_preset("gemma_2b_en", load_weights=False)
print(gemma_lm)
print(dir(gemma_lm))
#gemma_lm.load_weights("../data/gemma_lm_weights.weights.h5")

#backbone.enable_lora(2)
#print(dir(backbone))
#m = backbone.load_lora_weights("../data/lora_adapters_weights.weights.h5")
#print(m)
#model = load_model("../data/gemma_lm_weights.weights.h5")
#gemma_lm = keras_nlp.models.GemmaCausalLM.from_preset("gemma_2b_en". False)
#print(gemma_lm)

print("a")
prompt = template.format(
    instruction="Tell me a story. My name is Daniel.",
    response="",
)
sampler = keras_nlp.samplers.TopKSampler(k=3, seed=2)
print("b")
gemma_lm.compile(sampler=sampler)
print("c")
print(gemma_lm.generate(prompt, max_length=256))
print("d")
