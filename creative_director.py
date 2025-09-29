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

        # Enhanced model suite - Using Replicate's official recommendations
        self.models = {
            # Image models (Replicate's picks)
            'seedream': 'bytedance/seedream-3',  # BEST overall quality
            'flux_schnell': 'black-forest-labs/flux-schnell',  # BEST for speed
            'ideogram': 'ideogram-ai/ideogram-v3-turbo',  # BEST for text in images
            'recraft_svg': 'recraft-ai/recraft-v3-svg',  # BEST for SVG/logos

            # Additional proven models
            'flux_dev': 'black-forest-labs/flux-dev',  # High quality, slower
            'sdxl': 'stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b',  # Reliable fallback
            'playground': 'playgroundai/playground-v2.5-1024px-aesthetic:42fe626e41cc811eaf02c94b892774839268ce1994ea778eba97103fe1ef51b8',

            # Video models (expanded suite)
            'svd': 'stability-ai/stable-video-diffusion:3f0457e4619daac51203dedb472816fd4af51f3149fa7a9e0b5ffcf1b8172438',
            'cogvideox': 'fofr/cogvideox-5b:70e0d70174e00dce12207c7e015c5fb09e957ac5a8b0e5f7a04f2ac18009e519',  # Text-to-video
            'zeroscope': 'anotherjesse/zeroscope-v2-xl:9f747673945c62801b13b84701c783929c0ee784e4748ec062204894dda1a351',
            'animatediff': 'lucataco/animate-diff:1531004ee4c98894ab11f8a4ce6206099e732c1da15121987a8eef54828f0663',
            'i2vgen': 'ali-vilab/i2vgen-xl:5821a9d7c4b8a76ae89cf942779b41abaf377cd018bff9ccbd00d2b9c92bf0f0',

            # Audio models
            'riffusion': 'riffusion/riffusion:8cf61ea6c56afd61d8f5b9ffd14d7c216c0a93844ce2d82ac1c9ecc9c7f24e05',
            'musicgen': 'meta/musicgen:671ac645ce5e552cc63a54a2bbff63fcf798043055d2dac5fc9e36a837eedcfb'
        }

        # Default models for speed/quality balance
        self.default_image = 'flux_schnell'  # Best balance
        self.default_video = 'svd'  # Most reliable
        self.default_audio = 'riffusion'  # Fastest

        # Professional creative briefs (replacing cursed themes)
        self.briefs = {
            'salem_aesthetic': {
                'name': 'Salem Opulence-Adjacent Decay',
                'prompts': [
                    "couture-grunge texture, trailer-park baroque interior, gold grills beside crystal rosaries, velvet-curtained F-150 truck, resource-heavy chrome flipped to ruin porn, decision-grade creative vision",
                    "Catholic-ballerina iconography over trap-house neon, satin ballet slippers muddied in rural Michigan clay, abandoned K-mart crucifixes, Wal-Mart votive candles, gothic Americana meets Southern prosperity",
                    "Ranchero chandelier above lean-filled crystal stemware, crushed-velvet church pews, Confederate flag repurposed as couture cape, chrome ATV graveyard, oil-slick rainbow, bullion-tone filters"
                ],
                'audio': "trap-influenced church organ, Southern gothic hymnal, prosperity gospel choir over 808s, trailer-park baroque symphony"
            },
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

    def create_campaign(self, brief_type: str, quality: str = 'standard',
                        include_video: bool = False, video_type: str = 'image2video',
                        image_model: str = None, enhance_prompts: bool = False,
                        generate_landing: bool = False):
        """
        Create a complete campaign with images, video, and audio.
        Now with model selection and video generation.
        """

        brief = self.briefs.get(brief_type, self.briefs['product_launch'])
        quality_settings = self.quality_levels.get(quality, self.quality_levels['standard'])
        image_model = image_model or self.default_image

        print(f"\n{'='*60}")
        print(f"🎬 CREATING: {brief['name']}")
        print(f"📊 Quality: {quality.upper()}")
        print(f"🎨 Image Model: {image_model}")
        if include_video:
            print(f"🎥 Video: ENABLED")
        print(f"{'='*60}")

        results = {
            'brief_type': brief_type,
            'quality': quality,
            'model': image_model,
            'images': [],
            'video': None,
            'audio': None,
            'timestamp': int(time.time())
        }

        # Optional: Enhance prompts with LLM
        if enhance_prompts:
            from creative_enhancer import CreativeEnhancer
            enhancer = CreativeEnhancer(use_claude=os.getenv('USE_CLAUDE', False))
            print("\n✨ Enhancing prompts with AI...")
            enhanced_prompts = []
            for p in brief['prompts']:
                enhanced = enhancer.enhance_prompt(p)
                enhanced_prompts.append(enhanced)
                print(f"   ✓ Enhanced: {enhanced[:60]}...")
            brief['prompts'] = enhanced_prompts

        # Generate campaign images
        print("\n📸 Generating campaign visuals...")
        for i, prompt in enumerate(brief['prompts'], 1):
            print(f"   Asset {i}/3: ", end='', flush=True)

            try:
                # Different models have different parameters
                if 'flux' in image_model:
                    input_params = {
                        "prompt": prompt + ", professional quality, high detail",
                        "num_outputs": 1,
                        "aspect_ratio": "1:1",
                        "output_format": "png",
                        "output_quality": 95
                    }
                else:  # SDXL/Playground
                    input_params = {
                        "prompt": prompt + ", professional quality, commercial use",
                        "negative_prompt": "amateur, low quality, watermark, blurry",
                        "width": 1024,
                        "height": 1024,
                        "num_outputs": 1,
                        "num_inference_steps": quality_settings['steps'],
                        "guidance_scale": quality_settings['guidance']
                    }

                output = replicate.run(
                    self.models[image_model],
                    input=input_params
                )

                if output:
                    # Handle different output types
                    if isinstance(output, list):
                        url = output[0]
                    elif hasattr(output, 'url'):
                        url = output.url
                    else:
                        url = output

                    # Ensure URL is string
                    url = str(url) if not isinstance(url, str) else url

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

        # Generate video if requested
        if include_video:
            print(f"\n🎥 Generating campaign video ({video_type})...")
            try:
                if video_type == 'text2video':
                    # Direct text-to-video generation with CogVideoX
                    video_prompt = brief['prompts'][0] + ", high quality video, smooth motion"

                    video_output = replicate.run(
                        self.models['cogvideox'],
                        input={
                            "prompt": video_prompt,
                            "num_frames": 49,  # ~6 seconds at 8fps
                            "guidance_scale": 7,
                            "num_inference_steps": 50 if quality == 'premium' else 25
                        }
                    )
                elif video_type == 'zeroscope':
                    # Zeroscope for longer videos
                    video_prompt = brief['prompts'][0] + ", cinematic"

                    video_output = replicate.run(
                        self.models['zeroscope'],
                        input={
                            "prompt": video_prompt,
                            "width": 1024,
                            "height": 576,
                            "num_frames": 24,
                            "fps": 8
                        }
                    )
                else:  # Default image2video
                    if not results['images']:
                        print("   ⚠️ No images to animate, skipping video")
                        video_output = None
                    else:
                        hero_image = results['images'][0]['url']
                        video_output = replicate.run(
                            self.models[self.default_video],
                            input={
                                "input_image": hero_image,
                                "video_length": "14_frames",
                                "sizing_strategy": "maintain_aspect_ratio",
                                "frames_per_second": 7,
                                "motion_bucket_id": 127  # Medium motion
                            }
                        )

                if video_output:
                    # Handle FileOutput objects
                    if hasattr(video_output, 'url'):
                        results['video'] = video_output.url
                    elif isinstance(video_output, str):
                        results['video'] = video_output
                    else:
                        results['video'] = str(video_output)
                    print("   ✅ Video generated!")

            except Exception as e:
                print(f"   ❌ Video failed: {e}")

        # Generate campaign audio
        print("\n🎵 Generating campaign audio...")
        try:
            audio_output = replicate.run(
                self.models[self.default_audio],
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

        # Optional: Generate landing page
        if generate_landing:
            from creative_enhancer import CreativeEnhancer
            enhancer = CreativeEnhancer(use_claude=os.getenv('USE_CLAUDE', False))
            print("\n🌐 Generating landing page...")

            # Load the saved metadata for complete data
            campaign_dir = self.output_dir / f"{results['brief_type']}_{results['timestamp']}"
            metadata_path = campaign_dir / 'campaign_metadata.json'
            with open(metadata_path, 'r') as f:
                campaign_data = json.load(f)

            html = enhancer.generate_landing_page(campaign_data)
            landing_path = campaign_dir / 'index.html'
            with open(landing_path, 'w') as f:
                f.write(html)

            print(f"   ✅ Landing page: {landing_path}")
            results['landing_page'] = str(landing_path)

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
            'model': results.get('model', 'sdxl'),
            'timestamp': results['timestamp'],
            'images': [
                {
                    'url': str(img['url']),
                    'prompt': img['prompt'],
                    'index': img['index']
                } for img in results['images']
            ],
            'video': str(results['video']) if results.get('video') else None,
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

        if results.get('video'):
            print(f"\n🎥 Video: {results['video']}")

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