from flask import Flask, request, jsonify
from flask_cors import CORS  # Import CORS

app = Flask(__name__)
CORS(app)  # Enable CORS for all routes

# Sample library metadata
library_metadata = {
    "books": [
        {
            "title": "Artificial Intelligence: A Modern Approach",
            "author": "Stuart Russell, Peter Norvig",
            "isbn": "978-0134610995",
            "year": 2020,
            "available": True,
            "location": "Shelf 12, Section A"
        },
        {
            "title": "Life 3.0: Being Human in the Age of Artificial Intelligence",
            "author": "Max Tegmark",
            "isbn": "978-1101946596",
            "year": 2017,
            "available": False,
            "due_date": "2023-06-15"
        }
    ]
}

# Function simulating LLM behavior
def llm_response(query):
    query = query.lower()
    
    if "ai" in query or "artificial intelligence" in query:
        if "define" in query or "what is" in query:
            return {
                "response": "Artificial intelligence refers to the capability of computational systems to perform tasks typically associated with human intelligence, such as learning, reasoning, problem-solving, perception, and decision-making. It is a field of research in computer science that develops and studies methods and software that enable machines to perceive their environment and use learning and intelligence to take actions that maximize their chances of achieving defined goals.",
                "books": library_metadata["books"]
            }
        elif "book" in query or "recommend" in query:
            return {
                "books": library_metadata["books"]
            }
        else:
            return {
                "response": "I can help you with general AI concepts or find books about AI in our library. What would you like to know?"
            }
    elif "library" in query or "book" in query:
        matches = []
        for book in library_metadata["books"]:
            if query in book["title"].lower() or query in book["author"].lower():
                matches.append(book)
        if matches:
            return {
                "books": matches,
            }
        else:
            return {
                "response": "I couldn't find any books matching your query. Please try another keyword."
            }
    else:
        return {
            "response": "I'm here to help with questions about AI or our library's collection. How can I assist you?"
        }

@app.route('/api/chat', methods=['POST', 'OPTIONS'])
def chat():
    if request.method == 'OPTIONS':
        return jsonify({}), 200
    
    try:
        data = request.json
        query = data.get("message", "")
        
        if not query:
            return jsonify({"response": "Please provide a valid query."})
        
        response = llm_response(query)
        print(response)
        
        return jsonify(response)
    except Exception as e:
        return jsonify({"response": "An error occurred while processing your request. Please try again later."}), 500

if __name__ == '__main__':
    app.run(debug=True)