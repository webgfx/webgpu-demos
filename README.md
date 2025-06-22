# AI Demos Showcase

A beautiful and interactive showcase of WebAI and WebGPU demos featuring the latest in browser-based AI and graphics technology.

## Features

### 🎨 Beautiful Modern Design
- **Gradient Background**: Eye-catching purple gradient background
- **Glass-morphism UI**: Modern frosted glass effects for UI elements
- **Smooth Animations**: Fluid transitions and hover effects
- **Responsive Design**: Optimized for all device sizes

### 📱 Tab-based Navigation
- **WebAI Demos**: Language models, speech recognition, text-to-speech, and conversational AI
- **WebGPU Demos**: Computer vision, image processing, graphics, and performance benchmarks
- **Demo Counts**: Each tab shows the number of available demos
- **Smart Categorization**: Demos are intelligently categorized by their primary use case

### 🔍 Interactive Features
- **Search Functionality**: Real-time search across demo titles, frameworks, and dates
- **Video Previews**: Hover over demo cards to play preview videos
- **Smooth Loading**: Loading states and staggered animations
- **External Links**: Demos open in new tabs for seamless navigation

### 🎬 Enhanced Demo Cards
- **Video Hover Effects**: Videos automatically play on hover and reset on mouse leave
- **Expandable Cards**: Cards elegantly expand on hover to show more video content
- **Rich Metadata**: Each demo shows date, framework, and description with icons
- **Gradient Overlays**: Subtle gradients enhance video visibility

## Demo Categories

### WebAI Demos
Language models, conversational AI, and text processing:
- DeepSeek R1, Llama, Phi, Qwen models
- Speech recognition (Whisper, Moonshine)
- Text-to-speech (OuteTTS)
- Vision-language models (Moondream)

### WebGPU Demos  
Computer vision, graphics, and performance:
- Image classification (MobileNetV4)
- Object segmentation (SAM)
- Background removal (MODNet)
- Image generation (Stable Diffusion)
- Performance benchmarks

## Technology Stack

- **Frontend**: HTML5, CSS3, JavaScript (ES6+)
- **Styling**: Tailwind CSS with custom animations
- **AI Frameworks**: Transformers.js, ONNX Runtime Web, TVM, MediaPipe
- **APIs**: WebGPU, WebAssembly

## Getting Started

1. **Local Development**:
   ```bash
   python -m http.server 8000
   # Visit http://localhost:8000
   ```

2. **Or simply open**: `index.html` in your browser

## File Structure

```
├── index.html          # Main website file
├── demos.js           # Demo data and metadata  
├── assets/            # Demo videos and images
│   ├── *.mp4         # Preview videos
│   ├── *.png         # Poster images
│   └── logo.png      # Site logo
└── demos/            # Individual demo implementations
    ├── webgpu-*/     # WebGPU demo folders
    └── ...
```

## Contributing

To add a new demo:

1. Add demo metadata to `demos.js`:
   ```javascript
   {
     id: "demo-name",
     api: API.WEBGPU,
     category: CATEGORY.WEBAI, // or CATEGORY.WEBGPU
     date: "2024-XX-XX",
     desc: "Demo description",
     framework: FRAMEWORK.TJS,
     url: "https://demo-url.com"
   }
   ```

2. Add assets to `assets/`:
   - `demo-name.mp4` (preview video)
   - `demo-name.png` (poster image)

## Browser Compatibility

- **Chrome/Edge**: Full WebGPU support
- **Firefox**: Limited WebGPU support (experimental)
- **Safari**: WebGPU support in development

## Acknowledgments

This website collects WebAI demos developed by creative developers around the world. Without tremendous great efforts from projects like ONNX Runtime, Transformers.js, TensorFlow.js, MediaPipe, TVM and so on, we couldn't be here with so many great demos.

Especially we want to thank Joshua Lochner, author of Transformers.js, for his full permission to freely use his images, videos and demos related to Transformers.js project.

---

Built with ❤️ for the web development community