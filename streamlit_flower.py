import streamlit as st
import math
import random
import time
import numpy as np
import plotly.graph_objects as go
from plotly.subplots import make_subplots

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
    
    .surprise-button {
        background: linear-gradient(45deg, #FF69B4, #FF1493);
        color: white;
        padding: 15px 30px;
        border: none;
        border-radius: 30px;
        font-size: 18px;
        font-weight: bold;
        cursor: pointer;
        box-shadow: 0 8px 15px rgba(255, 105, 180, 0.3);
        transition: all 0.3s ease;
        text-decoration: none;
        display: inline-block;
        margin: 20px 0;
    }
    
    .surprise-button:hover {
        transform: translateY(-2px);
        box-shadow: 0 12px 20px rgba(255, 105, 180, 0.5);
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
    
    @keyframes pulse {
        0% { opacity: 1; }
        50% { opacity: 0.7; }
        100% { opacity: 1; }
    }
    
    .floating-hearts {
        position: absolute;
        animation: float 3s ease-in-out infinite;
    }
    
    @keyframes float {
        0%, 100% { transform: translateY(0px); }
        50% { transform: translateY(-20px); }
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
</style>
""", unsafe_allow_html=True)

class RomanticFlower:
    def __init__(self):
        self.petal_angle = 0
        self.heart_beat = 0
        self.sparkle_particles = []
        self.bloom_stage = 0
        self.max_bloom = 100
        self.petal_colors = ['#FF69B4', '#FF1493', '#DC143C', '#FF6347', '#FFB6C1']
        self.center_color = '#FFD700'
        self.center_x = 0
        self.center_y = 0
        
    def create_heart_petal(self, angle, size_factor=1.0, distance=1.0):
        """Create heart-shaped petal coordinates"""
        petal_size = 30 * size_factor
        
        # Heart shape coordinates
        t_values = np.linspace(0, 2*np.pi, 50)
        x_heart = petal_size * 0.05 * (16 * np.sin(t_values)**3)
        y_heart = -petal_size * 0.05 * (13 * np.cos(t_values) - 5 * np.cos(2*t_values) - 
                                       2 * np.cos(3*t_values) - np.cos(4*t_values))
        
        # Rotate the petal
        x_rotated = x_heart * np.cos(angle) - y_heart * np.sin(angle)
        y_rotated = x_heart * np.sin(angle) + y_heart * np.cos(angle)
        
        # Position the petal
        petal_distance = 60 * distance
        petal_x = self.center_x + petal_distance * np.cos(angle)
        petal_y = self.center_y + petal_distance * np.sin(angle)
        
        x_final = petal_x + x_rotated
        y_final = petal_y + y_rotated
        
        return x_final, y_final
    
    def create_flower_plot(self, bloom_progress):
        """Create the flower visualization using Plotly"""
        fig = go.Figure()
        
        # Set up the plot
        fig.update_layout(
            width=800,
            height=600,
            xaxis=dict(range=[-400, 400], showgrid=False, showticklabels=False, zeroline=False),
            yaxis=dict(range=[-300, 300], showgrid=False, showticklabels=False, zeroline=False),
            plot_bgcolor='rgba(13, 17, 23, 1)',
            paper_bgcolor='rgba(13, 17, 23, 1)',
            showlegend=False,
            margin=dict(l=0, r=0, t=0, b=0)
        )
        
        # Draw stem
        if bloom_progress > 0.3:
            fig.add_trace(go.Scatter(
                x=[self.center_x, self.center_x],
                y=[self.center_y + 50, self.center_y + 200],
                mode='lines',
                line=dict(color='#228B22', width=8),
                hoverinfo='skip'
            ))
            
            # Add leaves
            leaf_angles = [math.radians(-30), math.radians(30)]
            leaf_positions = [(self.center_x - 30, self.center_y + 120), 
                            (self.center_x + 25, self.center_y + 180)]
            
            for i, (leaf_x, leaf_y) in enumerate(leaf_positions):
                # Simple leaf shape
                leaf_t = np.linspace(0, 2*np.pi, 20)
                leaf_x_coords = leaf_x + 25 * np.cos(leaf_t) * np.cos(leaf_angles[i])
                leaf_y_coords = leaf_y + 15 * np.sin(leaf_t)
                
                fig.add_trace(go.Scatter(
                    x=leaf_x_coords,
                    y=leaf_y_coords,
                    fill='toself',
                    fillcolor='#228B22',
                    line=dict(color='#006400', width=2),
                    mode='lines',
                    hoverinfo='skip'
                ))
        
        # Draw petals
        num_petals = 8
        for i in range(num_petals):
            if bloom_progress > i * 0.12:
                angle = (2 * math.pi * i / num_petals) + self.petal_angle
                size_factor = bloom_progress * (0.8 + 0.3 * math.sin(self.heart_beat + i))
                color = self.petal_colors[i % len(self.petal_colors)]
                
                x_coords, y_coords = self.create_heart_petal(angle + math.pi/2, size_factor, bloom_progress)
                
                fig.add_trace(go.Scatter(
                    x=x_coords,
                    y=y_coords,
                    fill='toself',
                    fillcolor=color,
                    line=dict(color='#8B0000', width=2),
                    mode='lines',
                    hoverinfo='skip'
                ))
        
        # Draw flower center
        if bloom_progress > 0.5:
            center_size = 25 * bloom_progress
            beat_size = center_size + 5 * math.sin(self.heart_beat * 2)
            
            # Create circle for center
            theta = np.linspace(0, 2*np.pi, 50)
            center_x_coords = self.center_x + beat_size * np.cos(theta)
            center_y_coords = self.center_y + beat_size * np.sin(theta)
            
            fig.add_trace(go.Scatter(
                x=center_x_coords,
                y=center_y_coords,
                fill='toself',
                fillcolor=self.center_color,
                line=dict(color='#FF8C00', width=3),
                mode='lines',
                hoverinfo='skip'
            ))
        
        # Add sparkles
        if bloom_progress >= 1.0:
            for _ in range(random.randint(3, 8)):
                sparkle_x = self.center_x + random.randint(-100, 100)
                sparkle_y = self.center_y + random.randint(-100, 100)
                sparkle_size = random.randint(5, 15)
                sparkle_color = random.choice(['#FFD700', '#FFFF00', '#FFA500', '#FF69B4'])
                
                # Add sparkle as a star shape
                fig.add_trace(go.Scatter(
                    x=[sparkle_x],
                    y=[sparkle_y],
                    mode='markers',
                    marker=dict(
                        symbol='star',
                        size=sparkle_size,
                        color=sparkle_color,
                        line=dict(width=1, color='white')
                    ),
                    hoverinfo='skip'
                ))
        
        return fig

# Initialize session state
if 'flower_started' not in st.session_state:
    st.session_state.flower_started = False
if 'bloom_stage' not in st.session_state:
    st.session_state.bloom_stage = 0
if 'animation_time' not in st.session_state:
    st.session_state.animation_time = 0
if 'message_shown' not in st.session_state:
    st.session_state.message_shown = False

# Create flower instance
flower = RomanticFlower()

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
    
    # Speed up bloom button
    col1, col2, col3 = st.columns([1, 1, 1])
    with col2:
        if st.button("🌸 Bloom Faster! 🌸", key="bloom_button"):
            st.session_state.bloom_stage = min(st.session_state.bloom_stage + 15, 100)
    
    # Calculate animation parameters
    flower.petal_angle = st.session_state.animation_time * 0.03
    flower.heart_beat = st.session_state.animation_time * 0.15
    
    # Calculate bloom progress
    bloom_progress = min(st.session_state.bloom_stage / 100, 1.0)
    
    # Create and display flower
    fig = flower.create_flower_plot(bloom_progress)
    st.plotly_chart(fig, use_container_width=True, config={'displayModeBar': False})
    
    # Auto-bloom slowly
    if st.session_state.bloom_stage < 100:
        st.session_state.bloom_stage += 1.5
    
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
        st.markdown("""
        <div style="text-align: center; font-size: 2em; animation: float 2s ease-in-out infinite;">
            💕 💖 💗 💓 💝 💕 💖 💗 💓 💝
        </div>
        """, unsafe_allow_html=True)
        
        st.session_state.message_shown = True
        
        # Reset button
        if st.button("🌹 Create Another Flower 🌹", key="reset_button"):
            st.session_state.flower_started = False
            st.session_state.bloom_stage = 0
            st.session_state.animation_time = 0
            st.session_state.message_shown = False
            st.rerun()
    
    # Auto-refresh for animation
    if bloom_progress < 1.0:
        time.sleep(0.1)
        st.rerun()