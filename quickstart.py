#!/usr/bin/env python3
"""
Quick Start Script - Get running in 30 seconds
"""

import os
import sys
import subprocess

def check_requirements():
    """Check if everything is installed"""
    print("🔍 Checking requirements...")

    # Check Python version
    if sys.version_info < (3, 8):
        print("❌ Python 3.8+ required")
        return False

    # Check for replicate
    try:
        import replicate
        print("✅ Replicate library installed")
    except ImportError:
        print("📦 Installing requirements...")
        subprocess.run([sys.executable, "-m", "pip", "install", "-r", "requirements.txt"])

    # Check for API token
    if not os.getenv('REPLICATE_API_TOKEN'):
        print("\n⚠️  No REPLICATE_API_TOKEN found!")
        print("Get your token at: https://replicate.com/account/api-tokens")
        token = input("Paste your token here (or press Enter to skip): ").strip()
        if token:
            print(f"\nAdd this to your shell profile:")
            print(f"export REPLICATE_API_TOKEN='{token}'")
            os.environ['REPLICATE_API_TOKEN'] = token
        else:
            return False
    else:
        print("✅ API token configured")

    return True

def quick_demo():
    """Run a quick demo"""
    from creative_director import CreativeDirector

    print("\n🎨 QUICK DEMO - Generating sample content")
    print("=" * 50)

    director = CreativeDirector()

    print("\nAvailable options:")
    print("1. Professional Product Launch")
    print("2. Salem Aesthetic (Artistic)")
    print("3. Social Media Campaign")

    choice = input("\nSelect (1-3) or Enter for default: ").strip() or "1"

    brief_map = {
        "1": "product_launch",
        "2": "salem_aesthetic",
        "3": "social_campaign"
    }

    brief = brief_map.get(choice, "product_launch")

    print(f"\n🚀 Generating {brief} with FLUX (fast mode)...")

    results = director.create_campaign(
        brief_type=brief,
        quality='draft',  # Fast for demo
        include_video=False,  # Skip video for speed
        image_model='flux_schnell'  # Best model
    )

    print("\n✨ Demo complete!")
    print("\nNext steps:")
    print("1. Run 'python creative_director.py' for interactive mode")
    print("2. Check creative_outputs/ for your generated content")
    print("3. Use 'node download_assets.js' to batch download")

    return True

def main():
    print("""
    ⚡ CREATIVE PRODUCTION PIPELINE - Quick Start
    ============================================
    """)

    if not check_requirements():
        print("\n❌ Setup incomplete. Please fix the issues above.")
        return 1

    print("\n✅ All requirements met!")

    run_demo = input("\nRun a quick demo? (Y/n): ").strip().lower()
    if run_demo != 'n':
        quick_demo()
    else:
        print("\nRun 'python creative_director.py' to start creating!")

    return 0

if __name__ == "__main__":
    sys.exit(main())