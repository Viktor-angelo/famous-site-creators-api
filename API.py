from flask import Flask, jsonify, request


app = Flask(__name__)
sites = [
    {
        'id': 1,
        'title': 'google',
        'author': 'Larry page, Sergey Brin'
    },
    {
        'id': 2,
        'title': 'youtube',
        'author': 'Steve Chen, Chad hurley e Jawed Kariim'
    },
    {
        'id': 3,
        'title': 'facebook',
        'author': 'Mark Zuckerberg'
    },
    {
        'id': 4,
        'title': 'twitter',
        'author': 'Jack Dorsey'
    },
    {
        'id': 5,
        'title': 'wikpedia',
        'author': 'Jimmy Wales e Larry Sanger'
    },
    {
        'id': 6,
        'title': 'yahoo!',
        'author': 'Jerry Yang David Filo'
    },
    {
        'id': 7,
        'title': 'Reddit',
        'author': 'Steve Huffman e Alexis Ohanian'
    },
    {
        'id': 8,
        'title': 'Pinterest',
        'author': 'Ben Silbermann, Evan sharp e Paul sciarra'
    },
    {
        'id': 9,
        'title': 'Tumblr',
        'author': 'David Karp'
    },
    {
        'id': 10,
        'title': 'Buscapé',
        'author': 'Romero Rodrigues'
    },
]

# GET all sites
@app.route('/sites', methods=['GET'])
def get_all_sites():
    return jsonify(sites)

# GET site by id
@app.route('/sites/<int:id>', methods=['GET'])
def get_site_by_id(id):
    for site in sites:
        if site.get('id') == id:
            return jsonify(site)
    return jsonify({'error': 'Site not found'}), 404

# PUT update site by id
@app.route('/sites/<int:id>', methods=['PUT'])
def update_site_by_id(id):
    updated_site = request.get_json()
    for index, site in enumerate(sites):
        if site.get('id') == id:
            sites[index].update(updated_site)
            return jsonify(sites[index])
    return jsonify({'error': 'Site not found'}), 404

# POST add new site
@app.route('/sites', methods=['POST'])
def add_new_site():
    new_site = request.get_json()
    sites.append(new_site)
    return jsonify(new_site), 201

# DELETE site by id
@app.route('/sites/<int:id>', methods=['DELETE'])
def delete_site_by_id(id):
    for index, site in enumerate(sites):
        if site.get("id") == id:
            del sites[index]
            return jsonify({'message': 'Site successfully deleted'}), 200
    return jsonify({'error': 'Site not found'}), 404

if __name__ == '__main__':


    app.run(port=5000, host='localhost', debug=True)
