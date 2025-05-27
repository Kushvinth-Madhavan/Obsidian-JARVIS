# OJARVIS (Obsidian JARVIS)

An AI-powered knowledge assistant that helps you search and interact with your Obsidian vault using natural language.

## Project Structure

```
Obsidian-JARVIS/
├── frontend/           # Frontend application
│   ├── index.html     # Main HTML file
│   ├── css/          # Stylesheets
│   └── js/           # JavaScript files
├── backend/           # Python backend
│   ├── main.py       # Main application entry point
│   ├── script.py     # Core functionality
│   └── requirements.txt
├── docs/             # Documentation
└── .gitignore        # Git ignore rules
```

## Features

- Natural language search interface
- Real-time search results
- Modern, responsive UI
- Integration with Obsidian vault
- AI-powered knowledge retrieval

## Setup Instructions

### Backend Setup

1. Create a virtual environment:
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

2. Install dependencies:
   ```bash
   cd backend
   pip install -r requirements.txt
   ```

3. Run the backend server:
   ```bash
   python main.py
   ```

### Frontend Setup

1. Open `frontend/index.html` in your web browser
2. Alternatively, serve the frontend using a local server:
   ```bash
   cd frontend
   python -m http.server 8000
   ```

## Development

- Frontend development: Edit files in the `frontend` directory
- Backend development: Edit files in the `backend` directory
- Make sure to follow the existing code style and add appropriate comments

## Contributing

1. Fork the repository
2. Create a feature branch
3. Commit your changes
4. Push to the branch
5. Create a Pull Request

## License

MIT License - see LICENSE file for details
