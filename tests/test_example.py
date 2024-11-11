
import pytest
from deepeval import assert_test
from deepeval.metrics import FaithfulnessMetric
from deepeval.test_case import LLMTestCase
from deepeval.dataset import EvaluationDataset, Golden

from llama_index.core import VectorStoreIndex, SimpleDirectoryReader
from llama_index.core import Settings

documents = SimpleDirectoryReader(".").load_data()

Settings.chunk_size = 100
Settings.chunk_overlap = 20

index = VectorStoreIndex.from_documents(documents)
rag_application = index.as_query_engine(similarity_top_k=4)

example_golden = Golden(input="Is it permissible for an employee to accept a cash gift from a customer as a thank you for exceptional service?")

dataset = EvaluationDataset(goldens=[example_golden])

@pytest.mark.parametrize(
    "golden",
    dataset.goldens,
)
def test_rag(golden: Golden):
    # LlamaIndex returns a response object that contains
    # both the output string and retrieved nodes
    response_object = rag_application.query(golden.input)

    # Process the response object to get the output string
    # and retrieved nodes
    if response_object is not None:
        actual_output = response_object.response
        retrieval_context = [node.get_content() for node in response_object.source_nodes]

    test_case = LLMTestCase(
        input=golden.input,
        actual_output=actual_output,
        retrieval_context=retrieval_context
    )
    print("\n")
    print(f"Query: {test_case.input}")
    print(f"Response: {test_case.actual_output}")
    print(f"Retrieval context: {test_case.retrieval_context}")
    answer_faithfulness_metric = FaithfulnessMetric(threshold=0.5)
    answer_faithfulness_metric.measure(test_case)
    print(f"Metric score: {answer_faithfulness_metric.score}")
    print(f"Metric reason: {answer_faithfulness_metric.reason}")
    assert_test(test_case, [answer_faithfulness_metric])
