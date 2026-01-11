"""
AI Nexus - Prism Vibrant High-Density UI
Vivid gradients, glassmorphism, and high-energy professional aesthetics.
"""

CUSTOM_CSS = """
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@400;600;700&family=Outfit:wght@700;800&display=swap');

* { margin: 0; padding: 0; box-sizing: border-box; }

:root {
    --primary: #6366F1;
    --prism-gradient: linear-gradient(135deg, #6366F1 0%, #EC4899 50%, #F59E0B 100%);
    --bg-main: #FFFFFF;
    --surface: rgba(255, 255, 255, 0.8);
    --text-main: #1E293B;
    --text-dim: #64748B;
    --border: rgba(226, 232, 240, 0.8);
}

body, .stApp {
    background: #F8FAFC !important;
    background-image: 
        radial-gradient(at 0% 0%, rgba(99, 102, 241, 0.05) 0, transparent 50%), 
        radial-gradient(at 100% 0%, rgba(236, 72, 153, 0.05) 0, transparent 50%) !important;
    font-family: 'Inter', sans-serif !important;
}

/* Visibility Reset & Label Authoritativeness */
/* We target standard elements but exclude code-related tags to allow syntax highlighting */
p, div:not(.stCode):not(pre):not(code), label, li, h1, h2, h3, h4, h5, h6 {
    color: var(--text-main) !important;
}

/* Code Blocks - Forced Light Theme for Visibility */
pre {
    background: #F8FAFC !important;
    color: #1E293B !important;
    border-radius: 8px !important;
    padding: 1rem !important;
    border: 1px solid #E2E8F0 !important;
}

code {
    color: #1E293B !important;
    font-family: 'JetBrains Mono', monospace !important;
}

/* Force syntax highlighting elements to be visible */
.stCode span {
    color: #1E293B !important; 
}

/* Specific targeting for widget labels to ensure visibility */
.stWidget label p {
    color: var(--text-main) !important;
    font-weight: 600 !important;
    font-size: 0.9rem !important;
}

/* Multiselect widget fixes */
.stMultiSelect [data-baseweb="select"] {
    background-color: white !important;
}

.stMultiSelect [data-baseweb="tag"] {
    background-color: #6366F1 !important;
    color: white !important;
}

.stMultiSelect [data-baseweb="tag"] span {
    color: white !important;
}

.stMultiSelect [role="option"] {
    color: #1E293B !important;
    background-color: white !important;
}

.stMultiSelect [role="option"]:hover {
    background-color: #F1F5F9 !important;
}

.stMultiSelect input {
    color: #1E293B !important;
}

.stMultiSelect [data-baseweb="popover"] {
    background-color: white !important;
}

/* Selectbox fixes */
.stSelectbox [data-baseweb="select"] {
    background-color: white !important;
}

.stSelectbox [data-baseweb="select"] > div {
    color: #1E293B !important;
}

.stSelectbox [role="option"] {
    color: #1E293B !important;
    background-color: white !important;
}

.stSelectbox [role="option"]:hover {
    background-color: #F1F5F9 !important;
}

/* Prism Typography */
h1 {
    font-family: 'Outfit', sans-serif !important;
    font-size: 2.25rem !important;
    font-weight: 800 !important;
    background: var(--prism-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    margin-bottom: 0.5rem !important;
}

h2 {
    font-family: 'Outfit', sans-serif !important;
    font-size: 1.5rem !important;
    color: var(--text-main) !important;
    margin: 1.5rem 0 0.75rem 0 !important;
}

/* Glassmorphism Cards */
.glass-card, .metric-card, .tool-card {
    background: var(--surface) !important;
    backdrop-filter: blur(10px) !important;
    -webkit-backdrop-filter: blur(10px) !important;
    border: 1px solid var(--border) !important;
    border-radius: 16px !important;
    padding: 1.25rem !important;
    box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05), 0 2px 4px -2px rgba(0,0,0,0.05);
    transition: all 0.3s ease;
}

.tool-card:hover {
    transform: translateY(-3px);
    border-color: #6366F1 !important;
    box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1), 0 10px 10px -5px rgba(0,0,0,0.04);
}

.metric-card {
    text-align: center;
    border-bottom: 4px solid #6366F1 !important;
}

.metric-card:nth-child(2) { border-bottom-color: #EC4899 !important; }
.metric-card:nth-child(3) { border-bottom-color: #F59E0B !important; }
.metric-card:nth-child(4) { border-bottom-color: #10B981 !important; }

.metric-value { 
    font-size: 2rem !important; 
    font-weight: 800; 
    background: var(--prism-gradient);
    -webkit-background-clip: text;
    -webkit-text-fill-color: transparent;
    font-family: 'Outfit', sans-serif !important;
}

.metric-label { 
    font-size: 0.8rem !important; 
    color: var(--text-dim) !important; 
    text-transform: uppercase; 
    font-weight: 700;
    letter-spacing: 0.1em;
}

/* Prism Buttons */
.stButton > button {
    border-radius: 12px !important;
    padding: 0.6rem 1.5rem !important;
    font-weight: 700 !important;
    transition: all 0.2s ease !important;
    border: 2px solid #6366F1 !important;
    background: transparent !important;
    color: #6366F1 !important;
}

.stButton > button:hover {
    background: #6366F1 !important;
    color: white !important;
    box-shadow: 0 4px 12px rgba(99, 102, 241, 0.3);
}

/* Action Buttons */
[key^="btn_"] > button, .stButton > button[kind="primary"] {
    background: var(--prism-gradient) !important;
    color: white !important;
    border: none !important;
    box-shadow: 0 4px 15px rgba(236, 72, 153, 0.3) !important;
    white-space: normal !important;
    text-overflow: clip !important;
    overflow: visible !important;
    height: auto !important;
    min-height: 2.5rem !important;
}

[key^="btn_"] > button:hover {
    transform: scale(1.02);
    box-shadow: 0 8px 25px rgba(236, 72, 153, 0.4) !important;
}

/* Navigation Overhaul */
[key^="topnav_"] > button {
    border: none !important;
    background: rgba(99, 102, 241, 0.05) !important;
    color: #6366F1 !important;
}

[key^="topnav_"] > button:hover {
    background: rgba(99, 102, 241, 0.15) !important;
}

/* Inputs & Form Logic - Forced Visibility */
/* Inputs & Form Logic - Forced Light Theme Override */
.stTextInput input, .stTextArea textarea {
    background-color: #FFFFFF !important;
    color: #1E293B !important;
    caret-color: #6366F1 !important;
}

/* Selectbox Specific - Target the inner container */
.stSelectbox div[data-baseweb="select"] > div {
    background-color: #FFFFFF !important;
    color: #1E293B !important;
    border-color: rgba(226, 232, 240, 0.8) !important;
}

/* Dropdown Menu / Popover - Nuclear White Override */
div[data-baseweb="popover"], div[data-baseweb="menu"], ul[data-baseweb="menu"] {
    background-color: #FFFFFF !important;
    border: 1px solid #E2E8F0 !important;
}

/* Individual Options */
div[data-baseweb="option"], li[data-baseweb="option"] {
    color: #1E293B !important;
    background-color: #FFFFFF !important;
}

/* Hover/Focus States for Options */
div[data-baseweb="option"]:hover, li[data-baseweb="option"]:hover, li[aria-selected="true"] {
    background-color: #F1F5F9 !important;
    color: #6366F1 !important;
    font-weight: 700 !important;
}

/* Hide Streamlit Frame */
#MainMenu, footer, header { visibility: hidden; }

/* Badges */
.badge {
    padding: 0.3rem 0.7rem;
    border-radius: 20px;
    font-size: 0.75rem;
    font-weight: 700;
    color: white !important;
}

/* Keyboard Style */
kbd {
    background: linear-gradient(135deg, #E2E8F0 0%, #F1F5F9 100%);
    border: 1px solid #CBD5E1;
    border-radius: 6px;
    padding: 0.2rem 0.5rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.8rem;
    color: #1E293B;
    box-shadow: 0 2px 0 #94A3B8;
}

/* Smooth Scrolling */
html {
    scroll-behavior: smooth;
}

/* Card Load Animation */
@keyframes fadeInUp {
    from {
        opacity: 0;
        transform: translateY(20px);
    }
    to {
        opacity: 1;
        transform: translateY(0);
    }
}

.glass-card, .metric-card, .tool-card {
    animation: fadeInUp 0.4s ease-out;
}

/* Focus States for Accessibility */
button:focus, input:focus, select:focus {
    outline: 2px solid #6366F1 !important;
    outline-offset: 2px;
}

/* Enhanced focus visibility for keyboard navigation */
button:focus-visible, input:focus-visible, select:focus-visible, a:focus-visible {
    outline: 3px solid #F59E0B !important;
    outline-offset: 3px;
    box-shadow: 0 0 0 6px rgba(245, 158, 11, 0.2);
}

/* Reduced motion preference - respect user accessibility settings */
@media (prefers-reduced-motion: reduce) {
    .glass-card, .metric-card, .tool-card {
        animation: none !important;
        transition: none !important;
    }
    
    * {
        animation-duration: 0.01ms !important;
        animation-iteration-count: 1 !important;
        transition-duration: 0.01ms !important;
    }
}

/* High contrast mode support */
@media (prefers-contrast: high) {
    .glass-card, .metric-card, .tool-card {
        border: 2px solid #000 !important;
    }
    
    .metric-value, h1 {
        -webkit-text-fill-color: #000 !important;
        color: #000 !important;
    }
}

/* Skip to content link (screen reader friendly) */
.skip-to-content {
    position: absolute;
    left: -9999px;
    top: 0;
    z-index: 999;
    padding: 1rem;
    background: #6366F1;
    color: white;
}

.skip-to-content:focus {
    left: 0;
}

/* ============================================
   MOBILE RESPONSIVE DESIGN
   ============================================ */

/* Tablet Devices (768px and below) */
@media (max-width: 768px) {
    /* Typography Scaling */
    h1 {
        font-size: 1.75rem !important;
        line-height: 1.2 !important;
    }
    
    h2 {
        font-size: 1.25rem !important;
        margin: 1rem 0 0.5rem 0 !important;
    }
    
    h3 {
        font-size: 1.1rem !important;
    }
    
    p, div {
        font-size: 0.95rem !important;
        line-height: 1.6 !important;
    }
    
    /* Cards - Reduce padding for mobile */
    .glass-card, .metric-card, .tool-card {
        padding: 1rem !important;
        border-radius: 12px !important;
        margin-bottom: 0.75rem !important;
    }
    
    /* Metric Cards - Stack vertically */
    .metric-value {
        font-size: 1.5rem !important;
    }
    
    .metric-label {
        font-size: 0.7rem !important;
    }
    
    /* Buttons - Touch-friendly sizing */
    .stButton > button {
        padding: 0.75rem 1rem !important;
        font-size: 0.9rem !important;
        min-height: 44px !important; /* Apple's recommended touch target */
        width: 100% !important;
    }
    
    [key^="btn_"] > button {
        min-height: 44px !important;
        padding: 0.75rem 1rem !important;
    }
    
    /* Navigation - Stack vertically on mobile */
    [key^="topnav_"] > button {
        font-size: 0.85rem !important;
        padding: 0.5rem 0.25rem !important;
        min-height: 40px !important;
    }
    
    /* Input Fields - Larger for mobile */
    .stTextInput input, .stTextArea textarea {
        font-size: 16px !important; /* Prevents zoom on iOS */
        padding: 0.75rem !important;
        min-height: 44px !important;
    }
    
    .stSelectbox select {
        font-size: 16px !important;
        padding: 0.75rem !important;
        min-height: 44px !important;
    }
    
    /* Search Input */
    [key="global_search"] input {
        font-size: 14px !important;
        padding: 0.5rem !important;
    }
    
    /* Code Blocks - Horizontal scroll */
    pre {
        overflow-x: auto !important;
        font-size: 0.85rem !important;
        padding: 0.75rem !important;
    }
    
    /* Expanders - More padding */
    .streamlit-expanderHeader {
        padding: 0.75rem !important;
        font-size: 0.95rem !important;
    }
    
    /* Tabs - Smaller text */
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 0.85rem !important;
        padding: 0.5rem 0.75rem !important;
    }
    
    /* Remove hover effects on touch devices */
    .tool-card:hover {
        transform: none !important;
    }
    
    /* Spacing adjustments */
    .stMarkdown {
        margin-bottom: 0.75rem !important;
    }
}

/* Mobile Phones (480px and below) */
@media (max-width: 480px) {
    /* Further reduce typography */
    h1 {
        font-size: 1.5rem !important;
    }
    
    h2 {
        font-size: 1.15rem !important;
    }
    
    h3 {
        font-size: 1rem !important;
    }
    
    p, div {
        font-size: 0.9rem !important;
    }
    
    /* Cards - Minimal padding */
    .glass-card, .metric-card, .tool-card {
        padding: 0.75rem !important;
        border-radius: 10px !important;
    }
    
    /* Metric Cards - Smaller values */
    .metric-value {
        font-size: 1.25rem !important;
    }
    
    .metric-label {
        font-size: 0.65rem !important;
    }
    
    /* Buttons - Full width */
    .stButton > button {
        padding: 0.65rem 0.75rem !important;
        font-size: 0.85rem !important;
    }
    
    /* Navigation - Compact */
    [key^="topnav_"] > button {
        font-size: 0.75rem !important;
        padding: 0.4rem 0.15rem !important;
    }
    
    /* Hide icon text on very small screens, keep emoji */
    [key^="topnav_"] > button {
        white-space: nowrap !important;
        overflow: hidden !important;
        text-overflow: ellipsis !important;
    }
    
    /* Code blocks - Smaller font */
    pre {
        font-size: 0.75rem !important;
        padding: 0.5rem !important;
    }
    
    code {
        font-size: 0.8rem !important;
    }
    
    /* Reduce margins */
    .stMarkdown {
        margin-bottom: 0.5rem !important;
    }
    
    /* Tabs - Very compact */
    .stTabs [data-baseweb="tab-list"] button {
        font-size: 0.75rem !important;
        padding: 0.4rem 0.5rem !important;
    }
}

/* Landscape Orientation on Mobile */
@media (max-width: 768px) and (orientation: landscape) {
    h1 {
        font-size: 1.5rem !important;
    }
    
    .glass-card, .metric-card, .tool-card {
        padding: 0.75rem !important;
    }
}

/* Touch Device Optimizations */
@media (hover: none) and (pointer: coarse) {
    /* Remove all hover effects */
    .tool-card:hover,
    .stButton > button:hover,
    [key^="btn_"] > button:hover {
        transform: none !important;
    }
    
    /* Add active state instead */
    .stButton > button:active,
    [key^="btn_"] > button:active {
        transform: scale(0.98) !important;
        opacity: 0.9 !important;
    }
    
    /* Larger tap targets */
    button, a, input, select {
        min-height: 44px !important;
        min-width: 44px !important;
    }
}

/* High DPI / Retina Displays */
@media (-webkit-min-device-pixel-ratio: 2), (min-resolution: 192dpi) {
    /* Sharper borders */
    .glass-card, .metric-card, .tool-card {
        border-width: 0.5px !important;
    }
}

/* Small Desktop / Large Tablet (1024px and below) */
@media (max-width: 1024px) {
    /* Reduce column gaps */
    .row-widget.stHorizontal {
        gap: 0.5rem !important;
    }
    
    /* Adjust container width */
    .main .block-container {
        padding-left: 1rem !important;
        padding-right: 1rem !important;
        max-width: 100% !important;
    }
}

/* Very Small Screens (320px - iPhone SE) */
@media (max-width: 320px) {
    h1 {
        font-size: 1.25rem !important;
    }
    
    h2 {
        font-size: 1rem !important;
    }
    
    p, div {
        font-size: 0.85rem !important;
    }
    
    .glass-card, .metric-card, .tool-card {
        padding: 0.5rem !important;
    }
    
    .stButton > button {
        font-size: 0.8rem !important;
        padding: 0.5rem !important;
    }
}

/* Print Styles */
@media print {
    /* Hide navigation and interactive elements */
    [key^="topnav_"], .stButton, header, footer {
        display: none !important;
    }
    
    /* Optimize for print */
    .glass-card, .metric-card, .tool-card {
        break-inside: avoid !important;
        box-shadow: none !important;
        border: 1px solid #000 !important;
    }
    
    /* Black text for print */
    * {
        color: #000 !important;
        background: #fff !important;
    }
}

</style>
"""
