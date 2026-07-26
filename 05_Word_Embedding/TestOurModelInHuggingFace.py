
from huggingface_hub import hf_hub_download
from gensim.models import KeyedVectors

# Download files from Hugging Face
kv_file = hf_hub_download(
    repo_id="Sunil-Singh-Coder/word2vec-google-news-300",
    filename="word2vec-google-news-300.kv"
)

vectors_file = hf_hub_download(
    repo_id="Sunil-Singh-Coder/word2vec-google-news-300",
    filename="word2vec-google-news-300.kv.vectors.npy"
)

# Load the model
wv = KeyedVectors.load(kv_file, mmap="r")

