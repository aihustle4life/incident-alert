import os
from pathlib import Path

from dotenv import load_dotenv
from google import genai


ROOT = Path(__file__).resolve().parent
MODEL = "gemini-3.8-flash"


def main() -> None:
    load_dotenv(ROOT / ".env")
    api_key = os.getenv("GEMINI_API_KEY")
    if not api_key or api_key == "your_gemini_api_key_here":
        raise RuntimeError("Set GEMINI_API_KEY in the project's .env file.")

    alert = (ROOT / "data" / "sample_alert.txt").read_text(encoding="utf-8")
    client = genai.Client(api_key=api_key)
    response = client.models.generate_content(
        model=MODEL,
        contents=(
            "Analyze this incident alert. Summarize the issue, customer impact, "
            "and recommended next steps.\n\n"
            f"{alert}"
        ),
    )
    print(response.text or "The model returned no text.")


if __name__ == "__main__":
    main()
