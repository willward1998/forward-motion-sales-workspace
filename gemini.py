#!/usr/bin/env python3
"""
gemini.py — Gemini Image Generation CLI for Forward Motion Medical
Usage: python gemini.py <command> [args]

Commands:
  image "<prompt>" [--output file.png] [--aspect 1:1|3:4|4:3|9:16|16:9] [--model name]
  edit "<image_path>" "<instruction>" [--output file.png] [--aspect 1:1|3:4|4:3|9:16|16:9]
"""

import sys
import os
import io
import re
from datetime import datetime

try:
    from google import genai
    from google.genai import types
except ImportError:
    print("ERROR: 'google-genai' not installed. Run: pip3 install google-genai")
    sys.exit(1)

try:
    from PIL import Image
except ImportError:
    print("ERROR: 'Pillow' not installed. Run: pip3 install Pillow")
    sys.exit(1)

try:
    from dotenv import load_dotenv
    load_dotenv()
except ImportError:
    print("ERROR: 'python-dotenv' not installed. Run: pip3 install python-dotenv")
    sys.exit(1)

GEMINI_API_KEY = os.getenv("GEMINI_API_KEY")

if not GEMINI_API_KEY:
    print("ERROR: Missing GEMINI_API_KEY. Add it to your .env file.")
    print("Get a free key at https://aistudio.google.com")
    sys.exit(1)

DEFAULT_MODEL = "gemini-2.5-flash-image"
VALID_ASPECTS = {"1:1", "3:4", "4:3", "9:16", "16:9"}
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
DEFAULT_OUTPUT_DIR = os.path.join(SCRIPT_DIR, "images")


# ── Helpers ──────────────────────────────────────────────────────────

def get_client():
    return genai.Client(api_key=GEMINI_API_KEY)


def auto_filename(prompt):
    slug = re.sub(r"[^a-z0-9]+", "-", prompt.lower()).strip("-")[:40]
    ts = datetime.now().strftime("%Y%m%d-%H%M%S")
    return f"{slug}-{ts}.png"


def resolve_output(output_flag, prompt):
    if output_flag:
        return os.path.abspath(output_flag)
    os.makedirs(DEFAULT_OUTPUT_DIR, exist_ok=True)
    return os.path.join(DEFAULT_OUTPUT_DIR, auto_filename(prompt))


def save_image(image_data, output_path):
    try:
        img = Image.open(io.BytesIO(image_data))
        img.save(output_path)
        print(f"Saved: {output_path}")
    except Exception as e:
        print(f"ERROR: Failed to save image — {e}")
        sys.exit(1)


def parse_flags(args):
    flags = {}
    positional = []
    i = 0
    while i < len(args):
        if args[i] == "--output" and i + 1 < len(args):
            flags["output"] = args[i + 1]
            i += 2
        elif args[i] == "--aspect" and i + 1 < len(args):
            aspect = args[i + 1]
            if aspect not in VALID_ASPECTS:
                print(f"ERROR: Invalid aspect ratio '{aspect}'")
                print(f"Valid options: {', '.join(sorted(VALID_ASPECTS))}")
                sys.exit(1)
            flags["aspect"] = aspect
            i += 2
        elif args[i] == "--model" and i + 1 < len(args):
            flags["model"] = args[i + 1]
            i += 2
        else:
            positional.append(args[i])
            i += 1
    flags["positional"] = positional
    return flags


# ── Commands ─────────────────────────────────────────────────────────

def generate_image(prompt, output_path, aspect_ratio=None, model=DEFAULT_MODEL):
    client = get_client()

    config_kwargs = {"response_modalities": ["IMAGE"]}
    if aspect_ratio:
        config_kwargs["image_config"] = types.ImageConfig(
            aspect_ratio=aspect_ratio
        )
    config = types.GenerateContentConfig(**config_kwargs)

    try:
        response = client.models.generate_content(
            model=model,
            contents=prompt,
            config=config,
        )
    except Exception as e:
        err = str(e)
        err_lower = err.lower()
        if "429" in err:
            print("ERROR: Rate limit hit. Wait a moment and try again.")
        elif "safety" in err_lower or "block" in err_lower:
            print("ERROR: Blocked by safety filter. Try rephrasing your prompt.")
        else:
            print(f"ERROR: {err}")
        sys.exit(1)

    # Extract image from response
    if response.candidates and response.candidates[0].content:
        for part in response.candidates[0].content.parts:
            if part.inline_data:
                save_image(part.inline_data.data, output_path)
                return

    # No image returned — check for text (safety message)
    if response.candidates and response.candidates[0].content:
        for part in response.candidates[0].content.parts:
            if part.text:
                print(f"No image generated. Model response: {part.text}")
                sys.exit(1)

    print("ERROR: No image in response. The prompt may have been blocked by safety filters.")
    print("Try rephrasing your prompt.")
    sys.exit(1)


def edit_image(image_path, instruction, output_path, aspect_ratio=None, model=DEFAULT_MODEL):
    if not os.path.exists(image_path):
        print(f"ERROR: File not found — {image_path}")
        sys.exit(1)

    # Load source image
    try:
        with open(image_path, "rb") as f:
            image_bytes = f.read()
    except Exception as e:
        print(f"ERROR: Could not read image — {e}")
        sys.exit(1)

    # Detect mime type
    ext = os.path.splitext(image_path)[1].lower()
    mime_map = {".png": "image/png", ".jpg": "image/jpeg", ".jpeg": "image/jpeg", ".webp": "image/webp"}
    mime_type = mime_map.get(ext, "image/png")

    client = get_client()

    config_kwargs = {"response_modalities": ["IMAGE"]}
    if aspect_ratio:
        config_kwargs["image_config"] = types.ImageConfig(
            aspect_ratio=aspect_ratio
        )
    config = types.GenerateContentConfig(**config_kwargs)

    image_part = types.Part(inline_data=types.Blob(mime_type=mime_type, data=image_bytes))
    text_part = types.Part(text=instruction)

    try:
        response = client.models.generate_content(
            model=model,
            contents=[image_part, text_part],
            config=config,
        )
    except Exception as e:
        err = str(e).lower()
        if "429" in err or "rate" in err:
            print("ERROR: Rate limit hit. Wait a moment and try again.")
        elif "safety" in err or "block" in err:
            print("ERROR: Blocked by safety filter. Try rephrasing your instruction.")
        else:
            print(f"ERROR: {e}")
        sys.exit(1)

    if response.candidates and response.candidates[0].content:
        for part in response.candidates[0].content.parts:
            if part.inline_data:
                save_image(part.inline_data.data, output_path)
                return

    print("ERROR: No image in response. Try rephrasing your instruction.")
    sys.exit(1)


# ── CLI dispatch ─────────────────────────────────────────────────────

def main():
    if len(sys.argv) < 2:
        print(__doc__)
        sys.exit(0)

    cmd = sys.argv[1]
    args = sys.argv[2:]

    if cmd == "image":
        if not args:
            print('Usage: python3 gemini.py image "<prompt>" [--output file.png] [--aspect 16:9]')
            sys.exit(1)
        flags = parse_flags(args)
        if not flags["positional"]:
            print('Usage: python3 gemini.py image "<prompt>" [--output file.png] [--aspect 16:9]')
            sys.exit(1)
        prompt = flags["positional"][0]
        output_path = resolve_output(flags.get("output"), prompt)
        generate_image(
            prompt=prompt,
            output_path=output_path,
            aspect_ratio=flags.get("aspect"),
            model=flags.get("model", DEFAULT_MODEL),
        )

    elif cmd == "edit":
        if len(args) < 2:
            print('Usage: python3 gemini.py edit "<image_path>" "<instruction>" [--output file.png]')
            sys.exit(1)
        flags = parse_flags(args)
        positional = flags["positional"]
        if len(positional) < 2:
            print('Usage: python3 gemini.py edit "<image_path>" "<instruction>" [--output file.png]')
            sys.exit(1)
        image_path = positional[0]
        instruction = positional[1]
        output_path = resolve_output(flags.get("output"), instruction)
        edit_image(
            image_path=image_path,
            instruction=instruction,
            output_path=output_path,
            aspect_ratio=flags.get("aspect"),
            model=flags.get("model", DEFAULT_MODEL),
        )

    else:
        print(f"Unknown command: {cmd}")
        print(__doc__)
        sys.exit(1)


if __name__ == "__main__":
    main()
