# 🎨 Creative Production Pipeline

*Professional AI creative production system - The synthesis of av-pair and fever-dream-pipeline*

## The Evolution Complete

This is the final form of a journey that began with simple audio-video synchronization:

1. **[av-pair](https://github.com/closestfriend/av-pair)** - The thesis: Pure, innocent A/V sync
2. **[fever-dream-pipeline](https://github.com/closestfriend/fever-dream-pipeline)** - The antithesis: Cursed content chaos
3. **This repo** - The synthesis: Professional creative production

## ⚡ Quick Start (30 seconds)

```bash
# The fastest way to get started
python quickstart.py
```

This will:
1. Check your Python version
2. Install requirements
3. Verify your API token
4. Run a demo generation

## 🚀 What This Does

Transforms creative briefs into multi-modal marketing assets using AI:
- **Product launches** - Hero shots, lifestyle imagery, launch soundtracks
- **Social campaigns** - Engaging visuals, viral-ready content
- **Brand storytelling** - Documentary-style imagery, emotional scores
- **Educational content** - Infographics, tutorials, learning materials

## 📦 Quick Start

```bash
# Clone the repository
git clone https://github.com/closestfriend/creative-production-pipeline.git
cd creative-production-pipeline

# Install dependencies
pip install replicate

# Set your Replicate API token
export REPLICATE_API_TOKEN='your-token-here'

# Install the prediction downloader (essential for asset management)
npm install -g replicate-predictions-downloader

# Run the creative director
python3 creative_director.py
```

## 🎯 Usage

### Interactive Mode
```bash
python3 creative_director.py
# Then select:
# 1. Creative brief type
# 2. Quality level (draft/standard/premium)
```

### Python API
```python
from creative_director import CreativeDirector

director = CreativeDirector()

# Create a product launch campaign
results = director.create_campaign('product_launch', quality='standard')

# Access generated assets
for image in results['images']:
    print(f"Image: {image['url']}")
print(f"Audio: {results['audio']}")
```

## 📋 Available Briefs

### Product Launch
- Hero product shots
- Lifestyle usage scenes
- Detail close-ups
- Uplifting launch music

### Social Campaign
- Eye-catching posts
- Story formats
- Shareable designs
- Viral-ready audio

### Brand Story
- Documentary moments
- Values visualization
- Heritage montages
- Emotional soundtracks

### Educational Content
- Clean infographics
- Tutorial illustrations
- Concept explanations
- Focus-enhancing audio

## 🎯 Model Selection (Replicate's Official Picks)

### Image Generation
| Model | Specialty | Speed | Use Case |
|-------|-----------|-------|----------|
| **bytedance/seedream-3** | Best Overall | Medium | Hero assets, maximum quality |
| **black-forest-labs/flux-schnell** | Best Speed | ⚡ <1s | Rapid iteration, drafts |
| **ideogram-ai/ideogram-v3-turbo** | Best Text | Fast | Logos, text overlays |
| **recraft-ai/recraft-v3-svg** | Best SVG | Fast | Icons, logos, vectors |

### Video Generation
| Model | Type | Duration | Quality |
|-------|------|----------|---------|
| **CogVideoX-5B** | Text-to-video | 6s | State-of-the-art |
| **Stable Video Diffusion** | Image-to-video | 2-4s | Production ready |
| **Zeroscope v2** | Text-to-video | 3-10s | Longer clips |

*Source: [Replicate's official recommendations](https://replicate.com/collections)*

## ⚡ Quality Levels

- **Draft**: Fast generation (20 steps) - For quick concepts
- **Standard**: Balanced quality (30 steps) - For most uses
- **Premium**: Maximum quality (50 steps) - For hero assets

## 🏗 Architecture

```
creative_director.py
├── CreativeDirector class
│   ├── Brief templates (professional prompts)
│   ├── Quality settings
│   └── Campaign generation
├── Replicate integration
│   ├── SDXL for images
│   └── Riffusion for audio
└── Asset management
    ├── Organized outputs
    ├── Metadata tracking
    └── replicate-predictions-downloader (npm)
```

## 🔧 Asset Management

This pipeline includes [replicate-predictions-downloader](https://github.com/closestfriend/replicate-predictions-downloader), a custom npm package I built to solve a critical gap: Replicate deletes API-generated predictions after just 1 hour (web UI predictions last 30 days), and there was no tool to batch download them before they vanish.

```bash
# Download recent campaign assets
npx replicate-predictions-downloader --since "1 hour ago"

# Download all assets from today's sessions
npx replicate-predictions-downloader --since "today"

# Incremental downloads (only new predictions)
npx replicate-predictions-downloader --last-run
```

This tool is essential for:
- **Urgently preserving API-generated assets** (1-hour lifespan!)
- Batch downloading campaign materials before they disappear
- Organizing outputs by model and date
- Creating permanent backups of creative work
- Ensuring you don't lose expensive generations

## 📊 Output Structure

```
creative_outputs/
└── {brief_type}_{timestamp}/
    ├── campaign_metadata.json
    └── (downloaded assets if implemented)
```

## 🔄 Extending

Easy to add new briefs:
```python
self.briefs['new_brief'] = {
    'name': 'Brief Name',
    'prompts': [
        "image prompt 1",
        "image prompt 2",
        "image prompt 3"
    ],
    'audio': "audio generation prompt"
}
```

## 🎭 From Chaos to Order

This represents the synthesis of two opposing forces:
- The technical precision of av-pair
- The creative chaos of fever-dream-pipeline

The result: A professional tool that harnesses AI creativity for legitimate business use.

## 🖼️ Example Outputs

### Salem Aesthetic (FLUX Schnell)
Complex artistic brief: "trailer-park baroque, opulence-adjacent decay"
- Velvet-curtained F-150 in ornate interior
- Muddy ballet slippers with neon cross
- Ranchero chandelier in desert church

### Product Launch (SDXL)
Professional commercial photography:
- Minimalist hero shots
- Lifestyle product usage
- Detail close-ups

*Full gallery in `/examples`*

## 🔄 API Modularity

The pipeline is designed to be API-agnostic. While currently using Replicate, it can be adapted for:
- **Google Gemini** - Imagen API for images
- **OpenAI** - DALL-E 3 for images
- **Midjourney** - Via unofficial APIs
- **Stability AI** - Direct API access
- **RunwayML** - Video generation
- **ElevenLabs** - Audio generation

Simply swap the API calls in `creative_director.py` while keeping the same interface.

## 🚦 Roadmap

- [ ] Batch campaign generation
- [ ] A/B testing variants
- [ ] Brand guideline integration
- [x] Video generation support (multiple models)
- [ ] Campaign performance tracking
- [ ] Template marketplace
- [ ] Multi-API backend support

## 📜 License

MIT - Use freely for your creative productions

---

*"From thesis through antithesis to synthesis - the dialectical evolution of AI creativity"*