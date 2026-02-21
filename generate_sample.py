from reportlab.lib.pagesizes import letter
from reportlab.pdfgen import canvas
import os

def create_sample_resume(filename):
    c = canvas.Canvas(filename, pagesize=letter)
    width, height = letter
    
    c.setFont("Helvetica-Bold", 24)
    c.drawString(100, height - 80, "John Doe")
    
    c.setFont("Helvetica", 12)
    c.drawString(100, height - 100, "Full Stack Developer | AI Enthusiast")
    
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, height - 140, "Skills")
    
    c.setFont("Helvetica", 12)
    skills = [
        "Programming: Python, JavaScript, Java, C++",
        "Frontend: React, Vue, Next.js, Tailwind CSS",
        "Backend: Node.js, Flask, Django, PostgreSQL",
        "Tools: Docker, Kubernetes, Git, AWS"
    ]
    
    y = height - 160
    for skill in skills:
        c.drawString(120, y, f"- {skill}")
        y -= 20
        
    c.setFont("Helvetica-Bold", 16)
    c.drawString(100, y - 20, "Experience")
    
    c.setFont("Helvetica", 12)
    c.drawString(120, y - 40, "Software Engineer at Tech Corp (2020 - Present)")
    c.drawString(140, y - 60, "Developed machine learning models using TensorFlow.")
    c.drawString(140, y - 80, "Built responsive web applications with React and Node.")
    
    c.save()

if __name__ == "__main__":
    # We need reportlab for this, let's see if we can install it or just use a text file
    # Actually, I'll just use a text file if reportlab is not available, 
    # but I'll try to install it first.
    pass
