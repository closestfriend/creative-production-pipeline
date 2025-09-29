#!/usr/bin/env python3
"""
CREATIVE DIRECTOR - Professional AI Production Pipeline
The synthesis of av-pair and fever-dream-pipeline
"""

import replicate
import os
import json
import time
from pathlib import Path

class CreativeDirector:
    """
    Professional creative production using AI models.
    Straightforward implementation for easy testing.
    """

    def __init__(self):
        self.output_dir = Path('./creative_outputs')
        self.output_dir.mkdir(exist_ok=True)

        # Same reliable models, professional use
        self.models = {
            'image': 'stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b',
            'audio': 'riffusion/riffusion:8cf61ea6c56afd61d8f5b9ffd14d7c216c0a93844ce2d82ac1c9ecc9c7f24e05'
        }

        # Professional creative briefs (replacing cursed themes)
        self.briefs = {
            'product_launch': {
                'name': 'Product Launch Campaign',
                'prompts': [
                    "sleek product hero shot, minimalist background, professional lighting, commercial photography",
                    "product in use, lifestyle setting, happy customer, bright natural lighting",
                    "product detail close-up, highlighting features, studio lighting, premium quality"
                ],
                'audio': "uplifting corporate music, inspiring, modern, professional presentation soundtrack"
            },
            'social_campaign': {
                'name': 'Social Media Campaign',
                'prompts': [
                    "eye-catching social media post, vibrant colors, trending design, Instagram aesthetic",
                    "engaging story format, vertical composition, bold typography, social media graphics",
                    "shareable content design, modern illustration style, bright and optimistic"
                ],
                'audio': "upbeat social media music, catchy, short form content, viral sound"
            },
            'brand_story': {
                'name': 'Brand Storytelling',
                'prompts': [
                    "authentic brand moment, documentary style, real people, natural environment",
                    "company values visualization, abstract concept art, meaningful symbolism",
                    "brand heritage montage, timeline visualization, evolution story"
                ],
                'audio': "emotional brand music, storytelling soundtrack, inspiring narrative score"
            },
            'educational_content': {
                'name': 'Educational Content',
                'prompts': [
                    "clean infographic design, data visualization, educational poster, clear typography",
                    "step-by-step tutorial illustration, instructional design, helpful diagrams",
                    "educational animation frame, explaining concept, simple and clear visuals"
                ],
                'audio': "educational background music, focus-enhancing, calm learning atmosphere"
            }
        }

        # Professional quality settings
        self.quality_levels = {
            'draft': {'steps': 20, 'guidance': 7.5},
            'standard': {'steps': 30, 'guidance': 10},
            'premium': {'steps': 50, 'guidance': 15}
        }

    def create_campaign(self, brief_type: str, quality: str = 'standard'):
        """
        Create a complete campaign with images and audio.
        Straightforward implementation for testing.
        """

        brief = self.briefs.get(brief_type, self.briefs['product_launch'])
        quality_settings = self.quality_levels.get(quality, self.quality_levels['standard'])

        print(f"\n{'='*60}")
        print(f"🎬 CREATING: {brief['name']}")
        print(f"📊 Quality: {quality.upper()}")
        print(f"{'='*60}")

        results = {
            'brief_type': brief_type,
            'quality': quality,
            'images': [],
            'audio': None,
            'timestamp': int(time.time())
        }

        # Generate campaign images
        print("\n📸 Generating campaign visuals...")
        for i, prompt in enumerate(brief['prompts'], 1):
            print(f"   Asset {i}/3: ", end='', flush=True)

            try:
                output = replicate.run(
                    self.models['image'],
                    input={
                        "prompt": prompt + ", professional quality, commercial use",
                        "negative_prompt": "amateur, low quality, watermark, blurry",
                        "width": 1024,
                        "height": 1024,
                        "num_outputs": 1,
                        "num_inference_steps": quality_settings['steps'],
                        "guidance_scale": quality_settings['guidance']
                    }
                )

                if output:
                    url = output[0] if isinstance(output, list) else output
                    results['images'].append({
                        'url': url,
                        'prompt': prompt,
                        'index': i
                    })
                    print("✅")
                else:
                    print("❌")

            except Exception as e:
                print(f"❌ ({str(e)[:30]}...)")

        # Generate campaign audio
        print("\n🎵 Generating campaign audio...")
        try:
            audio_output = replicate.run(
                self.models['audio'],
                input={
                    "prompt_a": brief['audio'],
                    "denoising": 0.75,
                    "seed_image_id": "vibes"
                }
            )

            if audio_output and isinstance(audio_output, dict):
                results['audio'] = audio_output.get('audio')
                print("   ✅ Audio generated!")

        except Exception as e:
            print(f"   ❌ Audio failed: {e}")

        # Save campaign metadata
        self._save_campaign(results, brief)

        return results

    def _save_campaign(self, results, brief):
        """Save campaign assets and metadata"""

        campaign_dir = self.output_dir / f"{results['brief_type']}_{results['timestamp']}"
        campaign_dir.mkdir(exist_ok=True)

        # Save metadata
        metadata_path = campaign_dir / 'campaign_metadata.json'

        # Convert to serializable format
        serializable_results = {
            'brief_type': results['brief_type'],
            'brief_name': brief['name'],
            'quality': results['quality'],
            'timestamp': results['timestamp'],
            'images': [
                {
                    'url': str(img['url']),
                    'prompt': img['prompt'],
                    'index': img['index']
                } for img in results['images']
            ],
            'audio': str(results['audio']) if results['audio'] else None
        }

        with open(metadata_path, 'w') as f:
            json.dump(serializable_results, f, indent=2)

        # Display results
        print(f"\n✨ CAMPAIGN CREATED ✨")
        print(f"📁 Location: {campaign_dir}")

        if results['images']:
            print(f"\n📸 Visual Assets: {len(results['images'])}")
            for img in results['images']:
                print(f"   {img['index']}. {img['prompt'][:50]}...")

        if results['audio']:
            print(f"\n🎵 Audio: {results['audio']}")

        print(f"\n💾 Metadata: {metadata_path}")

    def list_briefs(self):
        """List available creative briefs"""
        print("\n📋 Available Creative Briefs:")
        for key, brief in self.briefs.items():
            print(f"   • {key}: {brief['name']}")

    def list_quality_levels(self):
        """List available quality settings"""
        print("\n⚡ Quality Levels:")
        for level, settings in self.quality_levels.items():
            print(f"   • {level}: {settings['steps']} steps, {settings['guidance']} guidance")


def main():
    """Interactive creative director interface"""

    print("""
    🎨 CREATIVE PRODUCTION PIPELINE
    Professional AI Content Generation
    """)

    director = CreativeDirector()

    # Show available options
    director.list_briefs()
    print()
    director.list_quality_levels()

    # Get user input
    print("\n" + "="*40)

    briefs = list(director.briefs.keys())
    print("Select brief:")
    for i, brief in enumerate(briefs, 1):
        print(f"  {i}. {director.briefs[brief]['name']}")

    try:
        choice = int(input("\nChoice (1-4): ")) - 1
        brief_type = briefs[choice]

        quality = input("Quality (draft/standard/premium): ").lower()
        if quality not in director.quality_levels:
            quality = 'standard'

        # Generate campaign
        print(f"\n🚀 Generating {director.briefs[brief_type]['name']}...")
        results = director.create_campaign(brief_type, quality)

        print("\n✅ Production complete!")

    except (ValueError, IndexError) as e:
        print(f"Invalid input: {e}")
        print("Using defaults: product_launch / standard")
        director.create_campaign('product_launch', 'standard')


if __name__ == "__main__":
    main()