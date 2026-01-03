# llm-ci-troubleshooter
This project is a proof-of-concept LLM agent that analyzes CI build logs and suggests probable root causes and remediation steps.

# Pre-requisite
1. MacOS
2. python 3.9+

Steps:
Open terminal

sunilpoojary@192 ~ % python3 --version
Python 3.9.6
sunilpoojary@192 ~ %

1️⃣ Clone the Repository

sunilpoojary@192 ~ % mkdir llm-ci-troubleshoot
sunilpoojary@192 ~ % cd llm-ci-troubleshoot 
sunilpoojary@192 llm-ci-troubleshoot % git clone https://github.com/sundbgit/llm-ci-troubleshooter.git
Cloning into 'llm-ci-troubleshooter'...
remote: Enumerating objects: 3, done.
remote: Counting objects: 100% (3/3), done.
remote: Compressing objects: 100% (2/2), done.
remote: Total 3 (delta 0), reused 0 (delta 0), pack-reused 0 (from 0)
Receiving objects: 100% (3/3), done.
sunilpoojary@192 llm-ci-troubleshoot % ls
llm-ci-troubleshooter
sunilpoojary@192 llm-ci-troubleshoot % cd llm-ci-troubleshooter 
sunilpoojary@192 llm-ci-troubleshooter %

2️⃣ Create & Activate Virtual Environment

sunilpoojary@192 llm-ci-troubleshooter % python3 -m venv venv
sunilpoojary@192 llm-ci-troubleshooter % source venv/bin/activate
(venv) sunilpoojary@192 llm-ci-troubleshooter % 

3️⃣ Install Dependencies

(venv) sunilpoojary@192 llm-ci-troubleshooter % pip install --upgrade pip
Requirement already satisfied: pip in ./venv/lib/python3.9/site-packages (21.2.4)
Collecting pip
  Downloading pip-25.3-py3-none-any.whl (1.8 MB)
     |████████████████████████████████| 1.8 MB 4.1 MB/s 
Installing collected packages: pip
  Attempting uninstall: pip
    Found existing installation: pip 21.2.4
    Uninstalling pip-21.2.4:
      Successfully uninstalled pip-21.2.4
Successfully installed pip-25.3
(venv) sunilpoojary@192 llm-ci-troubleshooter % pip install torch transformers fastapi uvicorn sentence-transformers faiss-cpu
Collecting torch
Downloading threadpoolctl-3.6.0-py3-none-any.whl (18 kB)
Installing collected packages: mpmath, urllib3, typing-extensions, tqdm, threadpoolctl, sympy, safetensors, regex, pyyaml, Pillow, packaging, numpy, networkx, MarkupSafe, joblib, idna, hf-xet, h11, fsspec, filelock, click, charset_normalizer, certifi, annotated-types, annotated-doc, uvicorn, typing-inspection, scipy, requests, pydantic-core, jinja2, faiss-cpu, exceptiongroup, torch, scikit-learn, pydantic, huggingface-hub, anyio, tokenizers, starlette, transformers, fastapi, sentence-transformers
Successfully installed MarkupSafe-3.0.3 Pillow-11.3.0 annotated-doc-0.0.4 annotated-types-0.7.0 anyio-4.12.0 certifi-2025.11.12 charset_normalizer-3.4.4 click-8.1.8 exceptiongroup-1.3.1 faiss-cpu-1.13.0 fastapi-0.128.0 filelock-3.19.1 fsspec-2025.10.0 h11-0.16.0 hf-xet-1.2.0 huggingface-hub-0.36.0 idna-3.11 jinja2-3.1.6 joblib-1.5.3 mpmath-1.3.0 networkx-3.2.1 numpy-2.0.2 packaging-25.0 pydantic-2.12.5 pydantic-core-2.41.5 pyyaml-6.0.3 regex-2025.11.3 requests-2.32.5 safetensors-0.7.0 scikit-learn-1.6.1 scipy-1.13.1 sentence-transformers-5.1.2 starlette-0.49.3 sympy-1.14.0 threadpoolctl-3.6.0 tokenizers-0.22.1 torch-2.8.0 tqdm-4.67.1 transformers-4.57.3 typing-extensions-4.15.0 typing-inspection-0.4.2 urllib3-2.6.2 uvicorn-0.39.0
(venv) sunilpoojary@192 llm-ci-troubleshooter % 

4️⃣ Create CI Knowledge Base. ( From previous build run or extract it from sources)

< Work in Progress >

