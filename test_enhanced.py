#!/usr/bin/env python3
"""
Test enhanced pipeline with FLUX and video generation
"""

from creative_director import CreativeDirector

# Initialize director
director = CreativeDirector()

print("\n🚀 Testing Enhanced Pipeline with Salem Aesthetic")
print("=" * 50)

# Generate with FLUX Schnell (fast + high quality) and video
results = director.create_campaign(
    brief_type='salem_aesthetic',
    quality='premium',
    include_video=True,
    image_model='flux_schnell'
)

print("\n✅ Enhanced generation complete!")
print(f"Model used: FLUX Schnell")
print(f"Video generated: {'Yes' if results.get('video') else 'No'}")