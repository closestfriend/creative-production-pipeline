#!/usr/bin/env python3
"""
FAST REPLICATE CURSED CONTENT GENERATOR
Uses image sequences instead of slow video models
"""

import replicate
import os
import json
import time
from pathlib import Path

class FastCursedGenerator:
    """Fast generation using images + audio only"""

    def __init__(self):
        self.output_dir = Path('/Users/hnsk/Projects/Development/av-pair/replicate_output')
        self.output_dir.mkdir(exist_ok=True)

        # Fast, reliable models only
        self.models = {
            'image': 'stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b',
            'audio': 'riffusion/riffusion:8cf61ea6c56afd61d8f5b9ffd14d7c216c0a93844ce2d82ac1c9ecc9c7f24e05'
        }

        self.themes = {
            'toy_unboxing_medical': {
                'prompts': [
                    "3D cartoon doctor holding colorful surprise egg, hospital room, bright colors",
                    "3D cartoon doctor opening surprise egg revealing toy stethoscope, excited expression",
                    "3D cartoon doctor showing toy medical equipment from egg, children's educational style"
                ],
                'audio': "cheerful nursery rhyme with medical beeps, educational children's song"
            },
            'learning_colors_wrong': {
                'prompts': [
                    "3D animated finger family, red object labeled 'BLUE' in big letters, classroom",
                    "3D cartoon teacher pointing at green apple with 'YELLOW' label, confused children",
                    "Colorful animated shapes with wrong color labels, educational video style"
                ],
                'audio': "educational colors song but slightly off-key, children's learning music"
            },
            'superhero_pregnancy': {
                'prompts': [
                    "3D cartoon pregnant Spider-Man at baby shower, balloons and decorations",
                    "3D cartoon pregnant Elsa opening baby gifts, superhero theme party",
                    "Cartoon superheroes celebrating with baby items, pastel colors"
                ],
                'audio': "superhero theme mixed with lullaby, celebration music"
            },
            'toilet_training_chaos': {
                'prompts': [
                    "3D animated smiling toilet character with eyes, colorful bathroom",
                    "Happy cartoon toilet celebrating with confetti, potty training success",
                    "Dancing toilet character with children cheering, educational style"
                ],
                'audio': "potty training celebration song with flush sounds, upbeat children's music"
            }
        }

    def generate_fast_production(self, theme: str, cursedness: int = 5):
        """Generate images + audio quickly"""

        print(f"\n{'='*60}")
        print(f"⚡ FAST CURSED PRODUCTION: {theme.upper()}")
        print(f"   Cursedness Level: {cursedness}/10")
        print(f"{'='*60}")

        theme_data = self.themes.get(theme, self.themes['learning_colors_wrong'])
        results = {'theme': theme, 'cursedness': cursedness, 'images': [], 'audio': None}

        # Generate 3 key frame images
        print("\n🖼️ Generating cursed images...")
        for i, prompt in enumerate(theme_data['prompts'], 1):
            print(f"   Frame {i}/3: ", end='', flush=True)

            # Add cursedness modifiers
            if cursedness > 7:
                prompt += ", surreal, fever dream, uncanny valley, distorted"
            elif cursedness > 4:
                prompt += ", slightly unsettling, oversaturated colors"

            try:
                output = replicate.run(
                    self.models['image'],
                    input={
                        "prompt": prompt + ", YouTube Kids content, 3D render",
                        "negative_prompt": "realistic, adult, dark, scary",
                        "width": 1024,
                        "height": 576,
                        "num_outputs": 1,
                        "num_inference_steps": 20  # Faster inference
                    }
                )

                if output:
                    url = output[0] if isinstance(output, list) else output
                    results['images'].append(url)
                    print("✅")
                else:
                    print("❌")

            except Exception as e:
                print(f"❌ ({e})")

        # Generate audio
        print("\n🎵 Generating cursed audio...")
        try:
            audio_output = replicate.run(
                self.models['audio'],
                input={
                    "prompt_a": theme_data['audio'],
                    "denoising": 0.75,
                    "seed_image_id": "vibes"
                }
            )

            if audio_output and isinstance(audio_output, dict):
                results['audio'] = audio_output.get('audio')
                print("   ✅ Audio generated!")

        except Exception as e:
            print(f"   ❌ Audio failed: {e}")

        # Save results (handle FileOutput objects)
        timestamp = int(time.time())
        metadata_path = self.output_dir / f"fast_{theme}_{timestamp}.json"

        # Convert FileOutput objects to strings
        serializable_results = {}
        for key, value in results.items():
            if isinstance(value, list):
                serializable_results[key] = [str(v) if hasattr(v, '__dict__') else v for v in value]
            elif hasattr(value, '__dict__'):
                serializable_results[key] = str(value)
            else:
                serializable_results[key] = value

        with open(metadata_path, 'w') as f:
            json.dump(serializable_results, f, indent=2, default=str)

        # Display results
        print(f"\n✨ PRODUCTION COMPLETE ✨")
        print(f"📁 Metadata: {metadata_path}")

        if results['images']:
            print(f"\n🖼️ Images generated: {len(results['images'])}")
            for i, url in enumerate(results['images'], 1):
                print(f"   Frame {i}: {url}")

        if results['audio']:
            print(f"\n🎵 Audio: {results['audio']}")

        return results


if __name__ == "__main__":
    print("""
    ⚡ FAST CURSED CONTENT GENERATOR ⚡
    (Image sequences + Audio only)
    """)

    generator = FastCursedGenerator()

    themes = list(generator.themes.keys())
    print("Select theme:")
    for i, theme in enumerate(themes, 1):
        print(f"  {i}. {theme.replace('_', ' ').title()}")

    try:
        choice = int(input("\nChoice (1-4): ")) - 1
        theme = themes[choice]
        cursedness = int(input("Cursedness (1-10): "))

        generator.generate_fast_production(theme, cursedness)

        print("\n🎭 SUBSCRIBE FOR MORE CURSED CONTENT! 🎭")

    except Exception as e:
        print(f"Error: {e}")