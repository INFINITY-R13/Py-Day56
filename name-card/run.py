#!/usr/bin/env python3
"""
Kiro AI Digital Name Card
A Flask web application showcasing Kiro AI's capabilities
"""

from app import app

if __name__ == '__main__':
    print("🚀 Starting Kiro AI Digital Name Card...")
    print("📱 Visit: http://127.0.0.1:5000")
    print("🛑 Press Ctrl+C to stop")
    app.run(debug=True, host='127.0.0.1', port=5000)