import fitz  # PyMuPDF
import re
import requests

pdf_path = "Wallet id - Google Sheets.pdf"

# Step 1: Extract wallets
wallet_pattern = re.compile(r"0x[a-fA-F0-9]{40}")
doc = fitz.open(pdf_path)
all_text = "".join([page.get_text() for page in doc])
wallets = sorted(set(wallet_pattern.findall(all_text)))
print(f"✅ Extracted {len(wallets)} wallet addresses.")

# Step 2: Call FastAPI
response = requests.post(
    "http://127.0.0.1:8000/score-wallets/",
    params=[("wallets", w) for w in wallets]
)

if response.status_code == 200:
    print("✅ FastAPI Response:")
    print(response.json())
else:
    print(f"❌ ERROR {response.status_code}: {response.text}")
