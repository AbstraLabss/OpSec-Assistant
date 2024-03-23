import os
from chromadb.config import Settings
# https://python.langchain.com/en/latest/modules/indexes/document_loaders/examples/excel.html?highlight=xlsx#microsoft-excel
from langchain.document_loaders import CSVLoader, PDFMinerLoader, TextLoader, UnstructuredExcelLoader, UnstructuredWordDocumentLoader

import openai
from langchain.document_loaders import UnstructuredURLLoader
from langchain.embeddings import OpenAIEmbeddings
from dotenv import load_dotenv
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

ROOT_DIRECTORY = os.path.dirname(os.path.realpath(__file__))

# Define the folder for storing database
SOURCE_DIRECTORY = f"./dataset"

EMBEDDING_DIRECTORY = f"./Embedding"

# Can be changed to a specific number
INGEST_THREADS = os.cpu_count() or 8

# Define the Chroma settings 
# CHROMA_SETTINGS = Settings(
#     persist_directory=EMBEDDING_DIRECTORY, anonymized_telemetry=False
# )

# Define Search URL path
URL_PATH = ["https://docs.starknet.io/documentation/",
            "https://docs.starknet.io/documentation/quick_start/environment_setup/",
            "https://docs.starknet.io/documentation/quick_start/set_up_an_account/",
            "https://docs.starknet.io/documentation/quick_start/declare_a_smart_contract/",
            "https://docs.starknet.io/documentation/quick_start/deploy_a_smart_contract/",
            "https://docs.starknet.io/documentation/quick_start/interact_with_a_smart_contract/",
            "https://docs.starknet.io/documentation/starknet_versions/version_notes/",
            "https://docs.starknet.io/documentation/starknet_versions/upcoming_versions/",
            "https://docs.starknet.io/documentation/starknet_versions/deprecated/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Network_Architecture/header/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Network_Architecture/transaction-life-cycle/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Network_Architecture/transactions/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Network_Architecture/fee-mechanism/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Network_Architecture/starknet-state/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Network_Architecture/on-chain-data/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Network_Architecture/messaging-mechanism/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Network_Architecture/token-bridge/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Accounts/introduction/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Accounts/approach/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Accounts/validate_and_execute/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Accounts/deploying_new_accounts/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Accounts/simplified_transaction_flow/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Smart_Contracts/contract-classes/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Smart_Contracts/class-hash/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Smart_Contracts/contract-address/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Smart_Contracts/contract-storage/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Smart_Contracts/contract-abi/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Smart_Contracts/starknet-events/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Smart_Contracts/contract-syntax/index.html",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Smart_Contracts/cairo-and-sierra/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Smart_Contracts/system-calls-cairo1/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Cryptography/p-value/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Cryptography/hash-functions/",
            "https://docs.starknet.io/documentation/architecture_and_concepts/Cryptography/stark-curve/",
            "https://docs.starknet.io/documentation/tools/starknet-book/",
            "https://docs.starknet.io/documentation/tools/devtools/",
            "https://docs.starknet.io/documentation/cli/starkli/",
            "https://docs.starknet.io/documentation/cli/starknet-compiler-options/",
            "https://docs.starknet.io/documentation/tools/api-services/",
            "https://docs.starknet.io/documentation/starknet_versions/juno_versions/",
            "https://docs.starknet.io/documentation/starknet_versions/pathfinder_versions/",
            "https://docs.starknet.io/documentation/tools/important_addresses/",
            "https://docs.starknet.io/documentation/tools/limits_and_triggers/",
            "https://docs.starknet.io/documentation/tools/ref_block_explorers/",
            "https://docs.starknet.io/documentation/tools/audit/"
            ]

### 
# Embedding model
###

EMBEDDING_MODEL_NAME = OpenAIEmbeddings(model = "text-embedding-ada-002")


###
# Generation model
###