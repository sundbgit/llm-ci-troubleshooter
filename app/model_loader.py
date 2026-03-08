# phi2 model loading - LLM loading layer

from transformers import AutoTokenizer, AutoModelForCausalLM

MODEL_NAME = "microsoft/phi-2"

tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)

model = AutoModelForCausalLM.from_pretrained(
    MODEL_NAME,
    torch_dtype="auto"
)
