# Pixi

Production image resizer for developers.

<img alt="pixi logo" src="./pixi.webp" />

Resize, compress, and convert images to WebP for better web performance - without the headache.

## Why Pixi?

Every web developer knows: images are the #1 reason for slow websites. Even the fastest server can't compensate for 4MB images.

Pixi solves this at deployment time:
- ✅ Recursively finds all images in folders
- ✅ Resizes to max 1080px (keeps aspect ratio)
- ✅ Converts to WebP (smaller + better quality)
- ✅ Compresses with custom quality settings

## Quick Start

```bash
# Install dependencies
pip install -r requirements.txt
```

```bash
# Run (converts all images in current folder)
python pixi.py

# Or specify folder and quality
python pixi.py -p "./images" -q 80
```

## CLI Arguments

### path | -p

The path to the folder containing images (default: "./")

```bash
python pixi.py -p "./images"
```

### quality | -q

Compression quality 1-100 (default: 80)

```bash
python pixi.py -q 70
```

Lower = smaller file, higher = better quality

## Features

- 🔍 Recursively scans folders and subfolders
- 📦 Converts to WebP (.jpg, .jpeg, .png → .webp)
- 📏 Resizes to max 1080px (preserves aspect ratio)
- 🎛️ Adjustable compression quality (1-100)
- 🚀 CLI-based - automate in your deployment pipeline

## Use Case

Perfect for CI/CD pipelines - run pixi before deploying to ensure all images are optimized.
