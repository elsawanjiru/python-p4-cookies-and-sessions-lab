from flask import Flask, jsonify, session, request

app = Flask(__name__)
app.secret_key = 'your_secret_key_here'  # Replace with your own secret key

# ...

@app.route('/articles/<int:id>', methods=['GET'])
def view_article(id):
    # Initialize page_views in session if it doesn't exist
    session['page_views'] = session.get('page_views', 0)

    # Increment page_views for this user
    session['page_views'] += 1

    if session['page_views'] <= 3:
        # Fetch and return article data here (you need to implement this part)
        article = fetch_article_data(id)
        return jsonify(article)
    else:
        return jsonify({'message': 'Maximum pageview limit reached'}), 401

# Add a route to clear the session
@app.route('/clear', methods=['POST'])
def clear_session():
    session.clear()
    return jsonify({'message': 'Session cleared'})

if __name__ == '__main__':
    app.run(port=5555)
