#!/usr/bin/env python3
"""
HaloOne Headphones Demo
Professional campaign generation using studio modes
"""

import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from creative_director import CreativeDirector
from mode_system import StudioModes, create_job_schema
import json

def demo_all_modes_for_haloone():
    """
    Demonstrate all studio modes with HaloOne headphones
    Shows the versatility of the mode system
    """

    director = CreativeDirector()
    studio_modes = StudioModes()

    product_name = "HaloOne"
    product_desc = "Premium wireless headphones with spatial audio and adaptive noise cancellation"

    print("""
    ============================================
    HALOONE HEADPHONES - Studio Mode Showcase
    ============================================

    Generating campaigns in all 6 studio modes...
    """)

    # Test each mode
    modes_to_test = [
        ('parallax_nocturne', 'Deep cinematic feel, perfect for premium tech'),
        ('rust_luxe_baroque', 'Luxury meets decay, high-fashion editorial'),
        ('kinetic_typography', 'Bold text-driven campaign, Swiss design'),
        ('webgl_dreams', '3D web aesthetic, interactive feel'),
        ('mineral_futurism', 'Sci-fi crystalline, future materials'),
        ('soft_brutalism', 'Architectural, monolithic with soft touches')
    ]

    results = {}

    for mode_name, description in modes_to_test:
        print(f"\n{'='*60}")
        print(f"MODE: {mode_name.upper()}")
        print(f"Style: {description}")
        print('='*60)

        # Generate job schema (for inspection)
        job_schema = create_job_schema(mode_name, product_name, product_desc)

        print("\n📋 Job Configuration:")
        print(f"   Models: {', '.join(set([job['model'] for job in job_schema['jobs'].values()]))}")

        mode_info = studio_modes.get_mode_info(mode_name)
        print(f"   Color Palette: {', '.join(mode_info['color_palette'][:3])}...")
        print(f"   Studio Inspiration: {mode_info['studio_inspiration']}")

        # Save job schema for reference
        schema_path = f"./creative_outputs/haloone_{mode_name}_schema.json"
        os.makedirs('./creative_outputs', exist_ok=True)
        with open(schema_path, 'w') as f:
            json.dump(job_schema, f, indent=2)
        print(f"   Schema saved: {schema_path}")

        # Optional: Actually generate the campaign
        generate = input("\n   Generate this campaign? (y/n): ").lower() == 'y'

        if generate:
            try:
                result = director.create_campaign(
                    mode=mode_name,
                    product_name=product_name,
                    product_desc=product_desc,
                    include_video=False,  # Faster without video
                    generate_landing=True
                )
                results[mode_name] = result
                print(f"   ✅ Campaign generated successfully!")
            except Exception as e:
                print(f"   ❌ Generation failed: {e}")
                results[mode_name] = {"error": str(e)}

    # Summary
    print("\n" + "="*60)
    print("CAMPAIGN GENERATION SUMMARY")
    print("="*60)

    for mode_name, result in results.items():
        if 'error' in result:
            print(f"❌ {mode_name}: Failed - {result['error'][:50]}...")
        else:
            print(f"✅ {mode_name}: Success")
            if result.get('images'):
                print(f"   - {len(result['images'])} images generated")
            if result.get('audio'):
                print(f"   - Audio track generated")
            if result.get('landing_page'):
                print(f"   - Landing page created")

    print("\n🎉 Demo complete! Check ./creative_outputs for all assets.")

def quick_haloone_demo():
    """
    Quick demo with single mode for HaloOne
    """
    print("""
    ====================================
    HALOONE - Quick Studio Mode Demo
    ====================================
    """)

    director = CreativeDirector()

    # Use Parallax Nocturne for premium tech aesthetic
    print("\n🎬 Generating campaign with Parallax Nocturne mode...")
    print("   (Locomotive-inspired, cinematic depth)")

    result = director.create_campaign(
        mode='parallax_nocturne',
        product_name='HaloOne',
        product_desc='Premium wireless headphones with spatial audio',
        include_video=True,
        generate_landing=True
    )

    print("\n✨ Campaign generated!")
    print(f"   Images: {len(result.get('images', []))}")
    print(f"   Video: {'Yes' if result.get('video') else 'No'}")
    print(f"   Audio: {'Yes' if result.get('audio') else 'No'}")
    print(f"   Landing Page: {'Yes' if result.get('landing_page') else 'No'}")

if __name__ == "__main__":
    import argparse

    parser = argparse.ArgumentParser(description='HaloOne Campaign Demo')
    parser.add_argument('--all', action='store_true',
                        help='Test all studio modes')
    parser.add_argument('--quick', action='store_true',
                        help='Quick single-mode demo')

    args = parser.parse_args()

    if args.all:
        demo_all_modes_for_haloone()
    else:
        quick_haloone_demo()