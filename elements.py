from flask import Flask, jsonify, render_template, request
import periodictable as pt

# Create flask object
app = Flask(__name__)
element = pt.elements

# Define element info function for elements
def get_info_element(element):
    return {
        'name' : element.name.capitalize(),
        'atomic_number' : element.number,
        'symbol' : element.symbol,
        'atomic_mass' : element.mass,
        'crystal_structure' : element.crystal_structure
        }

# Render into html
@app.route('/')
def home():
    return render_template('index.html')

# Define Query
@app.route('/search', methods=['GET'])
def search_element():
    query = request.args.get('query','').strip()
    if not query:
        return jsonify({"error" : "Parameter 'query' diperlukan"}),400
    
    try:
        if query.isdigit():
            element = pt.elements[int(query)]
        else:
            element = pt.elements.symbol(query.capitalize())
        element_info = get_info_element(element)
        return jsonify(element_info)
    
    except ValueError:
        return jsonify({"error" : "Element is not found. Ensure symbol or atomic number valid"}),404
    except KeyError:
        return jsonify({"error" : "Element is not found. Ensure symbol or atomic number valid"}), 404  

if __name__ == '__main__':
    app.run(debug=True, port=5000)