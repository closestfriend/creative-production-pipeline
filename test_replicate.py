#!/usr/bin/env python3
"""
Test Replicate API connection and model availability
"""

import os
import replicate

print("Testing Replicate API...")
print(f"API Token set: {'REPLICATE_API_TOKEN' in os.environ}")

if 'REPLICATE_API_TOKEN' in os.environ:
    print(f"Token starts with: {os.environ['REPLICATE_API_TOKEN'][:8]}...")

    # Test with a simple, reliable model
    print("\nTesting with SDXL image generation (known working model)...")
    try:
        output = replicate.run(
            "stability-ai/sdxl:39ed52f2a78e934b3ba6e2a89f5b1c712de7dfea535525255b1aa35c5565e08b",
            input={
                "prompt": "a colorful cartoon character",
                "width": 512,
                "height": 512
            }
        )
        print(f"✅ SDXL test successful!")
        print(f"Output type: {type(output)}")
        if hasattr(output, '__dict__'):
            print(f"Output attributes: {output.__dict__}")
        else:
            print(f"Output: {output}")
    except Exception as e:
        print(f"❌ SDXL test failed: {e}")

    # Test available music models
    print("\nChecking music generation models...")
    music_models = [
        ("meta/musicgen:671ac645ce5e552cc63a54a2bbff63fcf798043055d2dac5fc9e36a837eedcfb", "MusicGen (Meta)"),
        ("riffusion/riffusion:8cf61ea6c56afd61d8f5b9ffd14d7c216c0a93844ce2d82ac1c9ecc9c7f24e05", "Riffusion"),
    ]

    for model_id, name in music_models:
        print(f"\nTesting {name}...")
        try:
            output = replicate.run(
                model_id,
                input={
                    "prompt_a": "upbeat children's song",
                    "denoising": 0.75,
                    "seed_image_id": "vibes"
                } if "riffusion" in model_id else {
                    "prompt": "cheerful children's music",
                    "duration": 5
                }
            )
            print(f"✅ {name} is available!")
            if output:
                print(f"   Output type: {type(output)}")
        except Exception as e:
            error_str = str(e)
            if "404" in error_str:
                print(f"⚠️ {name} model not found")
            elif "401" in error_str or "403" in error_str:
                print(f"❌ {name} authentication error - check API token")
            else:
                print(f"❌ {name} error: {e}")

    # Check video models
    print("\n\nChecking video generation models...")
    video_models = [
        ("stability-ai/stable-video-diffusion:3f0457e4619daac51203dedb472816fd4af51f3149fa7a9e0b5ffcf1b8172438", "Stable Video Diffusion"),
        ("andreasjansson/stable-diffusion-animation:ca1f5e306e5721e19c473e0d094e6603f0456fe759c10715fcd6c1b79242d4a5", "SD Animation"),
    ]

    for model_id, name in video_models:
        print(f"\nTesting {name}...")
        try:
            # Just check if we can start the model, don't wait for full generation
            prediction = replicate.predictions.create(
                version=model_id,
                input={
                    "prompt": "test" if "animation" in model_id else {},
                }
            )
            print(f"✅ {name} is available! (Prediction ID: {prediction.id})")
            # Cancel the prediction to save resources
            try:
                prediction.cancel()
            except:
                pass
        except Exception as e:
            error_str = str(e)
            if "404" in error_str:
                print(f"⚠️ {name} model not found")
            elif "401" in error_str or "403" in error_str:
                print(f"❌ {name} authentication error")
            else:
                print(f"❌ {name} error: {e}")

else:
    print("❌ REPLICATE_API_TOKEN environment variable not found!")
    print("\nTo set it, run:")
    print("export REPLICATE_API_TOKEN='your-api-token-here'")