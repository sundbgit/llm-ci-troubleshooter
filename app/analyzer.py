# log analysis logic

from app.model_loader import model, tokenizer

def analyze_log(ci_log):

    prompt = f"""
You are an DevOps expert.

Analyze the CI failure and suggest a fix.

CI Log:
{ci_log}

Fix:
"""

    inputs = tokenizer(prompt, return_tensors="pt")

    outputs = model.generate(
        **inputs,
        max_new_tokens=60
    )

    return tokenizer.decode(outputs[0], skip_special_tokens=True)
