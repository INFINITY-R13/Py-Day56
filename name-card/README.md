# Kiro AI - Digital Name Card

A sleek, modern digital name card built with Flask and HTML5 UP's Astral template.

## Features

- 🎨 Sleek, modern design based on HTML5 UP's Astral template
- 🤖 AI-themed customization with cyan/blue color scheme
- 📱 Mobile-friendly with smooth navigation
- ⚡ Fast loading with optimized assets
- 🎯 Professional showcase of skills and capabilities
- ✨ Smooth animations and hover effects
- 🔧 Technology stack showcase with interactive cards

## Quick Start

1. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

2. **Run the Application**
   ```bash
   python run.py
   ```

3. **Visit Your Digital Name Card**
   Open your browser and go to: `http://127.0.0.1:5000`

## Project Structure

```
name-card/
├── app.py              # Main Flask application
├── run.py              # Application runner with enhanced output
├── requirements.txt    # Python dependencies
├── templates/
│   └── index.html     # Main template with Kiro AI content
├── static/
│   ├── css/
│   │   ├── main.css   # Original HTML5 UP styles
│   │   ├── custom.css # Custom Kiro AI styling
│   │   └── noscript.css
│   ├── js/            # JavaScript files
│   ├── images/        # Template images
│   └── webfonts/      # Font files
└── README.md          # This file
```

## Customization

### Personalizing Content
Edit `templates/index.html` to customize:
- Name and title in the header
- Introduction text
- Capabilities/skills section
- About section
- Contact information and social links

### Styling
Modify `static/css/custom.css` to change:
- Color scheme (CSS variables in :root)
- Background gradients
- Technology card styling
- Animation effects
- Responsive behavior

### Images
Replace images in `static/images/` with your own:
- `bg.jpg` - Background image
- `pic01.jpg`, `pic02.jpg`, `pic03.jpg` - Section images

## Technologies Used

- **Backend**: Flask (Python web framework)
- **Frontend**: HTML5, CSS3, JavaScript
- **Template**: HTML5 UP Dimension
- **Icons**: Font Awesome
- **Fonts**: Source Sans Pro

## License

This project uses the HTML5 UP Dimension template, which is free for personal and commercial use under the CCA 3.0 license.

## Credits

- Template: [HTML5 UP Astral](https://html5up.net/astral)
- Icons: [Font Awesome](https://fontawesome.com/)
- Fonts: [Google Fonts](https://fonts.google.com/)

---

Built with ❤️ for showcasing AI capabilities in a beautiful, professional format.