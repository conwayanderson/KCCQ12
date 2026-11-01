# Conway Anderson - Design Portfolio

A modern, responsive portfolio website showcasing chip brand design and creative work.

## Features

- **Responsive Design**: Works perfectly on desktop, tablet, and mobile devices
- **Chip Brand Showcase**: Dedicated section highlighting chip brand identity, packaging, and marketing materials
- **Design Portfolio**: Grid layout showcasing various design projects
- **Smooth Animations**: Engaging scroll animations and hover effects
- **Mobile Navigation**: Hamburger menu for mobile devices
- **Modern UI**: Clean, professional design with gradient accents

## Structure

- `index.html` - Main HTML structure
- `styles.css` - All styling and responsive design
- `script.js` - Interactive functionality and animations

## Sections

1. **Hero** - Eye-catching introduction with call-to-action
2. **About** - Brief introduction to your design philosophy
3. **Chip Brand Design** - Showcase of chip brand work including:
   - Brand Identity
   - Package Design
   - Marketing Materials
4. **Design Work** - Portfolio grid of other design projects
5. **Contact** - Contact information and links

## Deployment

### Option 1: GitHub Pages
1. Push this code to a GitHub repository
2. Go to Settings → Pages
3. Select the branch and save
4. Your site will be live at `https://yourusername.github.io/repository-name`

### Option 2: Netlify
1. Sign up at [Netlify](https://www.netlify.com/)
2. Drag and drop the project folder
3. Your site will be live instantly with a custom URL

### Option 3: Vercel
1. Sign up at [Vercel](https://vercel.com/)
2. Import your repository
3. Deploy with one click

### Option 4: Traditional Web Hosting
Upload all files to your web server via FTP

## Customization

### Adding Your Own Images

Replace the SVG placeholders in the HTML with actual images:

```html
<!-- Replace this: -->
<div class="chip-image-placeholder">
    <svg>...</svg>
</div>

<!-- With this: -->
<div class="chip-image-placeholder">
    <img src="path/to/your/image.jpg" alt="Description">
</div>
```

### Updating Colors

Edit the CSS variables in `styles.css`:

```css
:root {
    --primary-color: #2C3E50;
    --secondary-color: #3498DB;
    --accent-color: #E74C3C;
    /* ... etc */
}
```

### Adding More Work Items

Copy and paste the `.work-item` or `.chip-card` div structure in `index.html` and add your content.

## Browser Support

- Chrome (latest)
- Firefox (latest)
- Safari (latest)
- Edge (latest)
- Mobile browsers

## License

© 2024 Conway Anderson. All rights reserved.
