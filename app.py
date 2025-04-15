from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=["*"])  # Enable CORS for all routes

# Expanded library metadata with more books and topics
library_metadata = {
    "ai": [
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
    ],
    "bl":[
        {
            "title": "Blockchain Revolution: How the Technology Behind Bitcoin Is Changing Money, Business, and the World",
            "author": "Don Tapscott, Alex Tapscott",
            "isbn": "978-0670088961",
            "year": 2016,
            "available": True,
            "location": "Shelf 15, Section B"
        },
        {
            "title": "Mastering Bitcoin: Unlocking Digital Cryptocurrencies",
            "author": "Andreas M. Antonopoulos",
            "isbn": "978-1491954358",
            "year": 2017,
            "available": True,
            "location": "Shelf 15, Section C"
        },
        {
            "title": "The Truth Machine: The Blockchain and the Future of Everything",
            "author": "Michael J. Casey, Paul Vigna",
            "isbn": "978-1250158040",
            "year": 2018,
            "available": True,
            "location": "Shelf 15, Section D"
        },],

    "topics": {
        "library_hours": "The library is open Monday to Friday from 9:00 AM to 8:00 PM, and Saturday to Sunday from 10:00 AM to 6:00 PM.",
        "e_books": "E-books can be accessed through our online portal using your library card. Visit our website for more details.",
        "membership": "To become a member, visit the library with a valid ID and proof of address. Membership is free for residents."
    }
}

# Function simulating LLM behavior with expanded capabilities
def llm_response(query):
    query = query.lower()
    print(query)
    response_data = {"response": "", "books": []}
    
    # Handle general topics

    if "library hours" in query or "library time" in query:
        response_data["response"] = library_metadata["topics"]["library_hours"]
    elif "e-books" in query or "ebooks" in query:
        response_data["response"] = library_metadata["topics"]["e_books"]
        print(response_data)

    elif "membership" in query or "join" in query or "register" in query:
        response_data["response"] = library_metadata["topics"]["membership"]
    
    # Handle book-related queries
    # if "book" in query or "find" in query or "recommend" in query:

    #     matches = library_metadata["ai"]
    #     response_data["response"] = f"Here are {len(matches)} book{'s' if len(matches) == 1 else ''} I found matching your query:"
    #     print("serching book.......")
    #     response_data["books"] = matches
            
    # Handle AI-specific queries
    if " ai" in query or "artificial intelligence" in query or "ai " in query:
        print("ai", "ai" in query, "artificial intelligence" in query)
        if "define" in query or "what is" in query:
            response_data["response"] = "Artificial intelligence refers to the capability of computational systems to perform tasks typically associated with human intelligence, such as learning, reasoning, problem-solving, perception, and decision-making. It is a field of research in computer science that develops and studies methods and software that enable machines to perceive their environment and use learning and intelligence to take actions that maximize their chances of achieving defined goals."
        
        response_data["response"] = "AI (Artificial Intelligence): Machines simulating human intelligence to learn, reason, and automate tasks, using data-driven decision-making to solve problems and transform industries."
        response_data["books"] = library_metadata["ai"]

    if "blockchain" in query or "block chain" in query:
        print("bl")
        if "define" in query or "what is" in query:
            response_data["response"] = "Blockchain is a decentralized, distributed ledger technology that records transactions across multiple computers, ensuring data integrity, transparency, and security without a central authority."
        
        response_data["response"] = "Blockchain is a decentralized, transparent, and immutable distributed ledger ensuring data security, widely used in cryptocurrencies, smart contracts, and supply chains."
        response_data["books"] = library_metadata["bl"]
    # Default response if no specific topic matched
    if not response_data["response"] and not response_data["books"]:
        response_data["response"] = "I'm here to help with questions about AI, library services, or our collection. How can I assist you?"
    
    return response_data

@app.route('/api/chat', methods=['POST', 'OPTIONS'])
def chat():
    if request.method == 'OPTIONS':
        return jsonify({}), 200
    
    try:
        data = request.json
        query = data.get("message", "")
        
        if not query:
            return jsonify({"response": "Please provide a valid query.", "books": []})
        
        response = llm_response(query)
        
        return jsonify(response)
    except Exception as e:
        return jsonify({"response": "An error occurred while processing your request. Please try again later.", "books": []}), 500

if __name__ == '__main__':
    app.run(debug=True)



    sk-a24398d278e74e2fa78ad9d9f6481013