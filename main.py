
import tkinter as tk
import math
import random

class SimpleRomanticFlower:
    def __init__(self, root):
        self.root = root
        self.root.title("💕 A Special Surprise for You 💕")
        self.root.geometry("800x600")
        self.root.configure(bg='#0D1117')
        
        # Create canvas
        self.canvas = tk.Canvas(root, width=800, height=600, bg='#0D1117', highlightthickness=0)
        self.canvas.pack(fill=tk.BOTH, expand=True)
        
        # Animation variables
        self.petal_angle = 0
        self.heart_beat = 0
        self.sparkle_particles = []
        self.message_visible = False
        self.bloom_stage = 0
        self.max_bloom = 100
        self.flower_started = False
        
        # Colors
        self.petal_colors = ['#FF69B4', '#FF1493', '#DC143C', '#FF6347', '#FFB6C1']
        self.center_color = '#FFD700'
        
        # Create initial elements
        self.center_x = 400
        self.center_y = 350
        
        # Show initial surprise button
        self.show_surprise_button()
        
    def show_surprise_button(self):
        """Show the initial surprise button"""
        # Create a beautiful frame for the button
        button_frame = tk.Frame(self.root, bg='#0D1117')
        button_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # Add romantic text above button
        title_label = tk.Label(button_frame, 
                              text="💖 I have something special for you 💖",
                              font=("Arial", 24, "bold"),
                              fg="#FF69B4",
                              bg="#0D1117")
        title_label.pack(pady=(0, 30))
        
        # Create the magical button
        self.surprise_button = tk.Button(button_frame,
                                        text="✨ Click for your surprise! ✨",
                                        font=("Arial", 18, "bold"),
                                        fg="black",
                                        bg="black",
                                        activebackground="#FF69B4",
                                        activeforeground="white",
                                        relief="raised",
                                        bd=5,
                                        padx=30,
                                        pady=15,
                                        command=self.start_surprise)
        self.surprise_button.pack()
        
        # Add a sweet message below
        message_label = tk.Label(button_frame,
                                text="Close your eyes, make a wish, and click... 🌟",
                                font=("Arial", 14, "italic"),
                                fg="#FFB6C1",
                                bg="#0D1117")
        message_label.pack(pady=(20, 0))
        
        # Add music instruction
        music_label = tk.Label(button_frame,
                              text="🎵 Play your favorite romantic song for the full experience! 🎵",
                              font=("Arial", 12),
                              fg="#FFD700",
                              bg="#0D1117")
        music_label.pack(pady=(15, 0))
        
        self.button_frame = button_frame
    
    def start_surprise(self):
        """Start the flower animation"""
        # Hide the button
        self.button_frame.destroy()
        
        # Start the flower animation
        self.flower_started = True
        self.bloom_stage = 5  # Start blooming immediately
        
        # Show romantic message
        self.canvas.create_text(400, 100, 
                               text="🌹 This flower blooms just for you 🌹",
                               font=("Arial", 20, "bold"),
                               fill="#FF69B4",
                               tags="opening_message")
        
        # Add instruction to click for faster blooming
        self.canvas.create_text(400, 130,
                               text="Click anywhere to make it bloom faster! 💖",
                               font=("Arial", 14),
                               fill="#FFB6C1",
                               tags="instruction")
        
        # Bind click to canvas to make flower bloom faster
        self.canvas.bind("<Button-1>", self.speed_up_bloom)
        
        # Start the animation loop
        self.animate()
    
    def create_petal(self, center_x, center_y, angle, size_factor=1.0, color="#FF69B4"):
        """Create a heart-shaped petal"""
        petal_size = 30 * size_factor
        
        # Heart shape equation
        points = []
        for i in range(0, 360, 10):
            t = math.radians(i)
            x = petal_size * (16 * math.sin(t)**3)
            y = -petal_size * (13 * math.cos(t) - 5 * math.cos(2*t) - 2 * math.cos(3*t) - math.cos(4*t))
            
            # Scale down the heart
            x = x * 0.05
            y = y * 0.05
            
            # Rotate the petal
            rotated_x = x * math.cos(angle) - y * math.sin(angle)
            rotated_y = x * math.sin(angle) + y * math.cos(angle)
            
            # Translate to position
            points.extend([center_x + rotated_x, center_y + rotated_y])
        
        return self.canvas.create_polygon(points, fill=color, outline="#8B0000", width=2, smooth=True, tags="flower")
    
    def create_leaf(self, x, y, angle, size=40):
        """Create a leaf shape"""
        leaf_points = []
        for i in range(0, 360, 20):
            t = math.radians(i)
            lx = size * 0.3 * math.cos(t)
            ly = size * math.sin(t)
            
            # Rotate
            rotated_x = lx * math.cos(angle) - ly * math.sin(angle)
            rotated_y = lx * math.sin(angle) + ly * math.cos(angle)
            
            leaf_points.extend([x + rotated_x, y + rotated_y])
        
        return self.canvas.create_polygon(leaf_points, fill="#228B22", outline="#006400", width=2, tags="flower")
    
    def create_stem(self):
        """Create the flower stem"""
        stem_x = self.center_x
        stem_bottom = 550
        
        # Main stem
        self.canvas.create_line(stem_x, self.center_y + 50, stem_x, stem_bottom,
                               fill="#228B22", width=8, capstyle=tk.ROUND, tags="flower")
        
        # Add leaves
        leaf1_x = stem_x - 30
        leaf1_y = self.center_y + 120
        self.create_leaf(leaf1_x, leaf1_y, math.radians(-30))
        
        leaf2_x = stem_x + 25
        leaf2_y = self.center_y + 180
        self.create_leaf(leaf2_x, leaf2_y, math.radians(30))
    
    def create_sparkle(self, x, y):
        """Create a sparkle effect"""
        sparkle = {
            'x': x + random.randint(-50, 50),
            'y': y + random.randint(-50, 50),
            'size': random.randint(3, 8),
            'life': 30,
            'max_life': 30,
            'color': random.choice(['#FFD700', '#FFFF00', '#FFA500', '#FF69B4'])
        }
        self.sparkle_particles.append(sparkle)
    
    def update_sparkles(self):
        """Update sparkle animations"""
        for sparkle in self.sparkle_particles[:]:
            sparkle['life'] -= 1
            if sparkle['life'] <= 0:
                self.sparkle_particles.remove(sparkle)
                continue
            
            # Draw sparkle as a simple star
            alpha = sparkle['life'] / sparkle['max_life']
            size = sparkle['size'] * alpha
            
            # Create simple star shape
            x, y = sparkle['x'], sparkle['y']
            
            # Vertical line
            self.canvas.create_line(x, y-size, x, y+size, 
                                   fill=sparkle['color'], width=2, tags="sparkle")
            # Horizontal line
            self.canvas.create_line(x-size, y, x+size, y, 
                                   fill=sparkle['color'], width=2, tags="sparkle")
            # Diagonal lines
            offset = size * 0.7
            self.canvas.create_line(x-offset, y-offset, x+offset, y+offset, 
                                   fill=sparkle['color'], width=1, tags="sparkle")
            self.canvas.create_line(x-offset, y+offset, x+offset, y-offset, 
                                   fill=sparkle['color'], width=1, tags="sparkle")
    
    def draw_flower(self):
        """Draw the complete flower"""
        if not self.flower_started:
            return
            
        # Clear previous flower elements
        self.canvas.delete("flower")
        self.canvas.delete("sparkle")
        
        # Calculate bloom progress
        bloom_progress = min(self.bloom_stage / self.max_bloom, 1.0)
        
        # Create stem first
        if bloom_progress > 0.3:
            self.create_stem()
        
        # Create petals in a circular pattern
        num_petals = 8
        for i in range(num_petals):
            angle = (2 * math.pi * i / num_petals) + self.petal_angle
            petal_distance = 60 * bloom_progress
            
            petal_x = self.center_x + petal_distance * math.cos(angle)
            petal_y = self.center_y + petal_distance * math.sin(angle)
            
            size_factor = bloom_progress * (0.8 + 0.3 * math.sin(self.heart_beat + i))
            color = self.petal_colors[i % len(self.petal_colors)]
            
            if bloom_progress > i * 0.12:
                self.create_petal(petal_x, petal_y, angle + math.pi/2, size_factor, color)
        
        # Create flower center
        if bloom_progress > 0.5:
            center_size = 25 * bloom_progress
            beat_size = center_size + 5 * math.sin(self.heart_beat * 2)
            self.canvas.create_oval(self.center_x - beat_size, self.center_y - beat_size,
                                   self.center_x + beat_size, self.center_y + beat_size,
                                   fill=self.center_color, outline="#FF8C00", width=3, tags="flower")
        
        # Add sparkles when fully bloomed
        if bloom_progress >= 1.0 and random.random() < 0.2:
            self.create_sparkle(self.center_x, self.center_y)
        
        # Update sparkles
        self.update_sparkles()
        
        # Show love message when fully bloomed
        if bloom_progress >= 1.0 and not self.message_visible:
            self.show_love_message()
            self.message_visible = True
    
    def show_love_message(self):
        """Display romantic message"""
        # Clear the opening messages
        self.canvas.delete("opening_message")
        self.canvas.delete("instruction")
        
        messages = [
            "You make every moment magical! 💖",
            "Like this flower, my love for you blooms endlessly! 🌸",
            "You are my enchanted melody! 🎵💕", 
            "Forever enchanted by you! ✨❤️",
            "You're the music in my heart! 🎶💝",
            "Every day with you feels like a fairytale! 🏰💖",
            "You're my happily ever after! 👑💕"
        ]
        
        message = random.choice(messages)
        
        
        # Create message text
        self.canvas.create_text(400, 50, 
                               text=message,
                               font=("Arial", 16, "bold"),
                               fill="#8B0000",
                               tags="message")
        
        # Add floating hearts
        for i in range(12):
            x = random.randint(100, 700)
            y = random.randint(150, 450)
            self.create_floating_heart(x, y)
    
    def create_floating_heart(self, x, y):
        """Create floating heart animation"""
        # Simple heart using two circles and a triangle
        size = random.randint(10, 20)
        
        # Create heart shape with simple circles and oval
        color = random.choice(['#FF69B4', '#FF1493', '#DC143C', '#FFB6C1'])
        
        # Left circle
        self.canvas.create_oval(x-size*0.5, y-size*0.3, x+size*0.1, y+size*0.3, 
                               fill=color, outline="", tags="heart")
        # Right circle  
        self.canvas.create_oval(x-size*0.1, y-size*0.3, x+size*0.5, y+size*0.3, 
                               fill=color, outline="", tags="heart")
        # Bottom triangle (as oval)
        self.canvas.create_oval(x-size*0.4, y-size*0.1, x+size*0.4, y+size*0.6, 
                               fill=color, outline="", tags="heart")
        
        # Animate heart floating up
        self.float_heart_group(x, y, size)
    
    def float_heart_group(self, x, y, size):
        """Animate heart floating upward"""
        # Find all hearts near this position and move them up
        for item in self.canvas.find_withtag("heart"):
            bbox = self.canvas.bbox(item)
            if bbox and abs(bbox[0] - x) < size and abs(bbox[1] - y) < size:
                if bbox[1] > 50:  # Still visible
                    self.canvas.move(item, random.randint(-1, 1), -2)
                else:
                    self.canvas.delete(item)
        
        # Continue animation if hearts exist
        if self.canvas.find_withtag("heart"):
            self.root.after(150, lambda: self.float_heart_group(x, y-2, size))
    
    def speed_up_bloom(self, event):
        """Speed up blooming when canvas is clicked"""
        if self.bloom_stage < self.max_bloom:
            self.bloom_stage += 15
    
    def animate(self):
        """Main animation loop"""
        if self.flower_started:
            self.petal_angle += 0.03
            self.heart_beat += 0.15
            
            # Auto-bloom slowly
            if self.bloom_stage < self.max_bloom:
                self.bloom_stage += 1.5
            
            self.draw_flower()
        
        self.root.after(60, self.animate)

def main():
    root = tk.Tk()
    
    # Center the window on screen
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f"+{x}+{y}")
    
    # Prevent window resizing
    root.resizable(False, False)
    
    flower = SimpleRomanticFlower(root)
    
    root.mainloop()

if __name__ == "__main__":
    main()
