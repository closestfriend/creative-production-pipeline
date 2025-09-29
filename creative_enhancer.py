#!/usr/bin/env python3
"""
Creative Enhancer - Prompt enhancement and landing page generation
Using Claude API or Replicate-hosted LLMs
"""

import os
import json
from typing import Dict, List, Optional

class CreativeEnhancer:
    """
    Enhance prompts and generate landing pages using LLMs
    """

    def __init__(self, use_claude: bool = False):
        self.use_claude = use_claude

        # Replicate-hosted LLMs (fallback when no Claude API)
        self.llm_models = {
            'llama3': 'meta/meta-llama-3-70b-instruct',
            'mistral': 'mistralai/mixtral-8x7b-instruct-v0.1',
            'claude_on_replicate': 'replicate/claude-3-haiku'  # If available
        }

        # Audio/transcription models on Replicate
        self.audio_models = {
            'whisper': 'openai/whisper',  # Transcription
            'bark': 'suno-ai/bark',  # TTS
            'elevenlabs': 'elevenlabs/voice-synthesis'  # If API key available
        }

        # Latest 2025 models from research
        self.cutting_edge_models = {
            'sora': 'openai/sora',  # When available on Replicate
            'veo3': 'google/veo-3',  # Synchronized audio-video
            'fugatto': 'nvidia/fugatto',  # Advanced audio synthesis
            'frames': 'runway/frames',  # Stylistic consistency
            'pika2': 'pika/pika-2.1',  # 1080p video
            'open_sora': 'open-sora/open-sora-2.0'  # Open source alternative
        }

    def enhance_prompt(self, original_prompt: str, style: str = 'cinematic') -> str:
        """
        Enhance a prompt using Claude or Replicate LLMs
        """

        enhancement_prompt = f"""
        Enhance this creative prompt for AI image generation.
        Original: {original_prompt}
        Style: {style}

        Add rich visual details, lighting, composition, and atmosphere.
        Keep it under 150 words. Return only the enhanced prompt.
        """

        if self.use_claude:
            # Direct Claude API call (user has Claude configured)
            return self._enhance_with_claude(enhancement_prompt)
        else:
            # Use Replicate-hosted LLM
            return self._enhance_with_replicate_llm(enhancement_prompt)

    def _enhance_with_claude(self, prompt: str) -> str:
        """Use Claude API directly (requires ANTHROPIC_API_KEY)"""
        try:
            # This would use the actual Claude API
            # For now, return a placeholder
            return f"[Enhanced via Claude]: {prompt}"
        except:
            return self._enhance_with_replicate_llm(prompt)

    def _enhance_with_replicate_llm(self, prompt: str) -> str:
        """Use Replicate-hosted LLM for enhancement"""
        import replicate

        try:
            output = replicate.run(
                self.llm_models['llama3'],
                input={
                    "prompt": prompt,
                    "max_new_tokens": 200,
                    "temperature": 0.8
                }
            )

            if output:
                return ''.join(output) if isinstance(output, list) else str(output)
        except:
            # Fallback to rule-based enhancement
            return self._rule_based_enhancement(prompt)

    def _rule_based_enhancement(self, prompt: str) -> str:
        """Simple rule-based enhancement as fallback"""
        enhancements = [
            "masterpiece quality",
            "highly detailed",
            "professional photography",
            "golden hour lighting",
            "8k resolution"
        ]
        return f"{prompt}, {', '.join(enhancements)}"

    def generate_landing_page(self, campaign_data: Dict) -> str:
        """
        Generate HTML landing page for campaign using LLM
        """

        page_prompt = f"""
        Create a modern, responsive HTML landing page for this campaign:

        Campaign: {campaign_data.get('brief_name', 'Product Launch')}
        Assets: {len(campaign_data.get('images', []))} images,
                {1 if campaign_data.get('video') else 0} videos,
                {1 if campaign_data.get('audio') else 0} audio tracks

        Include:
        - Hero section with main image
        - Grid gallery for additional images
        - Video player if video exists
        - Audio player if audio exists
        - Modern CSS with animations
        - Mobile responsive design

        Return complete HTML with inline CSS and JavaScript.
        """

        if self.use_claude:
            html = self._generate_page_with_claude(page_prompt)
        else:
            html = self._generate_page_with_template(campaign_data)

        return html

    def _generate_page_with_claude(self, prompt: str) -> str:
        """Generate full HTML using Claude"""
        # Placeholder for actual Claude API call
        return self._generate_page_with_template({})

    def _generate_page_with_template(self, data: Dict) -> str:
        """Generate HTML using template"""

        images_html = ""
        for img in data.get('images', []):
            images_html += f'''
            <div class="gallery-item">
                <img src="{img.get('url', '')}" alt="{img.get('prompt', '')[:50]}">
            </div>
            '''

        video_html = ""
        if data.get('video'):
            video_html = f'''
            <div class="video-container">
                <video controls autoplay muted loop>
                    <source src="{data['video']}" type="video/mp4">
                </video>
            </div>
            '''

        return f'''
        <!DOCTYPE html>
        <html lang="en">
        <head>
            <meta charset="UTF-8">
            <meta name="viewport" content="width=device-width, initial-scale=1.0">
            <title>{data.get('brief_name', 'Campaign')} - AI Generated</title>
            <style>
                * {{ margin: 0; padding: 0; box-sizing: border-box; }}
                body {{
                    font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
                    background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
                    min-height: 100vh;
                }}
                .container {{
                    max-width: 1200px;
                    margin: 0 auto;
                    padding: 2rem;
                }}
                .hero {{
                    text-align: center;
                    color: white;
                    padding: 4rem 0;
                }}
                h1 {{
                    font-size: 3rem;
                    margin-bottom: 1rem;
                    animation: fadeInUp 1s ease;
                }}
                .gallery {{
                    display: grid;
                    grid-template-columns: repeat(auto-fit, minmax(300px, 1fr));
                    gap: 2rem;
                    margin-top: 3rem;
                }}
                .gallery-item {{
                    background: white;
                    border-radius: 1rem;
                    overflow: hidden;
                    box-shadow: 0 20px 40px rgba(0,0,0,0.1);
                    transition: transform 0.3s ease;
                }}
                .gallery-item:hover {{
                    transform: translateY(-10px);
                }}
                .gallery-item img {{
                    width: 100%;
                    height: 100%;
                    object-fit: cover;
                }}
                .video-container {{
                    margin: 3rem 0;
                    border-radius: 1rem;
                    overflow: hidden;
                    box-shadow: 0 20px 40px rgba(0,0,0,0.2);
                }}
                video {{
                    width: 100%;
                    height: auto;
                }}
                @keyframes fadeInUp {{
                    from {{ opacity: 0; transform: translateY(30px); }}
                    to {{ opacity: 1; transform: translateY(0); }}
                }}
                .metadata {{
                    background: rgba(255,255,255,0.1);
                    backdrop-filter: blur(10px);
                    border-radius: 1rem;
                    padding: 2rem;
                    margin-top: 3rem;
                    color: white;
                }}
                .tech-stack {{
                    display: flex;
                    gap: 1rem;
                    flex-wrap: wrap;
                    margin-top: 1rem;
                }}
                .badge {{
                    background: rgba(255,255,255,0.2);
                    padding: 0.5rem 1rem;
                    border-radius: 2rem;
                    font-size: 0.875rem;
                }}
            </style>
        </head>
        <body>
            <div class="container">
                <div class="hero">
                    <h1>{data.get('brief_name', 'AI Campaign')}</h1>
                    <p>Generated with Creative Production Pipeline</p>
                    <div class="tech-stack">
                        <span class="badge">Model: {data.get('model', 'FLUX')}</span>
                        <span class="badge">Quality: {data.get('quality', 'Premium')}</span>
                        <span class="badge">Timestamp: {data.get('timestamp', '')}</span>
                    </div>
                </div>

                {video_html}

                <div class="gallery">
                    {images_html}
                </div>

                <div class="metadata">
                    <h2>Campaign Details</h2>
                    <p>This campaign was generated using state-of-the-art AI models.</p>
                    <p>Brief Type: {data.get('brief_type', 'Custom')}</p>
                    <p>Assets Generated: {len(data.get('images', []))} images
                    {', 1 video' if data.get('video') else ''}
                    {', 1 audio track' if data.get('audio') else ''}</p>
                </div>
            </div>

            <script>
                // Add progressive image loading
                document.querySelectorAll('img').forEach(img => {{
                    img.loading = 'lazy';
                }});

                // Add parallax scrolling
                window.addEventListener('scroll', () => {{
                    const scrolled = window.pageYOffset;
                    const hero = document.querySelector('.hero');
                    hero.style.transform = `translateY(${{scrolled * 0.5}}px)`;
                }});
            </script>
        </body>
        </html>
        '''

    def transcribe_audio(self, audio_url: str) -> str:
        """Transcribe audio using Whisper on Replicate"""
        import replicate

        try:
            output = replicate.run(
                self.audio_models['whisper'],
                input={
                    "audio": audio_url,
                    "model": "large-v3",
                    "language": "en",
                    "translate": False
                }
            )

            if output and 'transcription' in output:
                return output['transcription']
            return str(output)
        except Exception as e:
            return f"Transcription failed: {e}"

    def generate_voiceover(self, text: str, voice: str = "narrator") -> str:
        """Generate voiceover using Bark or ElevenLabs via Replicate"""
        import replicate

        try:
            # Try Bark first (free)
            output = replicate.run(
                self.audio_models['bark'],
                input={
                    "prompt": text,
                    "voice_preset": voice,
                    "output_full": False
                }
            )
            return output
        except:
            return None