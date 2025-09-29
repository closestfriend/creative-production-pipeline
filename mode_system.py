#!/usr/bin/env python3
"""
Professional Creative Mode System
Studio-inspired aesthetic universes for cohesive multi-modal generation
"""

import json
from typing import Dict, List, Any, Optional
from dataclasses import dataclass, asdict

@dataclass
class ModeConfig:
    """Configuration for a creative mode"""
    name: str
    description: str
    studio_inspiration: str
    prompt_kernel: str
    negative_prompt: str
    color_palette: List[str]
    motion_style: str
    audio_character: str
    preferred_models: Dict[str, str]
    quality_settings: Dict[str, Any]

class CreativeMode:
    """Base class for creative modes"""

    def __init__(self, config: ModeConfig):
        self.config = config

    def get_image_prompt(self, base_prompt: str) -> Dict[str, Any]:
        """Generate image generation parameters"""
        return {
            "prompt": f"{base_prompt}, {self.config.prompt_kernel}",
            "negative_prompt": self.config.negative_prompt,
            "guidance_scale": self.config.quality_settings.get("guidance", 7.5),
            "num_inference_steps": self.config.quality_settings.get("steps", 30)
        }

    def get_video_prompt(self, base_prompt: str) -> Dict[str, Any]:
        """Generate video generation parameters"""
        return {
            "prompt": f"{base_prompt}, {self.config.motion_style}",
            "fps": self.config.quality_settings.get("fps", 8),
            "num_frames": self.config.quality_settings.get("frames", 24)
        }

    def get_audio_prompt(self, base_prompt: str) -> Dict[str, Any]:
        """Generate audio generation parameters"""
        return {
            "prompt": f"{base_prompt}, {self.config.audio_character}",
            "duration": self.config.quality_settings.get("audio_duration", 10)
        }

class StudioModes:
    """Professional creative modes inspired by award-winning studios"""

    def __init__(self):
        self.modes = {}
        self._initialize_modes()

    def _initialize_modes(self):
        """Initialize all studio-inspired modes"""

        # Mode 1: Parallax Nocturne (Locomotive-inspired)
        self.modes['parallax_nocturne'] = CreativeMode(ModeConfig(
            name="Parallax Nocturne",
            description="Deep parallax motion with nocturnal aesthetic",
            studio_inspiration="Locomotive (Montreal)",
            prompt_kernel="deep parallax layers, nocturnal palette, cinematic depth of field, premium motion design, smooth camera movements, professional color grading, high-end commercial aesthetic",
            negative_prompt="flat composition, harsh daylight, amateur, static, low quality, watermark",
            color_palette=["#1a1a2e", "#0f0f1e", "#232347", "#5c5c8a", "#9999ff"],
            motion_style="smooth parallax scrolling, depth-based motion, professional easing curves",
            audio_character="atmospheric, deep bass, cinematic ambience, subtle motion sounds",
            preferred_models={
                "image": "flux_dev",
                "video": "cogvideox",
                "audio": "musicgen"
            },
            quality_settings={
                "steps": 50,
                "guidance": 12,
                "fps": 24,
                "frames": 48,
                "audio_duration": 15
            }
        ))

        # Mode 2: Rust-Luxe Baroque (Studio Blup-inspired)
        self.modes['rust_luxe_baroque'] = CreativeMode(ModeConfig(
            name="Rust-Luxe Baroque",
            description="Decayed opulence meets modern luxury",
            studio_inspiration="Studio Blup (São Paulo)",
            prompt_kernel="rust texture over gold leaf, baroque ornamental details, luxury brand aesthetic, decaying opulence, high fashion photography, editorial lighting, premium materials, weathered elegance",
            negative_prompt="cheap, plastic, new, pristine, amateur photography, flat lighting",
            color_palette=["#8B4513", "#DAA520", "#2F4F4F", "#8B7355", "#CD853F"],
            motion_style="slow reveal, texture focus, luxury brand pacing",
            audio_character="orchestral with industrial undertones, premium sound design",
            preferred_models={
                "image": "seedream",
                "video": "svd",
                "audio": "riffusion"
            },
            quality_settings={
                "steps": 60,
                "guidance": 15,
                "fps": 30,
                "frames": 60,
                "audio_duration": 20
            }
        ))

        # Mode 3: Kinetic Typography (Obys Agency-inspired)
        self.modes['kinetic_typography'] = CreativeMode(ModeConfig(
            name="Kinetic Typography",
            description="Dynamic text as primary visual element",
            studio_inspiration="Obys Agency (Kyiv)",
            prompt_kernel="bold typographic design, kinetic text animation, Swiss design principles, dynamic letter forms, professional typography, grid-based layout, motion graphics, clean minimalism",
            negative_prompt="handwritten, comic sans, amateur fonts, cluttered, no text",
            color_palette=["#000000", "#FFFFFF", "#FF0000", "#0000FF", "#FFFF00"],
            motion_style="text-driven animation, letter morphing, typographic rhythm",
            audio_character="rhythmic, percussive, synchronized to text motion",
            preferred_models={
                "image": "ideogram",  # Best for text
                "video": "animatediff",
                "audio": "musicgen"
            },
            quality_settings={
                "steps": 40,
                "guidance": 10,
                "fps": 30,
                "frames": 90,
                "audio_duration": 10
            }
        ))

        # Mode 4: WebGL Dreams (Immersive Garden-inspired)
        self.modes['webgl_dreams'] = CreativeMode(ModeConfig(
            name="WebGL Dreams",
            description="3D web-native aesthetic with shader-like effects",
            studio_inspiration="Immersive Garden (Paris)",
            prompt_kernel="WebGL aesthetic, shader effects, 3D rendered, metallic reflections, iridescent surfaces, particle systems, real-time rendering look, interactive design aesthetic, GPU-accelerated visuals",
            negative_prompt="flat 2D, no depth, static image, print design, low poly",
            color_palette=["#00FFFF", "#FF00FF", "#7B68EE", "#4169E1", "#9370DB"],
            motion_style="3D camera movements, shader animations, particle effects",
            audio_character="electronic, generative, interactive sound design",
            preferred_models={
                "image": "flux_dev",
                "video": "zeroscope",
                "audio": "riffusion"
            },
            quality_settings={
                "steps": 45,
                "guidance": 11,
                "fps": 60,
                "frames": 120,
                "audio_duration": 12
            }
        ))

        # Mode 5: Mineral Futurism (Buck Design-inspired)
        self.modes['mineral_futurism'] = CreativeMode(ModeConfig(
            name="Mineral Futurism",
            description="Geological textures meet sci-fi aesthetics",
            studio_inspiration="Buck Design (LA/NYC)",
            prompt_kernel="crystalline structures, mineral formations, futuristic materials, geometric patterns, refractive surfaces, scientific visualization, premium 3D rendering, subsurface scattering",
            negative_prompt="organic, soft, natural, vintage, hand-drawn",
            color_palette=["#4A90E2", "#7FFF00", "#FF1493", "#00CED1", "#FFD700"],
            motion_style="crystal growth animation, refractive light play, geometric transitions",
            audio_character="crystalline tones, synthetic textures, future ambient",
            preferred_models={
                "image": "seedream",
                "video": "cogvideox",
                "audio": "musicgen"
            },
            quality_settings={
                "steps": 55,
                "guidance": 13,
                "fps": 24,
                "frames": 48,
                "audio_duration": 18
            }
        ))

        # Mode 6: Soft Brutalism (Resn-inspired)
        self.modes['soft_brutalism'] = CreativeMode(ModeConfig(
            name="Soft Brutalism",
            description="Monolithic forms with unexpected softness",
            studio_inspiration="Resn (Wellington)",
            prompt_kernel="brutalist architecture, soft gradient overlays, massive concrete forms, pastel color washes, monolithic structures, architectural photography, soft lighting on hard surfaces",
            negative_prompt="ornate, decorated, busy, natural materials, wood, plants",
            color_palette=["#C0C0C0", "#FFB6C1", "#E6E6FA", "#F0E68C", "#D3D3D3"],
            motion_style="slow architectural reveals, light play on concrete, subtle gradient shifts",
            audio_character="ambient reverb, spatial audio, architectural acoustics",
            preferred_models={
                "image": "flux_schnell",
                "video": "svd",
                "audio": "riffusion"
            },
            quality_settings={
                "steps": 50,
                "guidance": 12,
                "fps": 12,
                "frames": 36,
                "audio_duration": 25
            }
        ))

    def get_mode(self, mode_name: str) -> Optional[CreativeMode]:
        """Get a specific mode by name"""
        return self.modes.get(mode_name)

    def list_modes(self) -> List[str]:
        """List all available modes"""
        return list(self.modes.keys())

    def get_mode_info(self, mode_name: str) -> Dict[str, Any]:
        """Get detailed information about a mode"""
        mode = self.get_mode(mode_name)
        if mode:
            return asdict(mode.config)
        return {}

class ReplicateOrchestrator:
    """Orchestrate Replicate API calls with mode-specific settings"""

    def __init__(self, mode: CreativeMode):
        self.mode = mode

    def prepare_image_job(self, prompt: str, aspect_ratio: str = "1:1") -> Dict[str, Any]:
        """Prepare image generation job with mode settings"""
        params = self.mode.get_image_prompt(prompt)
        model = self.mode.config.preferred_models["image"]

        # Model-specific parameter mapping
        if "flux" in model:
            return {
                "model": model,
                "input": {
                    "prompt": params["prompt"],
                    "num_outputs": 1,
                    "aspect_ratio": aspect_ratio,
                    "output_format": "png",
                    "output_quality": 95,
                    "guidance": params["guidance_scale"],
                    "num_inference_steps": params["num_inference_steps"]
                }
            }
        elif "seedream" in model or "ideogram" in model:
            return {
                "model": model,
                "input": {
                    "prompt": params["prompt"],
                    "negative_prompt": params["negative_prompt"],
                    "width": 1024,
                    "height": 1024,
                    "num_outputs": 1,
                    "guidance_scale": params["guidance_scale"],
                    "num_inference_steps": params["num_inference_steps"]
                }
            }
        else:  # SDXL fallback
            return {
                "model": "stability-ai/sdxl",
                "input": {
                    "prompt": params["prompt"],
                    "negative_prompt": params["negative_prompt"],
                    "width": 1024,
                    "height": 1024,
                    "num_outputs": 1,
                    "guidance_scale": params["guidance_scale"],
                    "num_inference_steps": params["num_inference_steps"]
                }
            }

    def prepare_video_job(self, prompt: str = None, image_url: str = None) -> Dict[str, Any]:
        """Prepare video generation job with mode settings"""
        params = self.mode.get_video_prompt(prompt if prompt else "")
        model = self.mode.config.preferred_models["video"]

        if "cogvideox" in model and prompt:
            # Text-to-video
            return {
                "model": model,
                "input": {
                    "prompt": params["prompt"],
                    "num_frames": params["num_frames"],
                    "fps": params["fps"],
                    "guidance_scale": 7,
                    "num_inference_steps": 50
                }
            }
        elif "svd" in model and image_url:
            # Image-to-video
            return {
                "model": model,
                "input": {
                    "input_image": image_url,
                    "video_length": "25_frames",
                    "sizing_strategy": "maintain_aspect_ratio",
                    "frames_per_second": params["fps"],
                    "motion_bucket_id": 127
                }
            }
        else:
            # Zeroscope or AnimateDiff fallback
            return {
                "model": "anotherjesse/zeroscope-v2-xl",
                "input": {
                    "prompt": params["prompt"],
                    "width": 1024,
                    "height": 576,
                    "num_frames": params["num_frames"],
                    "fps": params["fps"]
                }
            }

    def prepare_audio_job(self, prompt: str) -> Dict[str, Any]:
        """Prepare audio generation job with mode settings"""
        params = self.mode.get_audio_prompt(prompt)
        model = self.mode.config.preferred_models["audio"]

        if "musicgen" in model:
            return {
                "model": "meta/musicgen",
                "input": {
                    "prompt": params["prompt"],
                    "duration": params["duration"],
                    "temperature": 0.8,
                    "top_k": 250,
                    "top_p": 0.9
                }
            }
        else:  # Riffusion fallback
            return {
                "model": "riffusion/riffusion",
                "input": {
                    "prompt_a": params["prompt"],
                    "denoising": 0.75,
                    "seed_image_id": "vibes"
                }
            }

def create_job_schema(mode_name: str, product_name: str, product_desc: str) -> Dict[str, Any]:
    """Create a complete job schema for a product campaign"""

    studio_modes = StudioModes()
    mode = studio_modes.get_mode(mode_name)

    if not mode:
        raise ValueError(f"Mode {mode_name} not found")

    orchestrator = ReplicateOrchestrator(mode)

    # Build the complete job schema
    job = {
        "meta": {
            "mode": mode_name,
            "product": product_name,
            "description": product_desc,
            "studio_inspiration": mode.config.studio_inspiration
        },
        "jobs": {
            "hero_image": orchestrator.prepare_image_job(
                f"{product_name} product hero shot, {product_desc}",
                aspect_ratio="16:9"
            ),
            "detail_shot": orchestrator.prepare_image_job(
                f"{product_name} detail close-up, premium product photography, {product_desc}",
                aspect_ratio="1:1"
            ),
            "lifestyle_shot": orchestrator.prepare_image_job(
                f"{product_name} in use, lifestyle photography, {product_desc}",
                aspect_ratio="4:3"
            ),
            "hero_video": orchestrator.prepare_video_job(
                prompt=f"{product_name} cinematic reveal, {product_desc}"
            ),
            "soundtrack": orchestrator.prepare_audio_job(
                f"product launch music for {product_name}, {mode.config.audio_character}"
            )
        }
    }

    return job

# Example usage
if __name__ == "__main__":
    # Initialize studio modes
    studio_modes = StudioModes()

    # List available modes
    print("Available Creative Modes:")
    for mode_name in studio_modes.list_modes():
        mode_info = studio_modes.get_mode_info(mode_name)
        print(f"\n{mode_name}:")
        print(f"  - {mode_info['description']}")
        print(f"  - Inspired by: {mode_info['studio_inspiration']}")

    # Create HaloOne example job
    print("\n" + "="*60)
    print("Creating HaloOne Headphones Campaign...")
    print("="*60)

    job_schema = create_job_schema(
        mode_name="parallax_nocturne",
        product_name="HaloOne",
        product_desc="Premium wireless headphones with spatial audio"
    )

    print("\nJob Schema:")
    print(json.dumps(job_schema, indent=2))