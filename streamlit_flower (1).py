import streamlit as st
import math
import random
import time
import numpy as np

# Configure page
st.set_page_config(
    page_title="💕 A Special Surprise for You 💕",
    page_icon="🌹",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Custom CSS for romantic styling
st.markdown("""
<style>
    .main-container {
        background: linear-gradient(135deg, #0D1117 0%, #161B22 50%, #0D1117 100%);
        min-height: 100vh;
        padding: 20px;
    }
    
    .romantic-title {
        color: #FF69B4;
        text-align: center;
        font-size: 2.5em;
        font-weight: bold;
        margin: 20px 0;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    
    .sweet-message {
        color: #FFB6C1;
        text-align: center;
        font-size: 1.3em;
        font-style: italic;
        margin: 15px 0;
    }
    
    .music-note {
        color: #FFD700;
        text-align: center;
        font-size: 1.1em;
        margin: 10px 0;
    }
    
    .love-message {
        color: #DC143C;
        text-align: center;
        font-size: 1.5em;
        font-weight: bold;
        margin: 20px 0;
        animation: pulse 2s infinite;
    }
    
    .flower-container {
        text-align: center;
        padding: 40px;
        background: radial-gradient(circle, rgba(13,17,23,0.9) 0%, rgba(22,27,34,0.8) 100%);
        border-radius: 20px;
        margin: 20px 0;
        box-shadow: 0 10px 30px rgba(255,105,180,0.1);
    }
    
    .petal {
        display: inline-block;
        font-size: 3em;
        margin: 5px;
        animation: bloom 2s ease-in-out infinite;
    }
    
    .center {
        font-size: 4em;
        animation: heartbeat 1.5s ease-in-out infinite;
    }
    
    .stem {
        color: #228B22;
        font-size: 2em;
        line-height: 0.5em;
    }
    
    .leaf {
        color: #228B22;
        font-size: 1.5em;
        margin: 0 10px;
    }
    
    .sparkle {
        font-size: 1.5em;
        animation: sparkle 1s ease-in-out infinite;
    }
    
    .floating-hearts {
        text-align: center;
        font-size: 2em;
        animation: float 3s ease-in-out infinite;
        margin: 20px 0;
    }
    
    @keyframes bloom {
        0%, 100% { transform: scale(1) rotate(0deg); }
        50% { transform: scale(1.1) rotate(5deg); }
    }
    
    @keyframes heartbeat {
        0%, 100% { transform: scale(1); }
        50% { transform: scale(1.2); }
    }
    
    @keyframes sparkle {
        0%, 100% { opacity: 0.3; transform: scale(0.8); }
        50% { opacity: 1; transform: scale(1.2); }
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
    }
    
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.7; }
        100% { opacity: 1; }
    }
    
    .stButton > button {
        background: linear-gradient(45deg, #FF69B4, #FF1493) !important;
        color: white !important;
        border: none !important;
        border-radius: 30px !important;
        padding: 15px 30px !important;
        font-size: 18px !important;
        font-weight: bold !important;
        box-shadow: 0 8px 15px rgba(255, 105, 180, 0.3) !important;
        transition: all 0.3s ease !important;
    }
    
    .stButton > button:hover {
        transform: translateY(-2px) !important;
        box-shadow: 0 12px 20px rgba(255, 105, 180, 0.5) !important;
    }
    
    /* Hide Streamlit default elements */
    #MainMenu {visibility: hidden;}
    .stDeployButton {display:none;}
    footer {visibility: hidden;}
    .stApp > header {visibility: hidden;}
    
    /* Dark theme for the app */
    .stApp {
        background: linear-gradient(135deg, #0D1117 0%, #161B22 50%, #0D1117 100%);
    }
</style>
""", unsafe_allow_html=True)

class ASCIIRomanticFlower:
    def __init__(self):
        self.petal_emojis = ['🌸', '🌺', '🌻', '🌷', '🌹']
        self.sparkle_emojis = ['✨', '💫', '⭐', '🌟', '⭐']
        self.heart_emojis = ['💕', '💖', '💗', '💓', '💝', '❤️', '💜', '🧡', '💛', '💚']
        
    def create_flower_display(self, bloom_stage):
        """Create ASCII art flower display"""
        flower_html = '<div class="flower-container">'
        
        # Calculate bloom progress
        bloom_progress = min(bloom_stage / 100, 1.0)
        
        # Top sparkles (only when fully bloomed)
        if bloom_progress >= 1.0:
            sparkles = ''.join([f'<span class="sparkle">{random.choice(self.sparkle_emojis)}</span>' 
                              for _ in range(5)])
            flower_html += f'<div style="margin-bottom: 20px;">{sparkles}</div>'
        
        # Top row of petals
        if bloom_progress > 0.25:
            top_petals = self._get_petals_for_stage(bloom_progress, 'top')
            flower_html += f'<div style="margin: 10px 0;">{top_petals}</div>'
        
        # Middle row with center
        if bloom_progress > 0.125:
            middle_left = self._get_petals_for_stage(bloom_progress, 'middle_left')
            center = self._get_center(bloom_progress)
            middle_right = self._get_petals_for_stage(bloom_progress, 'middle_right')
            flower_html += f'<div style="margin: 10px 0;">{middle_left}{center}{middle_right}</div>'
        
        # Bottom row of petals
        if bloom_progress > 0.375:
            bottom_petals = self._get_petals_for_stage(bloom_progress, 'bottom')
            flower_html += f'<div style="margin: 10px 0;">{bottom_petals}</div>'
        
        # Stem and leaves
        if bloom_progress > 0.5:
            stem_html = self._create_stem()
            flower_html += stem_html
        
        # Bottom sparkles
        if bloom_progress >= 1.0:
            bottom_sparkles = ''.join([f'<span class="sparkle">{random.choice(self.sparkle_emojis)}</span>' 
                                     for _ in range(3)])
            flower_html += f'<div style="margin-top: 20px;">{bottom_sparkles}</div>'
        
        flower_html += '</div>'
        return flower_html
    
    def _get_petals_for_stage(self, bloom_progress, position):
        """Get petals for specific position based on bloom stage"""
        petal_configs = {
            'top': {'count': 3, 'threshold': 0.25},
            'middle_left': {'count': 2, 'threshold': 0.125},
            'middle_right': {'count': 2, 'threshold': 0.125},
            'bottom': {'count': 3, 'threshold': 0.375}
        }
        
        config = petal_configs.get(position, {'count': 0, 'threshold': 1.0})
        
        if bloom_progress < config['threshold']:
            return ''
        
        # Calculate how many petals to show
        petals_to_show = int(config['count'] * min((bloom_progress - config['threshold']) / 0.25, 1.0))
        petals_to_show = max(1, petals_to_show)  # Always show at least 1 if threshold is met
        
        petals = []
        for i in range(petals_to_show):
            petal = random.choice(self.petal_emojis)
            petals.append(f'<span class="petal">{petal}</span>')
        
        return ''.join(petals)
    
    def _get_center(self, bloom_progress):
        """Get the flower center"""
        if bloom_progress < 0.5:
            return ''
        
        centers = ['🌼', '🌻', '💛', '🟡']
        center = random.choice(centers)
        return f'<span class="center">{center}</span>'
    
    def _create_stem(self):
        """Create the stem and leaves"""
        stem_parts = []
        
        # Stem
        for i in range(4):
            stem_parts.append('<div class="stem">|</div>')
            if i == 1:  # Add left leaf
                stem_parts.append('<div><span class="leaf">🍃</span><span class="stem">|</span></div>')
            elif i == 2:  # Add right leaf
                stem_parts.append('<div><span class="stem">|</span><span class="leaf">🍃</span></div>')
        
        return ''.join(stem_parts)

# Initialize session state
if 'flower_started' not in st.session_state:
    st.session_state.flower_started = False
if 'bloom_stage' not in st.session_state:
    st.session_state.bloom_stage = 0
if 'animation_time' not in st.session_state:
    st.session_state.animation_time = 0
if 'message_shown' not in st.session_state:
    st.session_state.message_shown = False
if 'auto_refresh' not in st.session_state:
    st.session_state.auto_refresh = True

# Create flower instance
flower = ASCIIRomanticFlower()

# Main app logic
if not st.session_state.flower_started:
    # Show initial surprise screen
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        st.markdown('<div class="romantic-title">💖 I have something special for you 💖</div>', 
                   unsafe_allow_html=True)
        
        if st.button("✨ Click for your surprise! ✨", key="surprise_button"):
            st.session_state.flower_started = True
            st.session_state.bloom_stage = 5
            st.rerun()
        
        st.markdown('<div class="sweet-message">Close your eyes, make a wish, and click... 🌟</div>', 
                   unsafe_allow_html=True)
        st.markdown('<div class="music-note">🎵 Play your favorite romantic song for the full experience! 🎵</div>', 
                   unsafe_allow_html=True)

else:
    # Show flower animation
    if not st.session_state.message_shown:
        st.markdown('<div class="romantic-title">🌹 This flower blooms just for you 🌹</div>', 
                   unsafe_allow_html=True)
        st.markdown('<div class="sweet-message">Click the button below to make it bloom faster! 💖</div>', 
                   unsafe_allow_html=True)
    
    # Control buttons
    col1, col2, col3, col4 = st.columns([1, 1, 1, 1])
    
    with col2:
        if st.button("🌸 Bloom Faster! 🌸", key="bloom_button"):
            st.session_state.bloom_stage = min(st.session_state.bloom_stage + 20, 100)
            st.rerun()
    
    with col3:
        if st.button("⏸️ Pause/Resume", key="pause_button"):
            st.session_state.auto_refresh = not st.session_state.auto_refresh
            st.rerun()
    
    # Calculate bloom progress
    bloom_progress = min(st.session_state.bloom_stage / 100, 1.0)
    
    # Display flower
    flower_html = flower.create_flower_display(st.session_state.bloom_stage)
    st.markdown(flower_html, unsafe_allow_html=True)
    
    # Show bloom progress
    st.progress(bloom_progress, text=f"Blooming... {int(bloom_progress * 100)}%")
    
    # Auto-bloom slowly
    if st.session_state.bloom_stage < 100 and st.session_state.auto_refresh:
        st.session_state.bloom_stage += 2
    
    # Update animation time
    st.session_state.animation_time += 1
    
    # Show love message when fully bloomed
    if bloom_progress >= 1.0 and not st.session_state.message_shown:
        messages = [
            "You make every moment magical! 💖",
            "Like this flower, my love for you blooms endlessly! 🌸",
            "You are my enchanted melody! 🎵💕", 
            "Forever enchanted by you! ✨❤️",
            "You're the music in my heart! 🎶💝",
            "Every day with you feels like a fairytale! 🏰💖",
            "You're my happily ever after! 👑💕"
        ]
        
        selected_message = random.choice(messages)
        st.markdown(f'<div class="love-message">{selected_message}</div>', 
                   unsafe_allow_html=True)
        
        # Add floating hearts
        hearts = ''.join([random.choice(flower.heart_emojis) for _ in range(10)])
        st.markdown(f'<div class="floating-hearts">{hearts}</div>', 
                   unsafe_allow_html=True)
        
        st.session_state.message_shown = True
        st.session_state.auto_refresh = False  # Stop auto-refresh when complete
        
        # Reset button
        if st.button("🌹 Create Another Flower 🌹", key="reset_button"):
            st.session_state.flower_started = False
            st.session_state.bloom_stage = 0
            st.session_state.animation_time = 0
            st.session_state.message_shown = False
            st.session_state.auto_refresh = True
            st.rerun()
    
    # Auto-refresh for animation
    if bloom_progress < 1.0 and st.session_state.auto_refresh:
        time.sleep(1.5)
        st.rerun()

# Add a footer with instructions
st.markdown("""
---
<div style="text-align: center; color: #888; font-size: 0.9em;">
    💡 <strong>Tips:</strong> Use "Bloom Faster!" to speed up the animation, 
    "Pause/Resume" to control the flow, and enjoy the romantic surprise! 💕
</div>
""", unsafe_allow_html=True)