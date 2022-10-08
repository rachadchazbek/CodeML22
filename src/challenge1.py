from transformers import AutoTokenizer, AutoModelForMaskedLM

tokenizer = AutoTokenizer.from_pretrained("xlm-roberta-base")

model = AutoModelForMaskedLM.from_pretrained("xlm-roberta-base")