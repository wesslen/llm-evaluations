# LLM Evaluations Examples

## Reference-based metrics:
  - [notebooks/01_llm_evaluations_reference_based.ipynb](https://github.com/wesslen/llm-evaluations/blob/main/notebooks/01_llm_evaluations_reference_based.ipynb)
  - Overlap (BLEU, ROUGE, METEOR), Similarity (BERTscore), several others
  - [Huggingface's `evaluate`](https://huggingface.co/docs/evaluate/en/index) package for consistent implementation

## RAG Evaluation: Triad evaluation via LLM-as-a-Judge (OpenAI) and Unit Testing: 
  - [notebooks/02_rag_deepeval_llama_index.ipynb](https://github.com/wesslen/llm-evaluations/blob/main/notebooks/02_rag_deepeval_llama_index.ipynb)
  - [Llama-index](https://docs.llamaindex.ai/en/stable/) and [DeepEval](https://docs.confident-ai.com/docs/getting-started)

## Vulnerability testing: Llama 3.1 8B Instruct endpoint with OpenAI Red Teaming
- [Promptfoo Shared Link of Results](https://app.promptfoo.dev/eval/f:777f50d8-b4ed-4af0-84d8-26ceba97268f/)
- [README instructions](./security-testing/README.md)
- Compared two prompts on 150 unit tests across six test plugins (PII, politics, off-topic) and four adversarial strategies (prompt injection, base64, etc.)
- View [Red Team Report](security-testing/redteam.yaml) (YAML file).
